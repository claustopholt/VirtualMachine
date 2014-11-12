from antlr4 import FileStream
from cpu import Cpu
import TestLanguage

if __name__ == "__main__":

    # Load sourcecode and compile to bytecodes.
    sourcecode = FileStream("example-source.txt")
    bytecodes = TestLanguage.compile_code(sourcecode)

    # Instantiate a CPU with bytecodes, mem size, code addr, stack addr and data addr.
    cpu = Cpu(bytecodes, 512, 128, 0, 384)

    # Display start memory.
    cpu.get_disassembly()

    # Execute program.
    cpu.execute_step()

    print(cpu.out_stream.getvalue())
    #cpu.out_stream.close()

    # Display resulting memory.
    print(cpu.get_mem())
    cpu.print_registers()


