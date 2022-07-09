"""Test for the token class."""
from lib.token import Token
from lib.file import FileInfo
from lib.token_types import TokenType


def test_token_string_repr():
    """Test the token creation and the string representation
    """
    # Test that the string representation
    # of a token is the token type and value
    file = FileInfo('test', 'test.mg')

    token = Token(TokenType.INT, '1', file, file)
    str_ = str(token)

    assert "INT(value=\"1\")" == str_
    assert "INT(value=\"1\")" == repr(token)
