import unittest

from textnode import TextNode
from nodedelimiter import NodeDemimiter

class TestNodeDemimiter(unittest.TestCase):
    def test_split_node(self):
        node = TextNode("This is text with a **bolded** word", "text")
        node_delimiter = NodeDemimiter()
        new_nodes = node_delimiter.split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text"),
                TextNode("bolded", "bold"),
                TextNode(" word", "text"),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", "text"
        )
        node_delimiter = NodeDemimiter()
        new_nodes = node_delimiter.split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text"),
                TextNode("bolded", "bold"),
                TextNode(" word and ", "text"),
                TextNode("another", "bold"),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", "text"
        )
        node_delimiter = NodeDemimiter()
        new_nodes = node_delimiter.split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text"),
                TextNode("bolded word", "bold"),
                TextNode(" and ", "text"),
                TextNode("another", "bold"),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", "text")
        node_delimiter = NodeDemimiter()
        new_nodes = node_delimiter.split_nodes_delimiter([node], "*", "italic")
        self.assertListEqual(
            [
                TextNode("This is text with an ", "text"),
                TextNode("italic", "italic"),
                TextNode(" word", "text"),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", "text")
        node_delimiter = NodeDemimiter()
        new_nodes = node_delimiter.split_nodes_delimiter([node], "**", "bold")
        new_nodes = node_delimiter.split_nodes_delimiter(new_nodes, "*", "italic")
        self.assertListEqual(
            [
                TextNode("bold", "bold"),
                TextNode(" and ", "text"),
                TextNode("italic", "italic"),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", "text")
        node_delimiter = NodeDemimiter()
        new_nodes = node_delimiter.split_nodes_delimiter([node], "`", "code")
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text"),
                TextNode("code block", "code"),
                TextNode(" word", "text"),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()