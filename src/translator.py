from parse import Parser 

#All types of nodes 
STRING = 0
KEYWORD = 1
MODIFIER = 2
EOL = 3
ROOT = 4


def translate(tokens):
    """ Does the actual translation. Reads in the tokens and spits out the equivilent in MD.

    Args: Tokens - A LinkedList of tokens

    Returns: The constructed MD in a string.
    """

    node = tokens.get_root()

    constructed = "" 

    #New line found
    NL = False

    in_code = False

    while(node != None):
        if(node.get_type() == ROOT):
            pass

        else:
            type = node.get_type()
            data = node.get_data().strip()

            #Add a tab for every indent specified 
            constructed += "\t" * node.get_indent()

            #If it's not a keyword, we're not in code, and it's not a blank line, add make it a bullet point.
            if(NL and not in_code and data != "" and node.get_type() != KEYWORD):
                constructed += "* "
                NL = False

            if(type == MODIFIER):

                #Italics start
                if(data == "i"):
                    constructed += "*"

                #Bold start
                elif(data == "b"):
                    constructed += "**"

                #Italics end
                elif(data == "i:"):
                    constructed += "*"

                #Bold end
                elif(data == "b:"):
                    constructed += "**"

            elif(type == KEYWORD):

                #Specific definition syntax
                if(data == "def"):
                    constructed += "* **"
                    node = node.next
                    constructed += node.get_data() + "**"
                    NL = False

                elif(data == ""):
                    constructed += "* "

                #Code block syntax
                elif(data == "code:"):
                    constructed += "```"
                    node = node.next

                    #Ignore everything until the end of the code block
                    while(node.get_type() != KEYWORD and node.get_type() != "code"):
                        constructed += node.get_data() + " "
                        node = node.next

                    constructed += "```"

                #Section block syntax
                elif(data == "sec"):
                    node = node.next

                    #Ignore everything until the end of the line, then append "--" under it
                    while(node.get_type() != EOL):
                        constructed += node.get_data() + " "
                        node = node.next
                    constructed += node.get_data() + "--"

            elif(type == EOL):
                constructed += node.get_data() + "\n"
                NL = True

            elif(type == STRING):
                constructed += node.get_data() + " "

            else:
                print("Unrecognized data " + data + ".")

        node = node.next

    return constructed
