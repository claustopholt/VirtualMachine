from opcode import Opcode
from cpu import Cpu

if __name__ == "__main__":

    # A simple test program that counts to 20.
    code = [Opcode.iconst.value, 10,     # Push integer 10 onto the stack.
            Opcode.iconst.value, 1,      # Push integer 1 onto the stack.
            Opcode.iadd.value,           # Pop two integers from the stack, add them and push result onto the stack.
            Opcode.iconst.value, 1,      # Push integer 1 onto the stack.
            Opcode.iadd.value,           # Pop two, add, push result.
            Opcode.iconst.value, 20,     # Push integer 20 onto the stack.
            Opcode.bne.value, 512 - 14,  # Branching: Pop one, peek one and jump program 14 bytes back if not equals.
            Opcode.ioutput.value,        # Pop one from stack and send to stdout (i.e. print result)
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


