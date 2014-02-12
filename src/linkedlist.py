
#All type of nodes
STRING = 0
KEYWORD = 1
MODIFIER = 2
EOL = 3 #END_OF_LINE
ROOT = 4

class Node():
    """ Node class. Basic building block of the LinkedList class."""

    def __init__(self, data, type):
    """ Constructor. 

    Args: data - Data for the node
          type - Type of the node
    
    Returns: None
    """

        self.data = data
        self.type = type
        self.next = None

    def add_node(self, node):
    """ Appends a node to the end of the current node. 
        
        Args: node - Node to append. """

        self.next = node

    def set_indent(self, indent):
    """ Sets the indent level for this node. 

        Args: indent - Integer of indent level. """

        self.indent = indent

    def get_indent(self):
    """ Returns the indent level """

        return self.indent

    def get_data(self):
    """ Returns the node data """

        return self.data

    def get_type(self):
    """ Returns the node type """

        return self.type

class LinkedList(Node):
    """ Class inheriting from Node and makes a pretty (shitty) SLL. """

    def __init__(self, root):
    """ Constructor. 
        
        Args: root - The root node. """

        self.root = root 
        self.next = None

    def get_data(self, node):
    """ Returns the data for the node given. """

        return node.get_data()

    def get_next_node(self, node):
    """ Returns the node appended to the given node. """

        return node.next

    def get_root(self):
    """ Returns the root node. """

        return self.root
