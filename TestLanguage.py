from antlr4 import *
from Grammar.TestGrammarLexer import TestGrammarLexer
from Grammar.TestGrammarParser import TestGrammarParser
from Grammar.MyListener import MyListener
from antlr4 import InputStream


def compile_code(sourcecode):

    # Create a stream for the sourcecode (ANTLR4).
    sourcecode_stream = InputStream.InputStream(sourcecode)

    # Create lexer and parser.
    lexer = TestGrammarLexer(sourcecode_stream)
    stream = CommonTokenStream(lexer)
    parser = TestGrammarParser(stream)

    # Walk the tree.
    tree = parser.script()
    my_listener = MyListener()
    walker = ParseTreeWalker()
    walker.walk(my_listener, tree)

    return my_listener.bytecodes



