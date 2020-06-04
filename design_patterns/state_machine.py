"""State-based program for parsing XML file to text. Parser ingests XML
file as a string and iterates through it. Parser can have one of several
states, depending on what element of the XML file it is currently examining.

All states share a common interface. All have a single 'process' method,
and return the remaining unprocessed part of the input string, and directly
set the state of the calling Parser."""


"""Basic tree node representing element of final tree"""
class Node:
    def __init__(self, tag_name, parent=None, tag_param = None):
        self.parent = parent
        self.tag_name = tag_name
        self.tag_param = tag_param
        self.children = []
        self.text = ""

    def __str__(self):
        output = (f"""{self.tag_name}"""
            f"""{" (" + self.tag_param + ")" if self.tag_param else ""}"""
            f"""{": " + self.text if self.text else ""}"""
        )
        return output

"""Context class responsible for recording current state
and overseeing the parsing process"""
class Parser:
    def __init__(self, parse_string):
        self.parse_string = parse_string
        self.root = None
        self.current_node = None

        self.state = FirstTag()

    def process(self, remaining_string):
        remaining = self.state.process(remaining_string, self)
        if remaining:
            self.process(remaining)

    def start(self):
        self.process(self.parse_string)


"""Define some states"""
"""Initial state that sets root property of Parser"""
class FirstTag:
    def process(self, remaining_string, parser):
        i_start_tag = remaining_string.find("<")
        i_end_tag = remaining_string.find(">")
        tag_name = remaining_string[i_start_tag + 1 : i_end_tag]
        root = Node(tag_name)
        parser.root = parser.current_node = root
        parser.state = ChildNode()
        return remaining_string[i_end_tag + 1 :]

"""Reponsible for choosing Parser's state based on first
character of remaining_string"""
class ChildNode:
    def process(self, remaining_string, parser):
        stripped = remaining_string.strip()
        if stripped.startswith("</"):
            parser.state = CloseTag()
        elif stripped.startswith("<"):
            parser.state = OpenTag()
        else:
            parser.state = TextNode()
        return stripped

"""Deals with opening tags. Creates new node and appends it to
children of current_node"""
class OpenTag:
    def process(self, remaining_string, parser):
        i_start_tag = remaining_string.find("<")
        i_end_tag = remaining_string.find(">")
        tag_name = remaining_string[i_start_tag + 1 : i_end_tag]
        tag_param = None
        if tag_name.find(" ") >= 0:
            tag_name = tag_name.split(" ")
            tag_param = tag_name[1]
            tag_name = tag_name[0]
        node = Node(tag_name, parser.current_node)
        if tag_param:
            node.tag_param = tag_param
        parser.current_node.children.append(node)
        parser.current_node = node
        parser.state = ChildNode()
        return remaining_string[i_end_tag +1 :]

"""Deals with closing tags. Verifies that tag matches
corresponding opening tag, and sets current_node to parent"""
class CloseTag:
    def process(self, remaining_string, parser):
        i_start_tag = remaining_string.find("<")
        i_end_tag = remaining_string.find(">")
        assert remaining_string[i_start_tag + 1] == "/"
        tag_name = remaining_string[i_start_tag + 2 : i_end_tag]
        assert tag_name == parser.current_node.tag_name
        parser.current_node = parser.current_node.parent
        parser.state = ChildNode()
        return remaining_string[i_end_tag + 1:].strip()

"""Adds text to current_node's text attribute"""
class TextNode:
    def process(self, remaining_string, parser):
        i_start_tag = remaining_string.find("<")
        text = remaining_string[:i_start_tag]
        parser.current_node.text = text
        parser.state = ChildNode()
        return remaining_string[i_start_tag:]


""" Setup to run from Bash"""
if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as file:
        contents = file.read()
        p = Parser(contents)
        p.start()

        nodes = [p.root]
        while nodes:
            node = nodes.pop(0)
            print(node)
            nodes = node.children + nodes