"""Modulo para probar los errores."""
from lib.error import (UnrecognizedTokenError,
                       InvalidFloatError,
                       NotANodeError)
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

def test_float_error():
    """Test the float error module"""
    pos1 = TextContainer('test', FileInfo('1.1.2', 'test.mg'))
    pos1.advance()
    pos2 = TextContainer('test', FileInfo('1.1.2', 'test.mg'))
    pos2.advance()
    pos2.advance()
    float_error = InvalidFloatError(pos1, pos2, "1.1.2")
    print(float_error)
    error = ("\nInvalid Floating Point Value: in file \"test.mg\""+
             " at line 1, column 0:\n\ttest\n\t^\nInvalid float value: \"1.1.2\"")
    assert error == str(float_error)

def test_not_a_node_error():
    """Test the not a node error"""
    pos1 = TextContainer('test', FileInfo('1.1.2', 'test.mg'))
    pos1.advance()
    pos2 = TextContainer('test', FileInfo('1.1.2', 'test.mg'))
    pos2.advance()
    pos2.advance()
    node_error = NotANodeError("window", pos1, pos2)
    error = ("\nNotANodeError: in file \"test.mg\""+
             " at line 1, column 0:\n\ttest\n\t^\nValue window isn't a Node")
    assert str(node_error) == error
