import unittest
import TestLanguage
from antlr4 import InputStream
from cpu import Cpu


class TestCpu(unittest.TestCase):

    # Simple sanity check integration test.
    def test_execute_program(self):

        # Compile program and check that bytecodes were produced.
        sourcecode = InputStream.InputStream("script { a = 10; b = 2; if (a * b == 20) { output(40 / b); } }")
        bytecodes = TestLanguage.compile_code(sourcecode)
        self.assertTrue(len(bytecodes) > 5)

        # Execute program and check that the result is 20.
        cpu = Cpu(bytecodes, 512, 128, 0, 384)
        cpu.execute_step()
        data = cpu.out_stream.getvalue()
        cpu.out_stream.close()
        self.assertTrue(str(data).startswith("20"))

