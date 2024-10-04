
from blockhandler import BlockHandler

class HTMLConverter():
    def __init__(self):
        pass

    def markdown_to_html_node(self, markdown):
        blockhandler = BlockHandler()
        blocks = blockhandler.markdown_to_blocks(markdown)

        for block in blocks:
            node = self.create_node(block_type, block)

    def create_node(self, block):
        blockhandler = BlockHandler()
        block_type = blockhandler.block_to_block_type(block)

        if block_type == "paragraph":
            pass

        if block_type == "heading":
            pass

        if block_type == "code":
            pass

        if block_type == "quote":
            pass

        if block_type == "unordered_list":
            pass

        if block_type == "ordered_list":
            pass

# - `paragraph`
# - `heading`
# - `code`
# - `quote`
# - `unordered_list`
# - `ordered_list`


