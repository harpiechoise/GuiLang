"""Module for error representation and handling."""


class Error:
    """The top class to represent errors in an input program."""

    def __init__(self, name, desc, pos1, pos2):
        """General form of an error in a input program.

        Args:
            name (str): The error name (e.g. "Syntax Error").
            desc (str): The error description \
                (e.g. "Expected '=' but found '+'").
            pos1 (TextContainer): The position (index, column, line) at the
                starting position of the error.
            pos2 (TextContainer): Ending position of the error.
        """
        self.name = name
        self.desc = desc
        self.pos1 = pos1
        self.pos2 = pos2
        # self.col = col
        # self.line = line
        # self.file = file

    def get_line(self) -> str:
        """Get the line of the error in the input program file.

        Returns:
            str: The line in the original file where the error occurred.
        """
        # Open the the file and read lines
        with open(self.pos1.file_info.path, 'r', encoding="utf8") as file_:
            lines = file_.readlines()
        # Get the specific line of the error
        return f"\n\t{lines[self.pos1.line-1]}\n"

    def make_indicator(self):
        """Make visual hint of the error position in the input program file.

        Returns:
            str: A string with a indicator, the indicator have the same length
                as the error (^^^).
        """
        # Get the length of the error
        error_lenght = abs(self.pos2.col - self.pos1.col)
        # If the error is at the start of the line, the indicator is shorter
        if error_lenght == 1 or self.pos1.col == 0:
            return " "*(self.pos1.col) + "^"*(error_lenght)
        # Genetate the indicator
        return " "*(self.pos1.col) + "^"*(error_lenght+1)

    def __str__(self):
        """Get the string representation of the error."""
        # Get the indicator
        indicator = self.make_indicator()
        # Make the string representation
        error = f"\n{self.name}: in file \"{self.pos1.file_info.path}\" "
        error += f"at line {self.pos1.line}, column {self.pos1.col}:"
        error += f"{self.get_line()}\t{indicator}\n{self.desc}"
        return error

    def __repr__(self) -> str:
        """Get the string representation of the error."""
        # Get the same string representation as __str__
        return self.__str__()


class UnrecognizedTokenError(Error):
    """Error for unrecognized tokens."""

    def __init__(self, token, pos1, pos2):
        """When a token is not recognized, this error will be shown.

        Args:
            token (str): The token that is not recognized.
            pos1 (TextContainer): line, col, index, information at starting
                position of the error.
            pos2 (_type_): line, col, index, information at ending position of
                the error.
        """
        # Initalize the error base class with the specific error name and desc
        super().__init__("UnrecognizedTokenError",
                         f"Unrecognized token: \"{token}\"", pos1, pos2)

class InvalidFloatError(Error):
    """Error for invalid float point values"""
    def __init__(self, pos1, pos2, value):
        super().__init__("Invalid Floating Point Value",
                         f"Invalid float value: \"{value}\"", pos1, pos2)

class NotANodeError(Error):
    """Error for node bad dtype"""
    def __init__(self, value, pos1, pos2):
        super().__init__("NotANodeError", f"Value {value} isn't a Node", pos1, pos2)
