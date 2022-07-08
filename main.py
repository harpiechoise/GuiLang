import lib

PATH = './gui.mg'

with open(PATH, 'r') as f:
    data = f.read()

filename = PATH.split('\\')[-1].split('.')[0]

file = lib.FileInfo(filename, PATH)

parser = lib.Parser(data, file)

tokens, errors = parser.parse()
if errors:
    print(errors)
else:
    print(tokens)