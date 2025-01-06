import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a test", None, {"href": "https:www.google.com", "test": "seeing if the for loop works"})
        node2 = HTMLNode("p", "This is a test", None, {"href": "https:www.google.com", "test": "seeing if the for loop works"})
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = HTMLNode("p", "This is a test", None, None)
        node2 = HTMLNode("h1", "This is a test", None, None)
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("p", "This is a test", None, {"href": "https:www.google.com", "test": "seeing if the for loop works"})
        self.assertEqual(
            ' href="https:www.google.com" test="seeing if the for loop works"', node.props_to_html()
        )

    def test_repr(self):
        node = HTMLNode("p", "This is a test", None, {'href': 'https:www.google.com', 'test': 'seeing if the for loop works'})
        self.assertEqual(
            "HTMLNode(p, This is a test, None, {'href': 'https:www.google.com', 'test': 'seeing if the for loop works'})", repr(node)
        )