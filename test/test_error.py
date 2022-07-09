"""Modulo para probar los errores."""
from lib.error import UnrecognizedTokenError
from lib.file import TextContainer, FileInfo

def test_error_string():
    """Test the error module"""
    text = TextContainer('test', FileInfo('test', 'test.mg'))
    pos1 = text.copy()
    text.advance()
    pos2 = text.copy()
    error = UnrecognizedTokenError('test', pos1, pos2)
    assert ("\nUnrecognizedTokenError: in file \"test.mg\""
            " at line 1, column -1:\n\ttest\n\t^"
            "\nUnrecognized token: \"test\"") == str(error)
    assert error.make_indicator() == "^"
    assert ("\nUnrecognizedTokenError: in file \"test.mg\" "
            "at line 1, column -1:\n\ttest\n\t^\nUnrecognized "
            "token: \"test\"") == repr(error)

    text = TextContainer('test', FileInfo('test', 'test.mg'))

    text.advance()
    text.advance()

    pos3 = text.copy()
    text.advance()
    text.advance()
    text.advance()

    pos4 = text.copy()
    error = UnrecognizedTokenError('test', pos3, pos4)
    assert error.make_indicator() == " ^^^"
