import re
import sys

def main():
    """ Get's the first CLI argument, regex substitution magic, done."""

    arg = sys.argv[1]
    file = open(arg, "r")
    text = file.read()

    text = re.sub(r'(:def) (\w+)', r'* ** \2 **', text)
    text = re.sub(r':code', r'```', text)
    text = re.sub(r'(:i) (\w+) (:i)', r'*\2*', text)
    text = re.sub(r'(:b) (\w+) (:b)', r'** \2 **', text)
    text = re.sub(r'(:sec) (.*)(\n)', r'\2\n---', text, flags=re.MULTILINE)
    text = re.sub(r'(:)(\w|\*)', r'\t* \2', text)
    print(text)

if __name__ == "__main__":
    main()
