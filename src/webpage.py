import os
from block_markdown import markdown_to_html_node

def extract_title(md: str) -> str:
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")

def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as f:
        markdown = f.read()
    with open(template_path, 'r') as f:
        template = f.read()

    html = markdown_to_html_node(markdown).to_html()

    title = extract_title(markdown)
    template = template.replace('{{ Title }}', title)
    template = html.replace('{{ Content }}', html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template)