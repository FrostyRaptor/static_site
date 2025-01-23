import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextToHTMLNode(unittest.TestCase):
    def test_func(self):
        text_node = TextNode("This is normal text", TextType.TEXT)
        bold_node = TextNode("This text is bold", TextType.BOLD)
        italic_node = TextNode("Italic text here now", TextType.ITALIC)
        code_node = TextNode("Wow so much code here", TextType.CODE)
        link_node = TextNode("And now a link", TextType.LINK, "https://www.google.com")
        image_node = TextNode("And we end with this image", TextType.IMAGE, "https://www.image.com")

        self.assertEqual("LeafNode(None, This is normal text, None)", repr(text_node_to_html_node(text_node)))
        self.assertEqual("LeafNode(b, This text is bold, None)", repr(text_node_to_html_node(bold_node)))
        self.assertEqual("LeafNode(i, Italic text here now, None)", repr(text_node_to_html_node(italic_node)))
        self.assertEqual("LeafNode(code, Wow so much code here, None)", repr(text_node_to_html_node(code_node)))
        self.assertEqual("LeafNode(a, And now a link, {'href': 'https://www.google.com'})", repr(text_node_to_html_node(link_node)))
        self.assertEqual("LeafNode(img, , {'src': 'https://www.image.com', 'alt': 'And we end with this image'})", repr(text_node_to_html_node(image_node)))