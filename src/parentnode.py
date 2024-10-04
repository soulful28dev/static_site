
from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, value = None, children = children, props = props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode doesn't have tag")

        if len(self.children) is None:
            raise ValueError("ParentNode invalid with empty child")

        child_node_str = ""

        for child_node in self.children:
            child_node_str += child_node.to_html()

        open_tag = self.get_html_open_tag()
        close_tag = self.get_html_close_tag()

        return f"{open_tag}{child_node_str}{close_tag}"