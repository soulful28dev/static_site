import unittest

from textnodeconverter import TextNodeConverter
from textnode import TextNode

class TestTextNodeConverter(unittest.TestCase):
    def test_converter_text(self):
        converter = TextNodeConverter()
        text_node = TextNode("Hello World", "text")
        leaf_node = converter.text_node_to_html_node(text_node)

        self.assertEqual(leaf_node.to_html(), "Hello World")

    def test_converter_bold(self):
        converter = TextNodeConverter()
        text_node = TextNode("Hello World", "bold")
        leaf_node = converter.text_node_to_html_node(text_node)

        self.assertEqual(leaf_node.to_html(), "<b>Hello World</b>")

    def test_converter_italic(self):
        converter = TextNodeConverter()
        text_node = TextNode("Hello World", "italic")
        leaf_node = converter.text_node_to_html_node(text_node)

        self.assertEqual(leaf_node.to_html(), "<i>Hello World</i>")

    def test_converter_code(self):
        converter = TextNodeConverter()
        text_node = TextNode("Hello World", "code")
        leaf_node = converter.text_node_to_html_node(text_node)

        self.assertEqual(leaf_node.to_html(), "<code>Hello World</code>")

    def test_converter_link(self):
        converter = TextNodeConverter()
        text_node = TextNode("Hello World", "link", "http://www.boot.dev")
        leaf_node = converter.text_node_to_html_node(text_node)

        self.assertEqual(leaf_node.to_html(), "<a href=\"http://www.boot.dev\">Hello World</a>")

    def test_converter_image(self):
        converter = TextNodeConverter()
        text_node = TextNode("Hello World", "image", "http://www.boot.dev")
        leaf_node = converter.text_node_to_html_node(text_node)

        self.assertEqual(leaf_node.to_html(), "<img alt=\"Hello World\" src=\"http://www.boot.dev\"></img>")

    

    def test_md_convert_to_textnodes(self):
        converter = TextNodeConverter()
        raw_md = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        text_nodes = converter.md_to_textnodes(raw_md)

        self.assertListEqual(
            [
                TextNode("This is ", "text"),
                TextNode("text", "bold"),
                TextNode(" with an ", "text"),
                TextNode("italic", "italic"),
                TextNode(" word and a ", "text"),
                TextNode("code block", "code"),
                TextNode(" and an ", "text"),
                TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", "text"),
                TextNode("link", "link", "https://boot.dev"),
            ],
            text_nodes,
        )
    

if __name__ == "__main__":
    unittest.main()