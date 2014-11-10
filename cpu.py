import sys
import struct
from opcode import Opcode


class Cpu():

    def __init__(self, code, mem_size, program_start_address, stack_start_address, data_start_address):

        # Store mem size as well as program and stack start addresses.
        self.mem_size = mem_size
        self.program_start_address = program_start_address
        self.stack_start_address = stack_start_address
        self.data_start_address = data_start_address

        # Create a memory block to hold stack, code and data. self.mem is the "master" of all cpu operations.
        self.mem = bytearray(self.mem_size)

        # Convert code to bytes and and store in self.mem.
        # x64 is little-endinan, so 1000 decimal = 0x03e8 is stored as e803 and 10 decimal = 0a, stored as 0a00.
        program_bytes = struct.pack("{0}h".format(len(code)), *code)
        self.mem[program_start_address:program_start_address + len(program_bytes)] = program_bytes
        self.program_size = len(program_bytes)

        # Create stack pointer and program counter.
        self.sp = stack_start_address        # Stack pointer.
        self.pc = program_start_address      # Program counter.

    def execute_program(self):

        try:
            sys.stdout.write("\r\n- EXECUTE ----------------\r\n")
            while True:
                opcode_word = struct.unpack("h", str(self.mem[self.pc:self.pc + 2]))[0]
                opcode = Opcode._value2member_map_[opcode_word]
                self.pc += 2

                if opcode == Opcode.int:
                    self.mem[self.sp:self.sp + 2] = self.mem[self.pc:self.pc + 2]
                    self.pc += 2
                    self.sp += 2
                elif opcode == Opcode.add:
                    self.sp -= 2
                    pop1 = struct.unpack("h", str(self.mem[self.sp:self.sp + 2]))[0]
                    self.sp -= 2
                    pop2 = struct.unpack("h", str(self.mem[self.sp:self.sp + 2]))[0]
                    res = pop1 + pop2
                    self.mem[self.sp:self.sp + 2] = struct.pack("h", res)
                    self.sp += 2
                elif opcode == Opcode.output:
                    self.sp -= 2
                    pop1 = struct.unpack("h", str(self.mem[self.sp:self.sp + 2]))[0]
                    sys.stdout.write("{0}\r\n".format(pop1))
                elif opcode == Opcode.branch:
                    offset = struct.unpack("h", str(self.mem[self.pc:self.pc + 2]))[0]
                    self.pc += 2
                    print(offset)
                    self.pc += offset
                    if self.pc >= self.mem_size:
                        self.pc -= self.mem_size
                elif opcode == Opcode.bne:
                    self.sp -= 2
                    pop = struct.unpack("h", str(self.mem[self.sp:self.sp + 2]))[0]
                    peek = struct.unpack("h", str(self.mem[self.sp - 2:self.sp]))[0]
                    offset = struct.unpack("h", str(self.mem[self.pc:self.pc + 2]))[0]
                    self.pc += 2
                    if pop != peek:
                        self.pc += offset
                        if self.pc >= self.mem_size:
                            self.pc -= self.mem_size
                elif opcode == Opcode.halt:
                    break

                if self.pc >= self.mem_size:
                    sys.stdout.write("Program counter exceeded memory size, terminating.\r\n")
                    break

        except Exception as ex:
            sys.stdout.write("Program crash!! Message: {0}\r\n".format(ex.message))
        finally:
            sys.stdout.write("Program execution finished.\r\n")

    def print_mem(self):
        # Output memory as words (little-endian).
        sys.stdout.write("\r\n- MEMORY ----------------\r\n")

        for i in range(0, self.mem_size, 2):
            if i % 32 == 0:
                if i > 0:
                    sys.stdout.write("\r\n")
                sys.stdout.write("\033[0m{0:04x}:   \033[0m".format(i))

            color = "\033[0m"
            if self.mem[i] + self.mem[i+1] == 0:
                color = "\033[37m"
            sys.stdout.write("{0}{1:02x}{2:02x}\033[0m ".format(color, self.mem[i], self.mem[i + 1])),

        sys.stdout.write("\r\n")

    def print_disassembly(self):
        sys.stdout.write("\r\n- DISASSEMBLY ----------------\r\n")

        address = self.program_start_address
        while address < self.program_start_address + self.program_size:

            output = "{0:04x}:   ".format(address)

            # Get opcode and increment address to next word.
            opcode_word = struct.unpack("h", str(self.mem[address:address + 2]))[0]
            opcode = Opcode._value2member_map_[opcode_word]
            output += "{0:02x}{1:02x} ".format(self.mem[address], self.mem[address + 1])
            address += 2

            if opcode == Opcode.int:
                arg_word = struct.unpack("h", str(self.mem[address:address + 2]))[0]
                output += "{0:02x}{1:02x}       ICONST   {2}".format(self.mem[address],
                                                                     self.mem[address + 1],
                                                                     arg_word)
                address += 2
            elif opcode == Opcode.add:
                output += "           ADD"
            elif opcode == Opcode.sub:
                output += "           SUB"
            elif opcode == Opcode.mul:
                output += "           MUL"
            elif opcode == Opcode.div:
                output += "           DIV"
            elif opcode == Opcode.output:
                output += "           OUTPUT"
            elif opcode == Opcode.ldfld:
                arg_word = struct.unpack("h", str(self.mem[address:address + 2]))[0]
                output += "{0:02x}{1:02x}       LDFLD    {2}".format(self.mem[address],
                                                                  self.mem[address + 1],
                                                                  arg_word)
                address += 2
            elif opcode == Opcode.stfld:
                arg_word = struct.unpack("h", str(self.mem[address:address + 2]))[0]
                output += "{0:02x}{1:02x}       STFLD    {2}".format(self.mem[address],
                                                                  self.mem[address + 1],
                                                                  arg_word)
                address += 2
            elif opcode == Opcode.branch:
                arg_word = struct.unpack("h", str(self.mem[address:address + 2]))[0]
                output += "{0:02x}{1:02x}       BRANCH   {2}".format(self.mem[address],
                                                                     self.mem[address + 1],
                                                                     arg_word)
                address += 2
            elif opcode == Opcode.branchne:
                arg_word = struct.unpack("h", str(self.mem[address:address + 2]))[0]
                output += "{0:02x}{1:02x}       BRANCHNE {2}".format(self.mem[address],
                                                                     self.mem[address + 1],
                                                                     arg_word)
                address += 2
            elif opcode == Opcode.brancheq:
                arg_word = struct.unpack("h", str(self.mem[address:address + 2]))[0]
                output += "{0:02x}{1:02x}       BRANCHEQ {2}".format(self.mem[address],
                                                                     self.mem[address + 1],
                                                                     arg_word)
                address += 2
            elif opcode == Opcode.branchgt:
                arg_word = struct.unpack("h", str(self.mem[address:address + 2]))[0]
                output += "{0:02x}{1:02x}       BRANCHGT {2}".format(self.mem[address],
                                                                     self.mem[address + 1],
                                                                     arg_word)
                address += 2
            elif opcode == Opcode.branchlt:
                arg_word = struct.unpack("h", str(self.mem[address:address + 2]))[0]
                output += "{0:02x}{1:02x}       BRANCHLT {2}".format(self.mem[address],
                                                                     self.mem[address + 1],
                                                                     arg_word)
                address += 2
            elif opcode == Opcode.halt:
                output += "           HALT"

            # Output text.
            sys.stdout.write("{0}\r\n".format(output))

    def print_registers(self):
        sys.stdout.write("\r\n- REGISTERS ----------------\r\n")
        sys.stdout.write("sp: \033[91m{0:04x}\033[0m\r\n".format(self.sp))
        sys.stdout.write("pc: \033[93m{0:04x}\033[0m\r\n".format(self.pc))

