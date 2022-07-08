from lib.lexer import Lexer
from lib.file import FileInfo
from lib.token import Token
from lib.token_types import TokenType


def test_parser():
    file = FileInfo('test', 'test.mg')
    tokens1 = [Token(TokenType.CONSTRAINT, "window"),
               Token(TokenType.INT, '100'), Token(TokenType.INT, '200'),
               Token(TokenType.FLOAT, "1.023")]
    parser = Lexer(" window 100 200 1.023", file)
    tokens, errors = parser.parse()
    parser = Lexer(" ! window", file)
    tokens3, errors = parser.parse()

    assert tokens1 == tokens
    assert tokens3 == []
    assert errors is not None
