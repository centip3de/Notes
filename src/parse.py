from linkedlist import *

KEYWORDS = ["def", "sec", "code", "", "code:"] #Definition, section, code start, addition, code end
MODIFIERS = ["u", "b", "i", "!", "u:", "b:", "i:", "i:\n", "b:\n"] #Start underline, start bold, start intalics, important. End underline, end bold, end italics.

class Parser():
    """ A really shitty parser that parses the given file and turns it into nodes. """

    def __init__(self, file):
    """ Constructor. 

        Args: file - The file to parse. """

        self.file = file
        self.list = None
        self.data = []
        self.root_node = None

    def parse(self):
    """ Parses the file given in the constructor. """

        file = open(self.file, "r")
        root = Node("", ROOT)
        self.root_node = root
        in_code = False

        #Every line in the file
        for line in file.readlines():
            line = line.strip()
            tokens = line.split()

            #Every token in the line
            for token in tokens:
                indent_level = 0
                i = 0
                type = 0

                #Set the indent level for every ':' found
                while(token[i] == ":"):
                    indent_level += 1
                    i += 1

                #Set the type of the node as Keyword, Modifier, or String.
                if(token[i:] in KEYWORDS and ":" in token):
                    type = KEYWORD
                    if("code:" == token):
                        in_code = True
                    elif(":code" == token):
                        in_code = False
                    indent_level -= 1

                elif(token[i:] in MODIFIERS):
                    type = MODIFIER
                    indent_level -= 1

                else:
                    type = STRING


                #Append the token's data to the 'data' list
                self.data.append(token[i:] + " ")

                
                #Make a new node and set the values
                node = Node(token[i:], type)
                node.set_indent(indent_level)

                #Add the node
                root.add_node(node)
                root = root.next
                
            #At the end of everyline, make a EOL node 
            node = Node("\n", EOL)
            node.set_indent(0)
            root.add_node(node) 
            root = root.next

        #List now equals the constructed LinkedList
        self.list = LinkedList(self.root_node)

    def get_constructed(self):
    """ Returns the constructed LinkedList """
        return self.list

    def get_data(self):
    """ Returns the data. """
        return self.data
