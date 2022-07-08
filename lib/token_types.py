"""All Primitive Tokens."""
from enum import Enum


class TokenType(Enum):
    """Enum to hold the different types of tokens."""

    INT = "INT"
    FLOAT = "FLOAT"
    CONSTRAINT = "CONSTRAINT"

    def __str__(self):
        """Represent the token as string."""
        return self.value

    def __repr__(self):
        """Represent the token as internal string."""
        return self.value
