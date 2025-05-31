import os
import shutil
from mkdocs.plugins import BasePlugin

class CopyMarkdownPlugin(BasePlugin):
    def on_post_build(self, config):
        docs_dir = config['docs_dir']
        site_dir = config['site_dir']
        for root, _, files in os.walk(docs_dir):
            for file in files:
                if file.endswith('.md'):
                    src_path = os.path.join(root, file)
                    rel_path = os.path.relpath(src_path, docs_dir)
                    dest_path = os.path.join(site_dir, rel_path)
                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                    shutil.copy2(src_path, dest_path) 