from textnode import TextNode
from leafnode import LeafNode

from nodedelimiter import NodeDemimiter
from linkextracter import LinkExtracter

class TextNodeConverter():
    def __init__(self):
        pass

    def md_to_textnodes(self, raw_md):
        pre_node = TextNode(raw_md, "text")

        node_delimiter = NodeDemimiter()
        link_extracter = LinkExtracter()

        new_nodes = node_delimiter.split_nodes_delimiter([pre_node], "**", "bold")
        new_nodes = node_delimiter.split_nodes_delimiter(new_nodes, "*", "italic")
        new_nodes = node_delimiter.split_nodes_delimiter(new_nodes, "`", "code")
        
        new_nodes = link_extracter.split_nodes_image(new_nodes)
        new_nodes = link_extracter.split_nodes_link(new_nodes)

        return new_nodes

    def text_node_to_html_node(self, text_node):
        if text_node.text_type == "text":
            return LeafNode(tag = None, value = text_node.text, props = None)
        if text_node.text_type == "bold":
            return LeafNode(tag = "b", value = text_node.text, props = None)
        if text_node.text_type == "italic":
            return LeafNode(tag = "i", value = text_node.text, props = None)
        if text_node.text_type == "code":
            return LeafNode(tag = "code", value = text_node.text, props = None)
        if text_node.text_type == "link":
            props = {
                "href": f"{text_node.url}"
            }
            return LeafNode(tag = "a", value = text_node.text, props = props)
        if text_node.text_type == "image":
            props = {
                "alt": f"{text_node.text}",
                "src": f"{text_node.url}",
            }
            return LeafNode(tag = "img", value = "", props = props)

        else:
            raise Exception("Invalid text_node_type")