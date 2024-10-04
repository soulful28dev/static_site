import os
import shutil

from copystatic import copy_files_recursive
from markdown_blocks import markdown_to_html_node, markdown_to_blocks


dir_path_static = "./static"
dir_path_public = "./public"

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        if os.path.isfile(from_path):
            new_ext_filename = dest_path.replace(".md", ".html")
            generate_page(from_path, template_path, new_ext_filename)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md = open(from_path, 'r').read()
    tl = open(template_path, 'r').read()

    html_string = markdown_to_html_node(md).to_html()
    title_md = extract_title(md)

    tl = tl.replace("{{ Title }}", title_md)
    tl = tl.replace("{{ Content }}", html_string)

    fw = open(dest_path, "w+")
    fw.write(tl)
    fw.close()

def extract_title(markdown):
    if not markdown.startswith("# "):
        raise Exception("There is no title")
    blocks = markdown_to_blocks(markdown)
    return blocks[0][2:].strip()

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    generate_pages_recursive("content", "template.html", "public")


main()
