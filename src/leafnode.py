from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        super().__init__(tag, value, children = None, props = props)

    def to_html(self):
        if self.value == None:
            raise ValueError()

        if self.tag == None:
            return self.value
        
        return self.to_html_default()
