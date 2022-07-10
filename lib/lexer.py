"""Generate the tokens from an input file."""

import string
from lib.file import TextContainer
from lib.token import Token
from lib.token_types import TokenType
from lib.error import (UnrecognizedTokenError,
                       InvalidFloatError)


class Lexer:
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
                number_token, errors = self.parse_number(self.text.copy())
                if errors:
                    return [], errors
                tokens.append(number_token)
            # We ignore the spaces
            elif self.current_char in " \t\n":
                self.advance()
                continue
            # If the char is a letter, it is a constraint
            elif self.current_char in string.ascii_letters:
                token = self.parse_constraint(self.text.copy)
                tokens.append(token)
            # If the char is a parenthesis, add it to the tokens

            elif self.current_char in "()":
                if self.current_char == '(':
                    tokens.append(Token(TokenType.LPAREN, "(", self.text.copy(), self.text.copy()))
                if self.current_char == ')':
                    tokens.append(Token(TokenType.RPAREN, ")", self.text.copy(), self.text.copy()))
                self.advance()

            elif self.current_char == ',':
                tokens.append(Token(TokenType.COMMA, ",", self.text.copy(), self.text.copy()))
                self.advance()

            else:
                # If the token was not recognized,
                # We let the error class handle the error
                position_initial = self.text.copy()
                token = self.parse_unrecognized_token()
                return [], UnrecognizedTokenError(token,
                                                  position_initial,
                                                  self.text.copy())

        return tokens, None

    def parse_constraint(self, starting_position):
        """Parse the constraints strings."""
        # Constraints ends with an space
        constraint = ""
        while True:
            # If the char is a space, we stop, All characters are part of a
            # constraint
            constraint += self.current_char
            self.advance()
            if self.current_char not in string.ascii_letters:
                break
        return Token(TokenType.CONSTRAINT, constraint, starting_position, self.text.copy())

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

    def parse_number(self, starting_position):
        """Parse a float or an integer token."""
        point_count = 0
        number = ""
        while self.current_char is not None\
                and (self.current_char.isdigit() or self.current_char == '.'):
            # A number with two periods is invalid
            if point_count > 1:
                # Do-While to parse entire number
                number += self.current_char
                while True:
                    if not self.current_char.isdigit() or\
                        self.current_char != ".":
                            break
                    print(self.current_char)
                    self.advance()
                # Create the error class
                error = InvalidFloatError(starting_position,
                                        self.text.copy(), number)
                return "", error
            if self.current_char == '.':
                # If the char is a point, we count it
                point_count += 1
            # Build the number
            number += self.current_char
            self.advance()

        if point_count == 0:
            return Token(TokenType.INT, number, starting_position, self.text.copy()), ""
        else:
            return Token(TokenType.FLOAT, number, starting_position, self.text.copy()), ""

    def advance(self):
        """Advance the index, col and line of the TextContainer."""
        self.current_char = self.text.advance()
