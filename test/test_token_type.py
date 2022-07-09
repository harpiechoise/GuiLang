"""Token types testing."""
from lib.token_types import TokenType


def test_token_type():
    """Test the token types."""
    # Test string representation of token type
    assert "INT" == str(TokenType.INT)
    assert "FLOAT" == str(TokenType.FLOAT)
    assert "CONSTRAINT" == str(TokenType.CONSTRAINT)
    # Test repr of token type
    assert "INT" == repr(TokenType.INT)
    assert "FLOAT" == repr(TokenType.FLOAT)
    assert "CONSTRAINT" == repr(TokenType.CONSTRAINT)
