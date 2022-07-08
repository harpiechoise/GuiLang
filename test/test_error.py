from lib.error import UnrecognizedTokenError
from lib.file import TextContainer, FileInfo


def test_error_string():
    t = TextContainer('test', FileInfo('test', 'test.mg'))
    p1 = t.copy()
    t.advance()
    p2 = t.copy()
    e = UnrecognizedTokenError('test', p1, p2)
    assert ("\nUnrecognizedTokenError: in file \"test.mg\""
            " at line 1, column -1:\n\ttest\n\t^"
            "\nUnrecognized token: \"test\"") == str(e)
    assert e.make_indicator() == "^"
    assert ("\nUnrecognizedTokenError: in file \"test.mg\" "
            "at line 1, column -1:\n\ttest\n\t^\nUnrecognized "
            "token: \"test\"") == repr(e)

    t = TextContainer('test', FileInfo('test', 'test.mg'))

    t.advance()
    t.advance()

    p3 = t.copy()
    t.advance()
    t.advance()
    t.advance()

    p4 = t.copy()
    e = UnrecognizedTokenError('test', p3, p4)
    assert e.make_indicator() == " ^^^"
