from antlr4 import *
from TinyLanguageLexer import TinyLanguageLexer
from TinyLanguageParser import TinyLanguageParser
from TinyLanguageCustomListener import TinyLanguageCustomListener
from antlr4.error import ErrorListener
from antlr4 import InputStream


class TinyLanguageCustomErrorListener(ErrorListener.ErrorListener):

    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        # Custom error listener.
        raise Exception("{0} at line {1}".format(msg, line))


def compile_code(sourcecode):
    # Create a stream for the sourcecode (ANTLR4).
    sourcecode_stream = InputStream.InputStream(sourcecode)

    # Create lexer and parser.
    lexer = TinyLanguageLexer(sourcecode_stream)
    stream = CommonTokenStream(lexer)
    parser = TinyLanguageParser(stream)

    # Add custom error listener.
    parser.addErrorListener(TinyLanguageCustomErrorListener())

    # Walk the tree.
    tree = parser.script()
    my_listener = TinyLanguageCustomListener()
    walker = ParseTreeWalker()
    walker.walk(my_listener, tree)

    # Return the compiled bytecodes.
    return my_listener.bytecodes

