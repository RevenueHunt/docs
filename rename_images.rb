#!/usr/bin/env ruby

require 'fileutils'
require 'pathname'

# Track renamed files for reference updating
RENAMED_FILES = {}

def find_image_files(directory)
  Dir.glob(File.join(directory, '**', '*')).select do |file|
    File.file?(file) && 
    file.match?(/\.(png|jpg|jpeg|gif|webp)$/i) && 
    file.include?(' ')
  end
end

def rename_image_files(files)
  files.each do |file|
    old_name = File.basename(file)
    new_name = old_name.gsub(' ', '_')
    new_path = File.join(File.dirname(file), new_name)
    
    begin
      FileUtils.mv(file, new_path)
      RENAMED_FILES[old_name] = new_name
      puts "Renamed: #{old_name} -> #{new_name}"
    rescue => e
      puts "Error renaming #{file}: #{e.message}"
    end
  end
end

def find_markdown_files(directory)
  Dir.glob(File.join(directory, '**', '*.md'))
end

def update_markdown_references(files)
  files.each do |file|
    content = File.read(file)
    modified = false
    
    RENAMED_FILES.each do |old_name, new_name|
      # Handle both standard markdown and HTML image tags
      if content.include?(old_name)
        content.gsub!(old_name, new_name)
        modified = true
      end
    end
    
    if modified
      begin
        File.write(file, content)
        puts "Updated references in: #{file}"
      rescue => e
        puts "Error updating #{file}: #{e.message}"
      end
    end
  end
end

def main
  docs_dir = 'docs'
  images_dir = File.join(docs_dir, 'images')
  
  puts "Starting image renaming process..."
  
  # Find and rename image files
  image_files = find_image_files(images_dir)
  if image_files.empty?
    puts "No image files with spaces found."
    return
  end
  
  puts "\nFound #{image_files.size} image files with spaces."
  rename_image_files(image_files)
  
  # Find and update markdown files
  markdown_files = find_markdown_files(docs_dir)
  if markdown_files.empty?
    puts "No markdown files found."
    return
  end
  
  puts "\nFound #{markdown_files.size} markdown files."
  update_markdown_references(markdown_files)
  
  puts "\nProcess completed!"
  puts "Renamed #{RENAMED_FILES.size} files"
end

if __FILE__ == $PROGRAM_NAME
  main
end 