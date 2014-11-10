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
        buf.write(u"\35\177\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\3\2\3\2\3\2\6\2 \n\2\r\2\16\2!\3\2\3\2\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\5\3,\n\3\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write(u"\3\5\3\5\3\5\3\5\3\5\3\5\5\5:\n\5\3\6\3\6\3\7\3\7\3\b")
        buf.write(u"\3\b\3\t\3\t\3\t\7\tE\n\t\f\t\16\tH\13\t\3\t\3\t\3\n")
        buf.write(u"\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write(u"\f\3\f\3\f\3\f\5\f\\\n\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write(u"\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write(u"\3\f\3\f\3\f\3\f\7\fv\n\f\f\f\16\fy\13\f\3\r\3\r\3\16")
        buf.write(u"\3\16\3\16\2\3\26\17\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write(u"\2\2\u0082\2\34\3\2\2\2\4+\3\2\2\2\6-\3\2\2\2\b\62\3")
        buf.write(u"\2\2\2\n;\3\2\2\2\f=\3\2\2\2\16?\3\2\2\2\20A\3\2\2\2")
        buf.write(u"\22K\3\2\2\2\24N\3\2\2\2\26[\3\2\2\2\30z\3\2\2\2\32|")
        buf.write(u"\3\2\2\2\34\35\7\7\2\2\35\37\7\3\2\2\36 \5\4\3\2\37\36")
        buf.write(u"\3\2\2\2 !\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"#\3\2\2\2")
        buf.write(u"#$\7\f\2\2$\3\3\2\2\2%,\5\6\4\2&,\5\b\5\2\',\5\24\13")
        buf.write(u"\2()\5\26\f\2)*\7\r\2\2*,\3\2\2\2+%\3\2\2\2+&\3\2\2\2")
        buf.write(u"+\'\3\2\2\2+(\3\2\2\2,\5\3\2\2\2-.\7\17\2\2./\7\13\2")
        buf.write(u"\2/\60\5\26\f\2\60\61\7\r\2\2\61\7\3\2\2\2\62\63\7\t")
        buf.write(u"\2\2\63\64\7\b\2\2\64\65\5\n\6\2\65\66\7\4\2\2\669\5")
        buf.write(u"\f\7\2\678\7\n\2\28:\5\16\b\29\67\3\2\2\29:\3\2\2\2:")
        buf.write(u"\t\3\2\2\2;<\5\26\f\2<\13\3\2\2\2=>\5\20\t\2>\r\3\2\2")
        buf.write(u"\2?@\5\20\t\2@\17\3\2\2\2AF\7\3\2\2BE\5\4\3\2CE\5\22")
        buf.write(u"\n\2DB\3\2\2\2DC\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2")
        buf.write(u"\2GI\3\2\2\2HF\3\2\2\2IJ\7\f\2\2J\21\3\2\2\2KL\7\5\2")
        buf.write(u"\2LM\7\r\2\2M\23\3\2\2\2NO\7\6\2\2OP\7\b\2\2PQ\5\26\f")
        buf.write(u"\2QR\7\4\2\2RS\7\r\2\2S\25\3\2\2\2TU\b\f\1\2U\\\5\30")
        buf.write(u"\r\2V\\\5\32\16\2WX\7\b\2\2XY\5\26\f\2YZ\7\4\2\2Z\\\3")
        buf.write(u"\2\2\2[T\3\2\2\2[V\3\2\2\2[W\3\2\2\2\\w\3\2\2\2]^\f\r")
        buf.write(u"\2\2^_\7\22\2\2_v\5\26\f\16`a\f\f\2\2ab\7\23\2\2bv\5")
        buf.write(u"\26\f\rcd\f\13\2\2de\7\20\2\2ev\5\26\f\ffg\f\n\2\2gh")
        buf.write(u"\7\21\2\2hv\5\26\f\13ij\f\t\2\2jk\7\24\2\2kv\5\26\f\n")
        buf.write(u"lm\f\b\2\2mn\7\25\2\2nv\5\26\f\top\f\7\2\2pq\7\26\2\2")
        buf.write(u"qv\5\26\f\brs\f\6\2\2st\7\30\2\2tv\5\26\f\7u]\3\2\2\2")
        buf.write(u"u`\3\2\2\2uc\3\2\2\2uf\3\2\2\2ui\3\2\2\2ul\3\2\2\2uo")
        buf.write(u"\3\2\2\2ur\3\2\2\2vy\3\2\2\2wu\3\2\2\2wx\3\2\2\2x\27")
        buf.write(u"\3\2\2\2yw\3\2\2\2z{\7\17\2\2{\31\3\2\2\2|}\7\16\2\2")
        buf.write(u"}\33\3\2\2\2\n!+9DF[uw")
        return buf.getvalue()
		

class TestGrammarParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    EOF = Token.EOF
    T__10=1
    T__9=2
    T__8=3
    T__7=4
    T__6=5
    T__5=6
    T__4=7
    T__3=8
    T__2=9
    T__1=10
    T__0=11
    INT=12
    ID=13
    MUL=14
    DIV=15
    ADD=16
    SUB=17
    EQUALS=18
    NOTEQUALS=19
    GT=20
    GTE=21
    LT=22
    LTE=23
    INC=24
    DEC=25
    COMMENT=26
    WHITESPACE=27

    tokenNames = [ u"<INVALID>", u"'{'", u"')'", u"'break'", u"'output'", 
                   u"'script'", u"'('", u"'if'", u"'else'", u"'='", u"'}'", 
                   u"';'", u"INT", u"ID", u"'*'", u"'/'", u"'+'", u"'-'", 
                   u"'=='", u"'!='", u"'>'", u"'>='", u"'<'", u"'<='", u"'++'", 
                   u"'--'", u"COMMENT", u"WHITESPACE" ]

    RULE_script = 0
    RULE_statement = 1
    RULE_varAssign = 2
    RULE_ifStatement = 3
    RULE_ifCondition = 4
    RULE_ifTrueBlock = 5
    RULE_ifFalseBlock = 6
    RULE_ifBlock = 7
    RULE_breakWord = 8
    RULE_outputCall = 9
    RULE_expr = 10
    RULE_idExpr = 11
    RULE_intExpr = 12

    ruleNames =  [ u"script", u"statement", u"varAssign", u"ifStatement", 
                   u"ifCondition", u"ifTrueBlock", u"ifFalseBlock", u"ifBlock", 
                   u"breakWord", u"outputCall", u"expr", u"idExpr", u"intExpr" ]

    def __init__(self, input):
        super(TestGrammarParser, self).__init__(input)
        self.checkVersion("4.4")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ScriptContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TestGrammarParser.ScriptContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TestGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(TestGrammarParser.StatementContext,i)


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
            self.state = 26
            self.match(self.T__6)
            self.state = 27
            self.match(self.T__10)
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28 
                self.statement()
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__7) | (1 << self.T__5) | (1 << self.T__4) | (1 << self.INT) | (1 << self.ID))) != 0)):
                    break

            self.state = 33
            self.match(self.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TestGrammarParser.StatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def outputCall(self):
            return self.getTypedRuleContext(TestGrammarParser.OutputCallContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(TestGrammarParser.IfStatementContext,0)


        def expr(self):
            return self.getTypedRuleContext(TestGrammarParser.ExprContext,0)


        def varAssign(self):
            return self.getTypedRuleContext(TestGrammarParser.VarAssignContext,0)


        def getRuleIndex(self):
            return TestGrammarParser.RULE_statement

        def enterRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.enterStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.exitStatement(self)




    def statement(self):

        localctx = TestGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 41
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 35 
                self.varAssign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 36 
                self.ifStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 37 
                self.outputCall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 38 
                self.expr(0)
                self.state = 39
                self.match(self.T__0)
                pass


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

        def expr(self):
            return self.getTypedRuleContext(TestGrammarParser.ExprContext,0)


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
        self.enterRule(localctx, 4, self.RULE_varAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(self.ID)
            self.state = 44
            self.match(self.T__2)
            self.state = 45 
            self.expr(0)
            self.state = 46
            self.match(self.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TestGrammarParser.IfStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ifFalseBlock(self):
            return self.getTypedRuleContext(TestGrammarParser.IfFalseBlockContext,0)


        def ifCondition(self):
            return self.getTypedRuleContext(TestGrammarParser.IfConditionContext,0)


        def ifTrueBlock(self):
            return self.getTypedRuleContext(TestGrammarParser.IfTrueBlockContext,0)


        def getRuleIndex(self):
            return TestGrammarParser.RULE_ifStatement

        def enterRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.enterIfStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = TestGrammarParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(self.T__4)
            self.state = 49
            self.match(self.T__5)
            self.state = 50 
            self.ifCondition()
            self.state = 51
            self.match(self.T__9)
            self.state = 52 
            self.ifTrueBlock()
            self.state = 55
            _la = self._input.LA(1)
            if _la==TestGrammarParser.T__3:
                self.state = 53
                self.match(self.T__3)
                self.state = 54 
                self.ifFalseBlock()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfConditionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TestGrammarParser.IfConditionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(TestGrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return TestGrammarParser.RULE_ifCondition

        def enterRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.enterIfCondition(self)

        def exitRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.exitIfCondition(self)




    def ifCondition(self):

        localctx = TestGrammarParser.IfConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57 
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfTrueBlockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TestGrammarParser.IfTrueBlockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ifBlock(self):
            return self.getTypedRuleContext(TestGrammarParser.IfBlockContext,0)


        def getRuleIndex(self):
            return TestGrammarParser.RULE_ifTrueBlock

        def enterRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.enterIfTrueBlock(self)

        def exitRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.exitIfTrueBlock(self)




    def ifTrueBlock(self):

        localctx = TestGrammarParser.IfTrueBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifTrueBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59 
            self.ifBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfFalseBlockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TestGrammarParser.IfFalseBlockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ifBlock(self):
            return self.getTypedRuleContext(TestGrammarParser.IfBlockContext,0)


        def getRuleIndex(self):
            return TestGrammarParser.RULE_ifFalseBlock

        def enterRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.enterIfFalseBlock(self)

        def exitRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.exitIfFalseBlock(self)




    def ifFalseBlock(self):

        localctx = TestGrammarParser.IfFalseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifFalseBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61 
            self.ifBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfBlockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TestGrammarParser.IfBlockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def breakWord(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TestGrammarParser.BreakWordContext)
            else:
                return self.getTypedRuleContext(TestGrammarParser.BreakWordContext,i)


        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TestGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(TestGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return TestGrammarParser.RULE_ifBlock

        def enterRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.enterIfBlock(self)

        def exitRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.exitIfBlock(self)




    def ifBlock(self):

        localctx = TestGrammarParser.IfBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(self.T__10)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__8) | (1 << self.T__7) | (1 << self.T__5) | (1 << self.T__4) | (1 << self.INT) | (1 << self.ID))) != 0):
                self.state = 66
                token = self._input.LA(1)
                if token in [self.T__7, self.T__5, self.T__4, self.INT, self.ID]:
                    self.state = 64 
                    self.statement()

                elif token in [self.T__8]:
                    self.state = 65 
                    self.breakWord()

                else:
                    raise NoViableAltException(self)

                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
            self.match(self.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BreakWordContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TestGrammarParser.BreakWordContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TestGrammarParser.RULE_breakWord

        def enterRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.enterBreakWord(self)

        def exitRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.exitBreakWord(self)




    def breakWord(self):

        localctx = TestGrammarParser.BreakWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_breakWord)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(self.T__8)
            self.state = 74
            self.match(self.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OutputCallContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TestGrammarParser.OutputCallContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(TestGrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return TestGrammarParser.RULE_outputCall

        def enterRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.enterOutputCall(self)

        def exitRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.exitOutputCall(self)




    def outputCall(self):

        localctx = TestGrammarParser.OutputCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_outputCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(self.T__7)
            self.state = 77
            self.match(self.T__5)
            self.state = 78 
            self.expr(0)
            self.state = 79
            self.match(self.T__9)
            self.state = 80
            self.match(self.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TestGrammarParser.ExprContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TestGrammarParser.RULE_expr

     
        def copyFrom(self, ctx):
            super(TestGrammarParser.ExprContext, self).copyFrom(ctx)


    class DivExprContext(ExprContext):

        def __init__(self, parser, ctx): # actually a TestGrammarParser.ExprContext)
            super(TestGrammarParser.DivExprContext, self).__init__(parser)
            self.copyFrom(ctx)

        def DIV(self):
            return self.getToken(TestGrammarParser.DIV, 0)
        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TestGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(TestGrammarParser.ExprContext,i)


        def enterRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.enterDivExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.exitDivExpr(self)


    class SubExprContext(ExprContext):

        def __init__(self, parser, ctx): # actually a TestGrammarParser.ExprContext)
            super(TestGrammarParser.SubExprContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TestGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(TestGrammarParser.ExprContext,i)

        def SUB(self):
            return self.getToken(TestGrammarParser.SUB, 0)

        def enterRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.enterSubExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.exitSubExpr(self)


    class MulExprContext(ExprContext):

        def __init__(self, parser, ctx): # actually a TestGrammarParser.ExprContext)
            super(TestGrammarParser.MulExprContext, self).__init__(parser)
            self.copyFrom(ctx)

        def MUL(self):
            return self.getToken(TestGrammarParser.MUL, 0)
        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TestGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(TestGrammarParser.ExprContext,i)


        def enterRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.enterMulExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.exitMulExpr(self)


    class IdExprWrapperContext(ExprContext):

        def __init__(self, parser, ctx): # actually a TestGrammarParser.ExprContext)
            super(TestGrammarParser.IdExprWrapperContext, self).__init__(parser)
            self.copyFrom(ctx)

        def idExpr(self):
            return self.getTypedRuleContext(TestGrammarParser.IdExprContext,0)


        def enterRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.enterIdExprWrapper(self)

        def exitRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.exitIdExprWrapper(self)


    class GtExprContext(ExprContext):

        def __init__(self, parser, ctx): # actually a TestGrammarParser.ExprContext)
            super(TestGrammarParser.GtExprContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TestGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(TestGrammarParser.ExprContext,i)

        def GT(self):
            return self.getToken(TestGrammarParser.GT, 0)

        def enterRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.enterGtExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.exitGtExpr(self)


    class AddExprContext(ExprContext):

        def __init__(self, parser, ctx): # actually a TestGrammarParser.ExprContext)
            super(TestGrammarParser.AddExprContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TestGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(TestGrammarParser.ExprContext,i)

        def ADD(self):
            return self.getToken(TestGrammarParser.ADD, 0)

        def enterRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.enterAddExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.exitAddExpr(self)


    class EqualExprContext(ExprContext):

        def __init__(self, parser, ctx): # actually a TestGrammarParser.ExprContext)
            super(TestGrammarParser.EqualExprContext, self).__init__(parser)
            self.copyFrom(ctx)

        def EQUALS(self):
            return self.getToken(TestGrammarParser.EQUALS, 0)
        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TestGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(TestGrammarParser.ExprContext,i)


        def enterRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.enterEqualExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.exitEqualExpr(self)


    class ParensExprContext(ExprContext):

        def __init__(self, parser, ctx): # actually a TestGrammarParser.ExprContext)
            super(TestGrammarParser.ParensExprContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TestGrammarParser.ExprContext,0)


        def enterRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.enterParensExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.exitParensExpr(self)


    class LtExprContext(ExprContext):

        def __init__(self, parser, ctx): # actually a TestGrammarParser.ExprContext)
            super(TestGrammarParser.LtExprContext, self).__init__(parser)
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(TestGrammarParser.LT, 0)
        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TestGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(TestGrammarParser.ExprContext,i)


        def enterRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.enterLtExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.exitLtExpr(self)


    class IntExprWrapperContext(ExprContext):

        def __init__(self, parser, ctx): # actually a TestGrammarParser.ExprContext)
            super(TestGrammarParser.IntExprWrapperContext, self).__init__(parser)
            self.copyFrom(ctx)

        def intExpr(self):
            return self.getTypedRuleContext(TestGrammarParser.IntExprContext,0)


        def enterRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.enterIntExprWrapper(self)

        def exitRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.exitIntExprWrapper(self)


    class NotEqualExprContext(ExprContext):

        def __init__(self, parser, ctx): # actually a TestGrammarParser.ExprContext)
            super(TestGrammarParser.NotEqualExprContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TestGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(TestGrammarParser.ExprContext,i)

        def NOTEQUALS(self):
            return self.getToken(TestGrammarParser.NOTEQUALS, 0)

        def enterRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.enterNotEqualExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.exitNotEqualExpr(self)



    def expr(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TestGrammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            token = self._input.LA(1)
            if token in [self.ID]:
                localctx = TestGrammarParser.IdExprWrapperContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 83 
                self.idExpr()

            elif token in [self.INT]:
                localctx = TestGrammarParser.IntExprWrapperContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 84 
                self.intExpr()

            elif token in [self.T__5]:
                localctx = TestGrammarParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 85
                self.match(self.T__5)
                self.state = 86 
                self.expr(0)
                self.state = 87
                self.match(self.T__9)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 117
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 115
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = TestGrammarParser.AddExprContext(self, TestGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 91
                        if not self.precpred(self._ctx, 11):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 92
                        self.match(self.ADD)
                        self.state = 93 
                        self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = TestGrammarParser.SubExprContext(self, TestGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 94
                        if not self.precpred(self._ctx, 10):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 95
                        self.match(self.SUB)
                        self.state = 96 
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = TestGrammarParser.MulExprContext(self, TestGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 97
                        if not self.precpred(self._ctx, 9):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 98
                        self.match(self.MUL)
                        self.state = 99 
                        self.expr(10)
                        pass

                    elif la_ == 4:
                        localctx = TestGrammarParser.DivExprContext(self, TestGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 100
                        if not self.precpred(self._ctx, 8):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 101
                        self.match(self.DIV)
                        self.state = 102 
                        self.expr(9)
                        pass

                    elif la_ == 5:
                        localctx = TestGrammarParser.EqualExprContext(self, TestGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 103
                        if not self.precpred(self._ctx, 7):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 104
                        self.match(self.EQUALS)
                        self.state = 105 
                        self.expr(8)
                        pass

                    elif la_ == 6:
                        localctx = TestGrammarParser.NotEqualExprContext(self, TestGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 106
                        if not self.precpred(self._ctx, 6):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 107
                        self.match(self.NOTEQUALS)
                        self.state = 108 
                        self.expr(7)
                        pass

                    elif la_ == 7:
                        localctx = TestGrammarParser.GtExprContext(self, TestGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 109
                        if not self.precpred(self._ctx, 5):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 110
                        self.match(self.GT)
                        self.state = 111 
                        self.expr(6)
                        pass

                    elif la_ == 8:
                        localctx = TestGrammarParser.LtExprContext(self, TestGrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 112
                        if not self.precpred(self._ctx, 4):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 113
                        self.match(self.LT)
                        self.state = 114 
                        self.expr(5)
                        pass

             
                self.state = 119
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class IdExprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TestGrammarParser.IdExprContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TestGrammarParser.ID, 0)

        def getRuleIndex(self):
            return TestGrammarParser.RULE_idExpr

        def enterRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.enterIdExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.exitIdExpr(self)




    def idExpr(self):

        localctx = TestGrammarParser.IdExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_idExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(self.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IntExprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TestGrammarParser.IntExprContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TestGrammarParser.INT, 0)

        def getRuleIndex(self):
            return TestGrammarParser.RULE_intExpr

        def enterRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.enterIntExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, TestGrammarListener ):
                listener.exitIntExpr(self)




    def intExpr(self):

        localctx = TestGrammarParser.IntExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_intExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(self.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 4)
         



