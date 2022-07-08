"""Classes for handling files."""
from dataclasses import dataclass


@dataclass(frozen=True)
class FileInfo:
    """Class for carry information about a file."""

    name: str
    path: str


class TextContainer:
    """Handle the text, position, data, and file information."""

    def __init__(self, text: str, file: FileInfo):
        """Initialize the TextContainer.

        Args:
            text (str): Text of the input file.
            file (FileInfo): File information.
        """
        self.text = text
        self.file_info = file
        self.index = -1
        self.col = -1
        self.line = 1

    def advance(self):
        """Advance the position of the index, column, and line."""
        # Check the eof
        if self.EOF():
            # None comunicates to the parses that the end of the file was
            # reached
            return None
        # Advance the index
        self.index += 1
        # Advance the column
        self.col += 1
        # The current char is the next before advance
        current_char = self.text[self.index]
        # If the character is a line break we sum 1 to the line
        if current_char == '\n':
            self.line += 1
            self.col = 0
        return current_char

    def copy(self):
        """Generate a copy of the TextContainer."""
        # Make a new instance of self
        a = TextContainer(self.text, self.file_info)
        a.index = self.index
        a.col = self.col
        a.line = self.line
        return a

    def EOF(self):
        """Check if the sindex is at the end of the file."""
        # Check the end of the file
        if self.index >= len(self.text)-1:
            return True
        return False
