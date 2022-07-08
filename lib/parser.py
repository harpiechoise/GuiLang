"""Generate the tokens from an input file."""

from lib.file import TextContainer
from lib.token import Token
from lib.token_types import TokenType
from lib.error import UnrecognizedTokenError
import string


class Parser:
    """Responsible for generating the tokens from the input file.
       All the tokens error are handled by the parser."""

    def __init__(self, text, file):
        """Initialize the Parser.

        Args:
            text (str): Text of the input file.
            file (file): File information for the TextContainer.
        """
        self.text = TextContainer(text, file)
        self.current_char = None
        self.advance()

    def parse(self):
        """Generate the tokens from the input file."""
        tokens = []
        # Finite state machine to parse the input file
        while self.current_char is not None:
            # If the char is digit, it is a number
            if self.current_char.isdigit():
                tokens.append(self.parse_number())
            # We ignore the spaces
            elif self.current_char in " \t":
                self.advance()
                continue
            # If the char is a letter, it is a constraint
            elif self.current_char in string.ascii_letters:
                token = self.parse_constraint()
                tokens.append(token)

            else:
                # If the token was not recognized,
                # We let the error class handle the error
                position_initial = self.text.copy()
                token = self.parse_unrecognized_token()
                return [], UnrecognizedTokenError(token,
                                                  position_initial,
                                                  self.text.copy())
            # Advance the index
            self.advance()
        return tokens, None

    def parse_constraint(self):
        """Parse the constraints strings."""
        # Constraints ends with an space
        constraint = ""
        while True:
            # If the char is a space, we stop, All characters are part of a
            # constraint
            constraint += self.current_char
            self.advance()
            if self.current_char == ' ' or self.current_char is None:
                break
        return Token(TokenType.CONSTRAINT, constraint)

    def parse_unrecognized_token(self):
        """If the token is not recognized, advance the index to the end
        position of the unrecognized token."""
        token = ""
        # We advance until we find a space or the end of the end of
        # the unrecognized token
        while self.current_char is not None \
                and not self.current_char.isspace():
            token += self.current_char
            self.advance()
        return token

    def parse_number(self):
        """Parse a float or an integer token."""
        point_count = 0
        number = ""
        while self.current_char is not None\
                and (self.current_char.isdigit() or self.current_char == '.'):

            # A number with two periods is invalid
            if point_count > 1:
                # TODO: Invalid float error
                raise Exception("Invalid number")
            if self.current_char == '.':
                # If the char is a point, we count it
                point_count += 1
            # Build the number
            number += self.current_char
            self.advance()
        if point_count == 0:
            return Token(TokenType.INT, number)
        else:
            return Token(TokenType.FLOAT, number)

    def advance(self):
        """Advance the index, col and line of the TextContainer."""
        self.current_char = self.text.advance()
