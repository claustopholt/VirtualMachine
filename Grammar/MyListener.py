from Grammar.TestGrammarListener import TestGrammarListener
from pprint import pprint
from opcode import Opcode

class MyListener(TestGrammarListener):

    variable_names = []
    labels = []
    context_properties = {}
    bytecodes = []

    #region Helpers

    def helper_create_label(self):
        label = "Label{}".format(len(self.labels))
        self.labels.append(label)
        return label

    def helper_mark_label(self, label):
        # Loop through all labels and replace with current index of bytecodes (which is the offset).
        offset = len(self.bytecodes)
        for index, bytecode in enumerate(self.bytecodes):
            if str(bytecode) == label:
                self.bytecodes[index] = offset

    #endregion

    #region Script

    def enterScript(self, ctx):
        pass

    def exitScript(self, ctx):
        self.bytecodes.append(Opcode.halt.value)

        #print(self.context_properties)
        #print(self.labels)
        #print(self.bytecodes)

    #endregion

    #region Variables and expressions

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
        true_label, done_label = [self.helper_create_label() for _ in xrange(2)]
        self.bytecodes.append(Opcode.brancheq.value)
        self.bytecodes.append(true_label)

        self.bytecodes.append(Opcode.int.value)     # False
        self.bytecodes.append(0)
        self.bytecodes.append(Opcode.branch.value)
        self.bytecodes.append(done_label)

        self.helper_mark_label(true_label)          # True
        self.bytecodes.append(Opcode.int.value)
        self.bytecodes.append(1)

        self.helper_mark_label(done_label)          # Done

    def exitNotEqualExpr(self, ctx):
        true_label, done_label = [self.helper_create_label() for _ in xrange(2)]
        self.bytecodes.append(Opcode.branchne.value)
        self.bytecodes.append(true_label)

        self.bytecodes.append(Opcode.int.value)     # False
        self.bytecodes.append(0)
        self.bytecodes.append(Opcode.branch.value)
        self.bytecodes.append(done_label)

        self.helper_mark_label(true_label)          # True
        self.bytecodes.append(Opcode.int.value)
        self.bytecodes.append(1)

        self.helper_mark_label(done_label)          # Done

    def exitGtExpr(self, ctx):
        true_label, done_label = [self.helper_create_label() for _ in xrange(2)]
        self.bytecodes.append(Opcode.branchgt.value)
        self.bytecodes.append(true_label)

        self.bytecodes.append(Opcode.int.value)     # False
        self.bytecodes.append(0)
        self.bytecodes.append(Opcode.branch.value)
        self.bytecodes.append(done_label)

        self.helper_mark_label(true_label)          # True
        self.bytecodes.append(Opcode.int.value)
        self.bytecodes.append(1)

        self.helper_mark_label(done_label)          # Done

    def exitLtExpr(self, ctx):
        true_label, done_label = [self.helper_create_label() for _ in xrange(2)]
        self.bytecodes.append(Opcode.branchlt.value)
        self.bytecodes.append(true_label)

        self.bytecodes.append(Opcode.int.value)     # False
        self.bytecodes.append(0)
        self.bytecodes.append(Opcode.branch.value)
        self.bytecodes.append(done_label)

        self.helper_mark_label(true_label)          # True
        self.bytecodes.append(Opcode.int.value)
        self.bytecodes.append(1)

        self.helper_mark_label(done_label)          # Done

    #endregion

    #region If..else

    def enterIfStatement(self, ctx):
        # Create three labels (true, false, done) and store in contex properties.
        self.context_properties[ctx] = [self.helper_create_label() for _ in xrange(3)]

    def exitIfCondition(self, ctx):
        # Get true, false and done labels from context properties.
        true_label, false_label, done_label = self.context_properties[ctx.parentCtx]

        self.bytecodes.append(Opcode.int.value)
        self.bytecodes.append(1)
        self.bytecodes.append(Opcode.brancheq.value)    # True
        self.bytecodes.append(true_label)

        self.bytecodes.append(Opcode.branch.value)      # False
        self.bytecodes.append(false_label)

    def enterIfTrueBlock(self, ctx):
        # Get true, false and done labels from context properties.
        true_label, false_label, done_label = self.context_properties[ctx.parentCtx]

        self.helper_mark_label(true_label)

    def exitIfTrueBlock(self, ctx):
        # Get true, false and done labels from context properties.
        true_label, false_label, done_label = self.context_properties[ctx.parentCtx]

        self.bytecodes.append(Opcode.branch.value)
        self.bytecodes.append(done_label)

    def enterIfFalseBlock(self, ctx):
        # Get true, false and done labels from context properties.
        true_label, false_label, done_label = self.context_properties[ctx.parentCtx]

        self.helper_mark_label(false_label)

    def exitIfFalseBlock(self, ctx):
        # Get true, false and done labels from context properties.
        true_label, false_label, done_label = self.context_properties[ctx.parentCtx]

        self.bytecodes.append(Opcode.branch.value)
        self.bytecodes.append(done_label)

    def exitIfStatement(self, ctx):
        # Get true, false and done labels from context properties.
        true_label, false_label, done_label = self.context_properties[ctx]

        if not ctx.ifFalseBlock():
            self.helper_mark_label(false_label)

        self.helper_mark_label(done_label)

    #endregion

    #region While

    def enterWhileStatement(self, ctx):
        # Create three labels (begin, true, done) and store in contex properties.
        true_label, done_label = [self.helper_create_label() for _ in xrange(2)]

        # Manually create begin_label (current offset), which also marks it.
        begin_label = len(self.bytecodes)
        self.context_properties[ctx] = [begin_label, true_label, done_label]

    def exitWhileCondition(self, ctx):
        # Get true, false and done labels from context properties.
        begin_label, true_label, done_label = self.context_properties[ctx.parentCtx]

        self.bytecodes.append(Opcode.int.value)
        self.bytecodes.append(1)
        self.bytecodes.append(Opcode.brancheq.value)    # True
        self.bytecodes.append(true_label)

        self.bytecodes.append(Opcode.branch.value)      # False (meaning: Done)
        self.bytecodes.append(done_label)

    def enterWhileBlock(self, ctx):
        # Get true, false and done labels from context properties.
        begin_label, true_label, done_label = self.context_properties[ctx.parentCtx]

        self.helper_mark_label(true_label)

    def exitWhileBlock(self, ctx):
        # Get true, false and done labels from context properties.
        begin_label, true_label, done_label = self.context_properties[ctx.parentCtx]

        self.bytecodes.append(Opcode.branch.value)
        self.bytecodes.append(begin_label)

    def exitWhileStatement(self, ctx):
        # Get true, false and done labels from context properties.
        begin_label, true_label, done_label = self.context_properties[ctx]

        self.helper_mark_label(done_label)

    #endregion

    #region System calls

    def exitOutputCall(self, ctx):
        self.bytecodes.append(Opcode.output.value)
        pass

    #endregion

    pass
