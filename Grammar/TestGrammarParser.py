# Generated from java-escape by ANTLR 4.4
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .TestGrammarListener import TestGrammarListener
else:
    from TestGrammarListener import TestGrammarListener
def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\24\24\4\2\t\2\4\3\t\3\3\2\3\2\3\2\6\2\n\n\2\r\2\16\2")
        buf.write(u"\13\3\2\3\2\3\3\3\3\3\3\3\3\3\3\2\2\4\2\4\2\2\22\2\6")
        buf.write(u"\3\2\2\2\4\17\3\2\2\2\6\7\7\4\2\2\7\t\7\3\2\2\b\n\5\4")
        buf.write(u"\3\2\t\b\3\2\2\2\n\13\3\2\2\2\13\t\3\2\2\2\13\f\3\2\2")
        buf.write(u"\2\f\r\3\2\2\2\r\16\7\6\2\2\16\3\3\2\2\2\17\20\7\b\2")
        buf.write(u"\2\20\21\7\5\2\2\21\22\7\7\2\2\22\5\3\2\2\2\3\13")
        return buf.getvalue()
		

class TestGrammarParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    EOF = Token.EOF
    T__3=1
    T__2=2
    T__1=3
    T__0=4
    INT=5
    ID=6
    MUL=7
    DIV=8
    ADD=9
    SUB=10
    GT=11
    GTE=12
    LT=13
    LTE=14
    INC=15
    DEC=16
    COMMENT=17
    WHITESPACE=18

    tokenNames = [ u"<INVALID>", u"'{'", u"'script'", u"'='", u"'}'", u"INT", 
                   u"ID", u"'*'", u"'/'", u"'+'", u"'-'", u"'>'", u"'>='", 
                   u"'<'", u"'<='", u"'++'", u"'--'", u"COMMENT", u"WHITESPACE" ]

    RULE_script = 0
    RULE_varAssign = 1

    ruleNames =  [ u"script", u"varAssign" ]

    def __init__(self, input):
        super(TestGrammarParser, self).__init__(input)
        self.checkVersion("4.4")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ScriptContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TestGrammarParser.ScriptContext, self).__init__(parent, invokingState)
            self.parser = parser

        def varAssign(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TestGrammarParser.VarAssignContext)
            else:
                return self.getTypedRuleContext(TestGrammarParser.VarAssignContext,i)


        def getRuleIndex(self):
            return TestGrammarParser.RULE_script

        def enterRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.enterScript(self)

        def exitRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.exitScript(self)




    def script(self):

        localctx = TestGrammarParser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_script)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.match(self.T__2)
            self.state = 5
            self.match(self.T__3)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6 
                self.varAssign()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==TestGrammarParser.ID):
                    break

            self.state = 11
            self.match(self.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarAssignContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TestGrammarParser.VarAssignContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TestGrammarParser.INT, 0)

        def ID(self):
            return self.getToken(TestGrammarParser.ID, 0)

        def getRuleIndex(self):
            return TestGrammarParser.RULE_varAssign

        def enterRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.enterVarAssign(self)

        def exitRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.exitVarAssign(self)




    def varAssign(self):

        localctx = TestGrammarParser.VarAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_varAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.match(self.ID)
            self.state = 14
            self.match(self.T__1)
            self.state = 15
            self.match(self.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




