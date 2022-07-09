"""Test the parser file"""
import os
from lib.parser import IntNode, FloatNode, ConstraintNode, TupleNode
from lib.token import Token
from lib.token_types import TokenType
from lib.file import TextContainer, FileInfo
import lib

def test_nodes():
    """Test all the nodes"""
    pos1 = TextContainer('test', TextContainer('test', FileInfo('test', 'test.mg')))
    pos2 = TextContainer('test', TextContainer('test', FileInfo('test', 'test.mg')))
    token_int = Token(TokenType.INT, '100', pos1, pos2)

    node_int = IntNode(token_int)
    node_int.evaluate()
    assert node_int.value == 100
    assert node_int.token == token_int

    token_float = Token(TokenType.FLOAT, '1.023', pos1, pos2)
    node_float = FloatNode(token_float)
    node_float.evaluate()
    assert node_float.value == 1.023
    assert node_float.token == token_float
    args = TupleNode([node_int, node_float])
    token = Token(TokenType.CONSTRAINT, 'window', pos1, pos2)
    node = ConstraintNode(token, args=args)
    node.evaluate()
    assert node.value == 'window'
    assert node.token == token
    assert node.args == args
    assert len(args.values) == 2
    assert args.values == [node_int, node_float]

    assert str(node) ==\
        ("ConstraintNode(value='window'"
         ", args=TupleNode(values=[IntNode(value=100), FloatNode(value=1.023)]))")
    assert repr(node) ==\
        ("ConstraintNode(value='window'"
         ", args=TupleNode(values=[IntNode(value=100), FloatNode(value=1.023)]))")

    assert str(node_int) == "IntNode(value=100)"
    assert str(node_float) == "FloatNode(value=1.023)"
    assert str(args) == "TupleNode(values=[IntNode(value=100), FloatNode(value=1.023)])"

    assert repr(node_int) == "IntNode(value=100)"
    assert repr(node_float) == "FloatNode(value=1.023)"
    assert repr(args) == "TupleNode(values=[IntNode(value=100), FloatNode(value=1.023)])"

def test_parser():
    """Test the parser tree generator"""
    path = './test/parser_test.mg'

    with open(path, 'r', encoding='utf8') as file_:
        data = file_.read()

    filename = path.rsplit('\\', maxsplit=1)[-1].split('.')[0]

    file = lib.FileInfo(filename, path)

    lexer = lib.Lexer(data, file)

    tokens, _ = lexer.parse()
    parser = lib.Parser(tokens)
    assert parser.current == -1
    assert not parser.parse_tree
    token_1 = Token(TokenType.INT, "100", lexer.text.copy(), lexer.text.copy())
    node_1 = IntNode(token_1)

    token_2 = Token(TokenType.INT, "100", lexer.text.copy(), lexer.text.copy())
    node_2 = IntNode(token_2)
    tree = parser.parse()
    args = TupleNode([
            node_1,
        ]
    )
    
    args.evaluate()
    node = ConstraintNode(Token(TokenType.CONSTRAINT, 'window',
                                lexer.text.copy(),
                                lexer.text.copy()), args=args)

    assert str(tree[0]) == str(node)
    term = Token(TokenType.FLOAT, "1.023", lexer.text.copy(), lexer.text.copy())
    float_term = parser.parse_terms(term)
    float_term.evaluate()
    assert str(FloatNode(term).evaluate()) == str(float_term)
