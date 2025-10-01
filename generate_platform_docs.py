#!/usr/bin/env python3
"""
Generate platform-specific documentation files for ChatGPT training.
This script extracts content from markdown files and creates separate files
for Shopify, Shopify (Legacy), and WooCommerce platforms.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple


class DocGenerator:
    def __init__(self, docs_dir: str = "docs", base_url: str = "https://docs.revenuehunt.com"):
        self.docs_dir = Path(docs_dir)
        self.base_url = base_url
        self.platforms = {
            'shopify': 'Shopify',
            'shopify-legacy': 'Shopify (Legacy)',
            'woocommerce': 'WooCommerce'
        }
        # Platforms to exclude
        self.exclude_platforms = ['Magento', 'BigCommerce', 'Standalone']
        
    def get_doc_url(self, md_file_path: Path) -> str:
        """Convert markdown file path to documentation URL."""
        # Get relative path from docs directory
        rel_path = md_file_path.relative_to(self.docs_dir)
        # Remove .md extension and convert to URL
        url_path = str(rel_path).replace('.md', '').replace('\\', '/')
        # Handle index files
        if url_path.endswith('/index'):
            url_path = url_path[:-6]  # Remove /index
        return f"{self.base_url}/{url_path}/"
    
    def parse_markdown_file(self, file_path: Path) -> Dict[str, List[str]]:
        """
        Parse a markdown file and extract content for each platform.
        Returns a dict with platform names as keys and content lines as values.
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        content = {
            'generic': [],
            'Shopify': [],
            'Shopify (Legacy)': [],
            'WooCommerce': [],
        }
        
        current_platform = 'generic'
        in_platform_section = False
        platform_indent = 0
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Check for platform-specific section marker
            platform_match = re.match(r'^===\s+"([^"]+)"', line)
            if platform_match:
                platform_name = platform_match.group(1)
                
                # Skip excluded platforms
                if platform_name in self.exclude_platforms:
                    # Find the end of this platform section
                    i += 1
                    if i < len(lines):
                        # Get the indentation of the content
                        next_line = lines[i] if i < len(lines) else ''
                        if next_line.strip():
                            section_indent = len(next_line) - len(next_line.lstrip())
                            # Skip all lines with this indentation or more
                            while i < len(lines):
                                line = lines[i]
                                # Check if we hit another === section or unindented content
                                if line.strip() and not line.startswith(' ' * section_indent):
                                    if re.match(r'^===\s+"([^"]+)"', line):
                                        break
                                    if not line.startswith(' '):
                                        break
                                i += 1
                    continue
                
                # Set current platform for included platforms
                if platform_name in content:
                    current_platform = platform_name
                    in_platform_section = True
                    i += 1
                    # Get the indentation level of the content
                    if i < len(lines) and lines[i].strip():
                        platform_indent = len(lines[i]) - len(lines[i].lstrip())
                    continue
                else:
                    # Unknown platform, skip it
                    i += 1
                    continue
            
            # Check if we're leaving a platform section
            if in_platform_section:
                # If line is not indented enough or is a new === section, we're done
                if line.strip():
                    line_indent = len(line) - len(line.lstrip())
                    if line_indent < platform_indent or re.match(r'^===\s+"([^"]+)"', line):
                        current_platform = 'generic'
                        in_platform_section = False
                        platform_indent = 0
                        if not re.match(r'^===\s+"([^"]+)"', line):
                            content['generic'].append(line)
                            i += 1
                        continue
            
            # Add line to appropriate section
            if current_platform in content:
                if in_platform_section and line.strip():
                    # Remove platform-specific indentation
                    if len(line) >= platform_indent:
                        dedented_line = line[platform_indent:]
                        content[current_platform].append(dedented_line)
                    else:
                        content[current_platform].append(line)
                elif not in_platform_section:
                    content['generic'].append(line)
            
            i += 1
        
        return content
    
    def find_all_markdown_files(self) -> List[Path]:
        """Find all markdown files in the docs directory."""
        md_files = []
        for file_path in self.docs_dir.rglob('*.md'):
            md_files.append(file_path)
        return sorted(md_files)
    
    def generate_output_files(self):
        """Generate the three platform-specific output files."""
        # Collect all content
        all_content = {
            'shopify': [],
            'shopify-legacy': [],
            'woocommerce': []
        }
        
        md_files = self.find_all_markdown_files()
        print(f"Found {len(md_files)} markdown files")
        
        for md_file in md_files:
            print(f"Processing: {md_file.relative_to(self.docs_dir)}")
            
            # Get the URL for this file
            doc_url = self.get_doc_url(md_file)
            
            # Parse the file
            parsed_content = self.parse_markdown_file(md_file)
            
            # For each platform, combine generic + platform-specific content
            for platform_key, platform_name in self.platforms.items():
                output = []
                output.append("=" * 80)
                output.append(f"SOURCE: {doc_url}")
                output.append("=" * 80)
                output.append("")
                
                # Add generic content
                if parsed_content['generic']:
                    generic_text = ''.join(parsed_content['generic']).strip()
                    if generic_text:
                        output.append(generic_text)
                        output.append("")
                
                # Add platform-specific content
                if parsed_content[platform_name]:
                    platform_text = ''.join(parsed_content[platform_name]).strip()
                    if platform_text:
                        output.append(f"--- {platform_name} Specific Content ---")
                        output.append("")
                        output.append(platform_text)
                        output.append("")
                
                # Only add to output if there's content
                full_text = '\n'.join(output).strip()
                if full_text and len(full_text) > len("=" * 80) + len(f"SOURCE: {doc_url}") + len("=" * 80):
                    all_content[platform_key].append('\n'.join(output))
                    all_content[platform_key].append("\n\n")
        
        # Write output files
        for platform_key, platform_name in self.platforms.items():
            output_file = f"{platform_key}.txt"
            print(f"\nGenerating {output_file}...")
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"Documentation for {platform_name}\n")
                f.write("=" * 80)
                f.write("\n\n")
                f.write("This file contains all documentation content relevant to ")
                f.write(f"{platform_name}.\n")
                f.write("Each section includes the source URL for reference.\n")
                f.write("=" * 80)
                f.write("\n\n\n")
                
                f.write('\n'.join(all_content[platform_key]))
            
            print(f"✓ Created {output_file}")
            # Get file size
            size_kb = os.path.getsize(output_file) / 1024
            print(f"  Size: {size_kb:.2f} KB")


def main():
    """Main function to run the documentation generator."""
    print("=" * 80)
    print("Documentation Generator for Platform-Specific Training Data")
    print("=" * 80)
    print()
    
    generator = DocGenerator()
    generator.generate_output_files()
    
    print("\n" + "=" * 80)
    print("Documentation generation complete!")
    print("=" * 80)
    print("\nGenerated files:")
    print("  - shopify.txt")
    print("  - shopify-legacy.txt")
    print("  - woocommerce.txt")
    print("\nThese files can be used to train ChatGPT for customer support.")


if __name__ == "__main__":
    main()
