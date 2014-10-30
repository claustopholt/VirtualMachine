from antlr4 import FileStream
from opcode import Opcode
from cpu import Cpu
import TestLanguage

if __name__ == "__main__":

    # Load sourcecode from text file and compile.
    sourcecode = FileStream("example-source.txt")
    bytecodes = TestLanguage.compile(sourcecode)

    # A simple test program that counts to 20.
    code = [Opcode.int.value, 10,     # Push integer 10 onto the stack.
            Opcode.int.value, 1,      # Push integer 1 onto the stack.
            Opcode.add.value,           # Pop two integers from the stack, add them and push result onto the stack.
            Opcode.int.value, 1,      # Push integer 1 onto the stack.
            Opcode.add.value,           # Pop two, add, push result.
            Opcode.int.value, 20,     # Push integer 20 onto the stack.
            Opcode.bne.value, 512 - 14,  # Branching: Pop one, peek one and jump program 14 bytes back if not equals.
            Opcode.output.value,        # Pop one from stack and send to stdout (i.e. print result)
            Opcode.halt.value]           # End program.

    # Instantiate a CPU.
    cpu = Cpu(code,
              512,  # Mem size
              128,  # Code start address
              0,    # Stack start address
              256)  # Data start address

    # Display start memory.
    cpu.print_disassembly()
    cpu.print_mem()
    cpu.print_registers()

    # Execute program.
    cpu.execute_program()

    # Display resulting memory.
    cpu.print_mem()
    cpu.print_registers()


