from parso import parse
from lib.parser import Parser
from lib.file import TextContainer, FileInfo
from lib.token import Token
from lib.token_types import TokenType

def test_parser():
    file = FileInfo('test', 'test.mg')
    tokens1 = [Token(TokenType.CONSTRAINT, "window"),Token(TokenType.INT, '100'), Token(TokenType.INT, '200'), Token(TokenType.FLOAT, "1.023")]
    parser = Parser(" window 100 200 1.023", file)
    
    
    tokens, errors = parser.parse()
    
    
    parser = Parser(" ! window", file)
    tokens3, errors = parser.parse()
    
    assert tokens1 == tokens
    assert tokens3 == []
    assert errors != None