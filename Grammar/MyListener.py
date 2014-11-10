from Grammar.TestGrammarListener import TestGrammarListener
from pprint import pprint
from opcode import Opcode

class MyListener(TestGrammarListener):

    # TODO: Variable names must be translated into mem offsets. Keep counter.
    variable_names = []
    bytecodes = []

    def enterScript(self, ctx):
        pass

    def exitScript(self, ctx):
        print(self.bytecodes)

    def exitVarAssign(self, ctx):
        name = ctx.ID().getText()
        if not name in self.variable_names:
            self.variable_names.append(name)
        offset = self.variable_names.index(name)

        self.bytecodes.append(Opcode.stfld.value)
        self.bytecodes.append(offset)

    def exitIdExpr(self, ctx):
        name = ctx.ID().getText()
        if not name in self.variable_names:
            self.variable_names.append(name)
        offset = self.variable_names.index(name)

        self.bytecodes.append(Opcode.ldfld.value)
        self.bytecodes.append(offset)

    def exitIntExpr(self, ctx):
        val = int(ctx.INT().getText())
        self.bytecodes.append(Opcode.int.value)
        self.bytecodes.append(val)

    def exitAddExpr(self, ctx):
        self.bytecodes.append(Opcode.add.value)

    def exitSubExpr(self, ctx):
        self.bytecodes.append(Opcode.sub.value)

    def exitMulExpr(self, ctx):
        self.bytecodes.append(Opcode.mul.value)

    def exitDivExpr(self, ctx):
        self.bytecodes.append(Opcode.div.value)

    def exitEqualExpr(self, ctx):
        # TODO!
        pass

    def exitNotEqualExpr(self, ctx):
        # TODO!
        pass

    def exitGtGteExpr(self, ctx):
        # TODO!
        pass

    def exitLtLteExpr(self, ctx):
        # TODO!
        pass

    def exitOutputCall(self, ctx):
        self.bytecodes.append(Opcode.output.value)

