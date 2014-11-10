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
    cpu.print_disassembly()

    # Execute program.
    cpu.execute_program()

    value = cpu.out_stream.getvalue()
    print("\r\n- EXECUTION -------------\r\n{0}".format(value))
    cpu.out_stream.close()

    # Display resulting memory.
    cpu.print_mem()
    cpu.print_registers()


