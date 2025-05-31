from setuptools import setup, find_packages

setup(
    name="copy_markdown_plugin",
    version="0.1",
    packages=["plugins"],
    entry_points={
        "mkdocs.plugins": [
            "copy_markdown_plugin = plugins.copy_markdown_plugin:CopyMarkdownPlugin"
        ]
    },
) 