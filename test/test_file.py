from lib.file import FileInfo, TextContainer


def test_file_string_repr():
    # Test that the string representation of a file is the path
    f = FileInfo('test', 'test.mg')
    s = str(f)
    assert "FileInfo(name='test', path='test.mg')" == s


def test_file_container():
    # Test that the text container is correctly initialized
    f = FileInfo('test', 'test.mg')
    t = TextContainer('test', f)

    assert 'test' == t.text
    assert 'test.mg' == t.file_info.path
    assert -1 == t.index
    assert -1 == t.col
    assert 1 == t.line
    assert "t" == t.advance()
    # Test that the text container is correctly advanced
    t.advance()
    t.advance()
    t.advance()
    # Test EOF
    assert None is t.advance()
    assert t.EOF()


def test_advance_line():
    f = FileInfo('test', 'test.mg')
    t = TextContainer('a\nest', f)
    assert 'a' == t.advance()
    assert "\n" == t.advance()

    assert t.line == 2


def test_text_container_copy():
    f = FileInfo('test', 'test.mg')
    t = TextContainer('test', f)
    t.advance()
    t2 = t.copy()
    assert id(t) != id(t2)
    assert t.text == t2.text
    assert t.file_info.path == t2.file_info.path
    assert t.index == t2.index
    assert t.col == t2.col
    assert t.line == t2.line
    assert t.EOF() == t2.EOF()
    assert id(t.file_info) == id(t2.file_info)
