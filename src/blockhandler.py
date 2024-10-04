import re

class BlockHandler():
    def __init__(self):
        pass

    def markdown_to_blocks(self, markdown):
        lst_block = filter(lambda block: len(block) != 0, markdown.split("\n\n"))
        lst_block_strip = list(map(lambda block: block.strip(), lst_block))
        return lst_block_strip

    def block_to_block_type(self, block):
        # Check heading format
        heading_format = ["# ", "## ", "### ", "#### ", "##### ", "###### "]
        if block.startswith("#"):
            is_heading_block = False
            sub_blocks = block.split("\n")

            if len(sub_blocks) != 1:
                is_heading_block = False
            else:
                for heading in heading_format:
                    if block.startswith(heading):
                        is_heading_block = True
        
            if is_heading_block:
                return "heading"

        # Check code block
        code_block_format = "```"
        if block.startswith("`"):
            block_prefix = block[:3]
            block_suffix = block[-3:]
            is_code_block = (block_prefix == code_block_format and 
                            block_suffix == code_block_format and
                            len(block) >= 6)

            if is_code_block:
                return "code"

        # Check quote block
        quote_block_format = ">"
        if block.startswith(">"):
            lines = block.split("\n")
            is_quote_block = True
            for line in lines:
                if not line.startswith(">"):
                    is_quote_block = False
                    break

            if is_quote_block:
                return "quote"

        # Check unordered list block
        unordered_list_format = ["*", "-"]
        if block.startswith("* ") or block.startswith("- "):
            type_unordered_prefix = block[0]

            lines = block.split("\n")
            is_unordered_list_block = True
            for line in lines:
                if not line.startswith(f"{type_unordered_prefix} "):
                    is_unordered_list_block = False
                    break

            if is_unordered_list_block:
                return "unordered_list"

        # Check ordered list block
        if block.startswith("1. "):
            lines = block.split("\n")
            is_ordered_list_block = True
            num_count = 1
            for line in lines:
                if (len(line) < 3) or (is_ordered_list_block == False):
                    is_ordered_list_block = False
                    break

                prefix = line[:3]
                is_ordered_list_block = (prefix == f"{num_count}. ")
                num_count += 1

            if is_ordered_list_block:
                return "ordered_list"

        return "paragraph"

    