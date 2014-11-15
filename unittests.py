import unittest
from TinyLanguage import TinyLanguage
from antlr4 import InputStream
from cpu import Cpu


class TestCpu(unittest.TestCase):

    # Simple sanity check integration test.
    def test_execute_program(self):

        # Compile program and check that bytecodes were produced.
        sourcecode = InputStream.InputStream("script { a = 10; b = 2; if (a * b == 20) { output(40 / b); } }")
        bytecodes = TinyLanguage.compile_code(sourcecode)
        self.assertTrue(len(bytecodes) > 5)

        # Execute program and check that the result is 20. TODO: FIX!
        try:
            cpu = Cpu(bytecodes, 512, 128, 0, 384)
            output = ""
            while True:
                output += cpu.execute_step()
        except:
            pass

        # The only output should be 20\r\n.
        self.assertTrue(output == "20\r\n")

