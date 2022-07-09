"""Main testing file"""
import lib

PATH = './gui.mg'

with open(PATH, 'r', encoding='utf8') as f:
    data = f.read()

filename = PATH.rsplit('\\', maxsplit=1)[-1].split('.')[0]

file = lib.FileInfo(filename, PATH)

lexer = lib.Lexer(data, file)

tokens, errors = lexer.parse()
parser = lib.Parser(tokens)
tree = parser.parse()

if errors:
    print(errors)
else:
    print(tree)
