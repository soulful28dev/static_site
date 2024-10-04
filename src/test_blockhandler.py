import unittest
import textwrap

from blockhandler import BlockHandler

class TestBlockHandler(unittest.TestCase):
    def test_split_block(self):
        md = textwrap.dedent("""
        # This is a heading
        
        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item
        """)

        block_handler = BlockHandler()
        lst_blocks = block_handler.markdown_to_blocks(md)

        self.assertListEqual(
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
            ],
            lst_blocks,
        )

    def test_block_type_heading(self):
        md = "# Heading 1"
        block_handler = BlockHandler()
        block_type = block_handler.block_to_block_type(md)
        self.assertEqual(block_type, "heading")

    def test_block_type_not_heading(self):
        md = "#. Heading 1"
        block_handler = BlockHandler()
        block_type = block_handler.block_to_block_type(md)
        self.assertEqual(block_type, "paragraph")

    def test_block_type_code(self):
        md = "``` test code block```"
        block_handler = BlockHandler()
        block_type = block_handler.block_to_block_type(md)
        self.assertEqual(block_type, "code")

    def test_block_type_not_code(self):
        md = "``1` test not code block```"
        block_handler = BlockHandler()
        block_type = block_handler.block_to_block_type(md)
        self.assertEqual(block_type, "paragraph")

    def test_block_type_quote(self):
        md = "> \"This is my quote test\"\n> \"This is my quote test2\""
        block_handler = BlockHandler()
        block_type = block_handler.block_to_block_type(md)
        self.assertEqual(block_type, "quote")

    def test_block_type_not_quote(self):
        md = "> \"This is my quote test\"\na > \"This is my quote test3\""
        block_handler = BlockHandler()
        block_type = block_handler.block_to_block_type(md)
        self.assertEqual(block_type, "paragraph")

    def test_block_type_unordered_list1(self):
        md = "* hehe\n* hihi\n* hoho"
        block_handler = BlockHandler()
        block_type = block_handler.block_to_block_type(md)
        self.assertEqual(block_type, "unordered_list")

    def test_block_type_unordered_list2(self):
        md = "- hehe\n- hihi\n- hoho"
        block_handler = BlockHandler()
        block_type = block_handler.block_to_block_type(md)
        self.assertEqual(block_type, "unordered_list")

    def test_block_type_not_unordered_list1(self):
        md = "* hehe\n* hihi\n * hoho"
        block_handler = BlockHandler()
        block_type = block_handler.block_to_block_type(md)
        self.assertEqual(block_type, "paragraph")

    def test_block_type_not_unordered_list2(self):
        md = "* hehe\n* hihi\n- hoho"
        block_handler = BlockHandler()
        block_type = block_handler.block_to_block_type(md)
        self.assertEqual(block_type, "paragraph")

    def test_block_type_not_unordered_list3(self):
        md = "* hehe\n* hihi\n*hoho"
        block_handler = BlockHandler()
        block_type = block_handler.block_to_block_type(md)
        self.assertEqual(block_type, "paragraph")

    def test_block_type_ordered_list1(self):
        md = "1. hehe\n2. hihi\n3. hoho"
        block_handler = BlockHandler()
        block_type = block_handler.block_to_block_type(md)
        self.assertEqual(block_type, "ordered_list")

    def test_block_type_ordered_list2(self):
        md = "1. hehe"
        block_handler = BlockHandler()
        block_type = block_handler.block_to_block_type(md)
        self.assertEqual(block_type, "ordered_list")

    def test_block_type_not_ordered_list1(self):
        md = "1. hehe\n3. hihi\n2. hoho"
        block_handler = BlockHandler()
        block_type = block_handler.block_to_block_type(md)
        self.assertEqual(block_type, "paragraph")

    def test_block_type_not_ordered_list2(self):
        md = "1. hehe\n. hihi\n2. hoho"
        block_handler = BlockHandler()
        block_type = block_handler.block_to_block_type(md)
        self.assertEqual(block_type, "paragraph")

    def test_block_type_not_ordered_list3(self):
        md = "hehe\n. hihi\n2. hoho"
        block_handler = BlockHandler()
        block_type = block_handler.block_to_block_type(md)
        self.assertEqual(block_type, "paragraph")

    
    

if __name__ == "__main__":
    unittest.main()