from enum import Enum

from htmlnode import LeafNode
from extract_markdown import extract_markdown_images, extract_markdown_links

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception(f"Node isn't one of the main types")
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    text_node_lst = []            

    for node in old_nodes:
        tmp = node.text.split(delimiter)
        for index in range(len(tmp)):
            if index == 1:
                text_node_lst.append(TextNode(tmp[index], text_type))
                continue
            text_node_lst.append(TextNode(tmp[index], TextType.TEXT))

    return text_node_lst

def split_nodes_image(old_nodes):
    new_nodes_lst = []

    for node in old_nodes:
        matches =  extract_markdown_images(node.text)

    return new_nodes_lst

def split_nodes_link(old_nodes):
    new_nodes_lst = []



    return new_nodes_lst