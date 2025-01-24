import unittest

from textnode import TextNode, TextType, split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_basics(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("This is text with `code`", TextType.TEXT)

        self.assertEqual([
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ], split_nodes_delimiter([node], "`", TextType.CODE))

        self.assertEqual([
            TextNode("This is text with ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode("", TextType.TEXT)
        ], split_nodes_delimiter([node2], "`", TextType.CODE))

    def test_lst(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("This is text with `code`", TextType.TEXT)

        self.assertEqual([
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            TextNode("This is text with ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode("", TextType.TEXT)
        ], split_nodes_delimiter([node, node2], "`", TextType.CODE))