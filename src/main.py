import sys
import translator
from parse import Parser

def main():
""" Get's the first CLI argument, passes it to the parser, 
    parses it, turns it into tokens and translates the tokens. """

    arg = sys.argv[1]
    parser = Parser(arg)
    parser.parse()
    tokens = parser.get_constructed()
    foo = translator.translate(tokens)

    #Print the output
    print(foo)


if __name__ == "__main__":
    main()
