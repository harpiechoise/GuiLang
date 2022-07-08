"""Generalize token."""

from dataclasses import dataclass
from typing import Any


@dataclass
class Token:
    """Generalize token, all token have a value and a type."""

    type: Any
    value: str

    def __str__(self):
        """Represent the token as string."""
        return f"{self.type}(value={self.value})"

    def __repr__(self):
        """Represent the token as internal string."""
        return self.__str__()
