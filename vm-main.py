from antlr4 import FileStream
from opcode import Opcode
from cpu import Cpu
import TestLanguage

if __name__ == "__main__":

    # Load sourcecode and compile to bytecodes.
    sourcecode = FileStream("example-source.txt")
    bytecodes = TestLanguage.compile_code(sourcecode)

    # Instantiate a CPU.
    cpu = Cpu(bytecodes,
              512,  # Mem size
              128,  # Code start address
              0,    # Stack start address
              384)  # Data start address

    # Display start memory.
    cpu.print_disassembly()
    #cpu.print_mem()
    #cpu.print_registers()

    # Execute program.
    cpu.execute_program()

    # Display resulting memory.
    cpu.print_mem()
    cpu.print_registers()


