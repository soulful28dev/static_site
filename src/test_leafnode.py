import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_convert_leafnode1(self):
        leaf_node1 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf_node1.to_html(), "<p>This is a paragraph of text.</p>")

    def test_convert_leafnode2(self):
        leaf_node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf_node2.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

if __name__ == "__main__":
    unittest.main()