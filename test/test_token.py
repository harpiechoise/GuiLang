from lib.token import Token
from lib.token_types import TokenType

def test_token_string_repr():
    # Test that the string representation of a token is the token type and value
    t = Token(TokenType.INT, '1')
    s = str(t)
    
    assert "INT(value=1)" == s
    assert "INT(value=1)" == repr(t)