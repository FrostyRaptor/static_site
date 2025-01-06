from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    htmlnode = HTMLNode("p", "This is a test", None, {"href": "https:www.google.com", "test": "seeing if the for loop works"})
    print(node)
    print(htmlnode.props_to_html())

main()