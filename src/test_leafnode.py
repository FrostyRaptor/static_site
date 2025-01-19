import unittest

from htmlnode import HTMLNode, LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        self.assertEqual("<p>This is a paragraph of text.</p>", node.to_html())
        self.assertEqual('<a href="https://www.google.com">Click me!</a>', node2.to_html())

    def test_repr(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        self.assertEqual(
            "LeafNode(p, This is a paragraph of text., None)", repr(node)
        )
        self.assertEqual(
            "LeafNode(a, Click me!, {'href': 'https://www.google.com'})", repr(node2)
        )

    def test_eq(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("p", "This is a paragraph of text.")
        node3 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        node4 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        self.assertEqual(node, node2)
        self.assertEqual(node3, node4)