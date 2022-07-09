"""Parser for .sgui files."""
from abc import ABC, abstractmethod

from lib.token_types import TokenType


class NodeBase(ABC):
    """Base class for all the nodes in the tree."""
    @abstractmethod
    def evaluate(self):
        """Evaluate the node, and return a value."""

    @abstractmethod
    def __str__(self):
        """Represent the node as string."""

    @abstractmethod
    def __repr__(self):
        """Represent the node as internal string."""


class IntNode(NodeBase):
    """Node to represent integer values
    """
    def __init__(self, token) -> None:
        self.token = token
        self.value = None

    def evaluate(self):
        self.value = int(self.token.value)
        return self

    def __str__(self):
        return f"IntNode(value={self.value})"

    def __repr__(self):
        return self.__str__()


class FloatNode(NodeBase):
    """Node to represent float values
    """
    def __init__(self, token) -> None:
        super().__init__()
        self.token = token
        self.value = None

    def evaluate(self):
        self.value = float(self.token.value)
        return self

    def __str__(self):
        return f"FloatNode(value={self.value})"

    def __repr__(self):
        return f"FloatNode(value={self.value})"


class TupleNode(NodeBase):
    """Represent the values
    """
    def __init__(self, tokens: list):
        """List of tokens to create the tuple.

        Args:
            tokens (list): List of tokens to create the tuple.
        """
        self.token = tokens
        self.values = []
        self.count = 0
        self.evaluate()

    def evaluate(self):
        """Evaluate the values of the nodes in the tuple
        """
        for node in self.token:
            if hasattr(node, "evaluate"):
                self.values.append(node.evaluate())
            else:
                # TODO: Not a node error
                print("Not a node")
        return self

    def __repr__(self):
        """Represent the node as internal string.

        Returns:
            stt: string representation of the node.
        """
        return self.__str__()

    def __str__(self):
        """Represent the node as string.

        Returns:
            str: String representation of the node.
        """
        return f"TupleNode(values={self.values})"


class ConstraintNode(NodeBase):
    """A Constraint or function node
    """
    def __init__(self, token, args):
        """A node for represent a any type constraint.

        Args:
            token (Token): Token of the constraint.
            args (_type_): Arguments of the constraint.
        """
        self.token = token
        self.value = token.value
        self.args = args

    def evaluate(self):
        return self

    def __str__(self):
        return f"ConstraintNode(value='{self.value}', args={self.args})"

    def __repr__(self):
        return self.__str__()


class Parser:
    """Parse the tokens into node for evaluation
    """
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.current = -1
        self.parse_tree = []

    def parse(self):
        """Parse the tokens
        """
        while self.current < len(self.tokens)-1:
            self.advance()
            args = None

            if self.current_token.type == TokenType.CONSTRAINT:
                constraint_token = self.current_token
                self.advance()
                if self.current_token.type == TokenType.LPAREN:
                    args = self.parse_tuple()
                else:
                    # TODO: Handle constraint without arguments
                    print("Constraint without arguments")
                constraint = ConstraintNode(constraint_token, args)
                self.parse_tree.append(constraint)
        return self.parse_tree

    def parse_terms(self, term):
        """Parse a term

        Args:
            term (Token): A token representing the
                term and his value
        """
        if term.type == TokenType.INT:
            return IntNode(term)
        elif term.type == TokenType.FLOAT:
            return FloatNode(term)


    def advance(self):
        """Advance the cursor to the next token
        """
        self.current += 1
        self.current_token = self.tokens[self.current]

    def parse_tuple(self):
        """Parse a tuple
        """
        tokens = []
        count = 0
        while self.current_token.type != TokenType.RPAREN:

            if self.current_token.type == TokenType.COMMA:
                count += 1
            else:
                node = self.parse_terms(self.current_token)
                if node:
                    tokens.append(node)
            self.advance()
        return TupleNode(tokens)
