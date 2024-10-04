import unittest

from linkextracter import LinkExtracter
from textnode import TextNode

class TestLinkExtracter(unittest.TestCase):
    def test_linkext1(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        link_extracter = LinkExtracter()
        list_attrs = link_extracter.extract_markdown_images(text)

        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"), 
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
            ],
            list_attrs,
        )

    def test_linkext2(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        link_extracter = LinkExtracter()
        list_attrs = link_extracter.extract_markdown_links(text)

        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"), 
                ("to youtube", "https://www.youtube.com/@bootdotdev")
            ],
            list_attrs,
        )

    def test_linkext3(self):
        node = TextNode(
            "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            "text",
        )
        link_extracter = LinkExtracter()
        new_nodes = link_extracter.split_nodes_image([node])
        
        self.assertListEqual(
            [
                TextNode("This is text with a link ", "text"),
                TextNode("to boot dev", "image", "https://www.boot.dev"),
                TextNode(" and ", "text"),
                TextNode(
                    "to youtube", "image", "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes
        )

    def test_linkext4(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            "text",
        )
        link_extracter = LinkExtracter()
        new_nodes = link_extracter.split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("This is text with a link ", "text"),
                TextNode("to boot dev", "link", "https://www.boot.dev"),
                TextNode(" and ", "text"),
                TextNode(
                    "to youtube", "link", "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes
        )


if __name__ == "__main__":
    unittest.main()