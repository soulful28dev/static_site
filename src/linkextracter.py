import re

from textnode import TextNode

class LinkExtracter:
    def __init__(self):
        pass

    def split_nodes_image(self, old_nodes):
        new_nodes = []
        for old_node in old_nodes:
            if old_node.text_type != "text":
                new_nodes.append(old_node)
                continue
            
            img_list = self.extract_markdown_images(old_node.text)
            
            if len(img_list) == 0:
                new_nodes.append(old_node)
                continue

            raw_node_text = old_node.text

            split_nodes = []
            if len(img_list) != 0:
                img_alt, img_link = img_list[0]
                img_pattern = f"![{img_alt}]({img_link})"
                sections = raw_node_text.split(img_pattern, 1)

                for i in range(len(sections)):
                    if sections[i] == "":
                        continue

                    if i == len(sections) - 1:
                        split_nodes.extend(self.split_nodes_image([TextNode(sections[i], "text")]))
                    else:
                        split_nodes.append(TextNode(sections[i], "text"))
                        split_nodes.append(TextNode(img_alt, "image", img_link))
                        raw_node_text = raw_node_text.removeprefix(sections[i] + img_pattern)

            new_nodes.extend(split_nodes)
        
        return new_nodes

    def split_nodes_link(self, old_nodes):
        new_nodes = []
        for old_node in old_nodes:
            if old_node.text_type != "text":
                new_nodes.append(old_node)
                continue
            
            link_list = self.extract_markdown_links(old_node.text)

            if len(link_list) == 0:
                new_nodes.append(old_node)
                continue

            raw_node_text = old_node.text

            split_nodes = []
            if len(link_list) != 0:
                link_alt, link = link_list[0]
                link_pattern = f"[{link_alt}]({link})"
                sections = raw_node_text.split(link_pattern, 1)

                for i in range(len(sections)):
                    if sections[i] == "":
                        continue

                    if i == len(sections) - 1:
                        split_nodes.extend(self.split_nodes_link([TextNode(sections[i], "text")]))
                    else:
                        split_nodes.append(TextNode(sections[i], "text"))
                        split_nodes.append(TextNode(link_alt, "link", link))
                        raw_node_text = raw_node_text.removeprefix(sections[i] + link_pattern)

            new_nodes.extend(split_nodes)
        
        return new_nodes

    def extract_markdown_images(self, text):
        list_ext = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
        return list_ext

    def extract_markdown_links(self, text):
        list_ext = re.findall(r"\[(.*?)\]\((.*?)\)", text)
        return list_ext

    def extract_img_alt(self, img_attr):
        list_ext = re.search(r"!\[(.*?)\]". img_attr)
        if list_ext:
            return list_ext.found(1)
        else: 
            return None

    def extract_img_src(self, img_attr):
        list_ext = re.search(r"\((.*?)\)". img_attr)
        if list_ext:
            return list_ext.found(1)
        else: 
            return None