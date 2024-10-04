import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_link_node(self):
        node = HTMLNode("link", "Hello World", children = None, props = {
            "href": "https://www.google.com", 
            "target": "_blank",
        })
        self.assertEqual(node.aprops_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")

    def test_img_node(self):
        node = HTMLNode("img", value = None, children = None, props = {
            "src": "img_girl.jpg"
        })
        self.assertEqual(node.aprops_to_html(), " src=\"img_girl.jpg\"")

    def test_img_wh_node(self):
        node = HTMLNode("img", value = None, children = None, props = {
            "src": "img_girl.jpg",
            "width": "500",
            "height": "600"
        })
        self.assertEqual(node.aprops_to_html(), " src=\"img_girl.jpg\" width=\"500\" height=\"600\"")

    

if __name__ == "__main__":
    unittest.main()