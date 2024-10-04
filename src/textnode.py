class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        isEqual = ((self.text == other.text) and
                    (self.text_type == other.text_type) and
                    (self.url == other.url))
        return isEqual

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    