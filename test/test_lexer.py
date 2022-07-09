"""Test file for lexer module."""
from lib.lexer import Lexer
from lib.file import FileInfo
from lib.token import Token
from lib.token_types import TokenType


def test_parser():
    """Funtion for test the lexer module.
    """
    file = FileInfo('test', 'test.mg')
    tokens1 = [Token(TokenType.CONSTRAINT, "window", file, file),
               Token(TokenType.INT, '100', file, file), Token(TokenType.INT, '200', file, file),
               Token(TokenType.FLOAT, "1.023", file, file)]
    parser = Lexer(" window 100 200 1.023", file)
    tokens, errors = parser.parse()
    parser = Lexer(" ! window", file)
    tokens3, errors = parser.parse()

    assert str(tokens1) == str(tokens)
    assert not tokens3
    assert errors is not None
