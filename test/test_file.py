"""Test file utils."""
from lib.file import FileInfo, TextContainer


def test_file_string_repr():
    """Test the file string representation."""
    # Test that the string representation of a file is the path
    file = FileInfo('test', 'test.mg')
    str_file = str(file)
    assert "FileInfo(name='test', path='test.mg')" == str_file

def test_file_container():
    """Test file container."""
    # Test that the text container is correctly initialized
    file_ = FileInfo('test', 'test.mg')
    text_container = TextContainer('test', file_)

    assert 'test' == text_container.text
    assert 'test.mg' == text_container.file_info.path
    assert -1 == text_container.index
    assert -1 == text_container.col
    assert 1 == text_container.line
    assert "t" == text_container.advance()
    # Test that the text container is correctly advanced
    text_container.advance()
    text_container.advance()
    text_container.advance()
    # Test EOF
    assert None is text_container.advance()
    assert text_container.eof()


def test_advance_line():
    """Test the advance method"""
    file_ = FileInfo('test', 'test.mg')
    text_container = TextContainer('a\nest', file_)
    assert 'a' == text_container.advance()
    assert "\n" == text_container.advance()

    assert text_container.line == 2


def test_text_container_copy():
    """Test file container copy method."""
    file_ = FileInfo('test', 'test.mg')
    text_container = TextContainer('test', file_)
    text_container.advance()
    text_container_copy = text_container.copy()
    assert id(text_container) != id(text_container_copy)
    assert text_container.text == text_container_copy.text
    assert text_container.file_info.path == text_container_copy.file_info.path
    assert text_container.index == text_container_copy.index
    assert text_container.col == text_container_copy.col
    assert text_container.line == text_container_copy.line
    assert text_container.eof() == text_container_copy.eof()
    assert id(text_container.file_info) == id(text_container_copy.file_info)
