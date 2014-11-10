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

    def stack_pop(self):
        self.sp -= 2
        pop_value = struct.unpack("h", str(self.mem[self.sp:self.sp + 2]))[0]
        return pop_value

    def stack_peek(self):
        peek_value = struct.unpack("h", str(self.mem[self.sp - 2:self.sp]))[0]
        return peek_value

    def stack_push(self, push_value):
        self.mem[self.sp:self.sp + 2] = struct.pack("h", push_value)
        self.sp += 2

    def code_next(self):
        code_value = struct.unpack("h", str(self.mem[self.pc:self.pc + 2]))[0]
        self.pc += 2
        return code_value

    def data_store(self, offset, value):
        addr = self.data_start_address + (offset * 2)
        self.mem[addr:addr + 2] = struct.pack("h", value)

    def data_get(self, offset):
        addr = self.data_start_address + (offset * 2)
        value = struct.unpack("h", str(self.mem[addr:addr + 2]))[0]
        return value

    def execute_program(self):

        try:
            sys.stdout.write("\r\n- EXECUTE ----------------\r\n")
            while True:
                opcode_word = struct.unpack("h", str(self.mem[self.pc:self.pc + 2]))[0]
                opcode = Opcode._value2member_map_[opcode_word]
                self.pc += 2

                if opcode == Opcode.int:
                    code_value = self.code_next()
                    self.stack_push(code_value)
                elif opcode == Opcode.add:
                    pop1_value = self.stack_pop()
                    pop2_value = self.stack_pop()
                    self.stack_push(pop1_value + pop2_value)
                elif opcode == Opcode.sub:
                    pop1_value = self.stack_pop()
                    pop2_value = self.stack_pop()
                    self.stack_push(pop2_value - pop1_value)
                elif opcode == Opcode.mul:
                    pop1_value = self.stack_pop()
                    pop2_value = self.stack_pop()
                    self.stack_push(pop1_value * pop2_value)
                elif opcode == Opcode.div:
                    pop1_value = self.stack_pop()
                    pop2_value = self.stack_pop()
                    self.stack_push(int(pop2_value / pop1_value))
                elif opcode == Opcode.output:
                    pop1_value = self.stack_pop()
                    sys.stdout.write("{0}\r\n".format(pop1_value))
                elif opcode == Opcode.branch:
                    offset = self.code_next()
                    self.pc += offset
                    if self.pc >= self.mem_size:
                        self.pc -= self.mem_size
                elif opcode == Opcode.branchne:
                    pop = self.stack_pop()
                    peek = self.stack_peek()
                    offset = self.code_next()
                    if pop != peek:
                        self.pc += offset
                        if self.pc >= self.mem_size:
                            self.pc -= self.mem_size
                elif opcode == Opcode.stfld:
                    offset = self.code_next()
                    pop_value = self.stack_pop()
                    self.data_store(offset, pop_value)
                elif opcode == Opcode.ldfld:
                    offset = self.code_next()
                    value = self.data_get(offset)
                    self.stack_push(value)

                elif opcode == Opcode.halt:
                    break

                if self.pc >= self.mem_size:
                    sys.stdout.write("Program counter exceeded memory size, terminating.\r\n")
                    break

        except Exception as ex:
            sys.stdout.write("Program crash!! Message: {0}\r\n".format(ex.message))
        finally:
            sys.stdout.write("Program finished.\r\n")

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
                output += "{0:02x}{1:02x}       BRANCH   00{2:02x}".format(self.mem[address],
                                                                     self.mem[address + 1],
                                                                     self.program_start_address + arg_word * 2)
                address += 2
            elif opcode == Opcode.branchne:
                arg_word = struct.unpack("h", str(self.mem[address:address + 2]))[0]
                output += "{0:02x}{1:02x}       BRANCHNE 00{2:02x}".format(self.mem[address],
                                                                     self.mem[address + 1],
                                                                     self.program_start_address + arg_word * 2)
                address += 2
            elif opcode == Opcode.brancheq:
                arg_word = struct.unpack("h", str(self.mem[address:address + 2]))[0]
                output += "{0:02x}{1:02x}       BRANCHEQ 00{2:02x}".format(self.mem[address],
                                                                     self.mem[address + 1],
                                                                     self.program_start_address + arg_word * 2)
                address += 2
            elif opcode == Opcode.branchgt:
                arg_word = struct.unpack("h", str(self.mem[address:address + 2]))[0]
                output += "{0:02x}{1:02x}       BRANCHGT 00{2:02x}".format(self.mem[address],
                                                                     self.mem[address + 1],
                                                                     self.program_start_address + arg_word * 2)
                address += 2
            elif opcode == Opcode.branchlt:
                arg_word = struct.unpack("h", str(self.mem[address:address + 2]))[0]
                output += "{0:02x}{1:02x}       BRANCHLT 00{2:02x}".format(self.mem[address],
                                                                     self.mem[address + 1],
                                                                     self.program_start_address + arg_word * 2)
                address += 2
            elif opcode == Opcode.halt:
                output += "           HALT"

            # Output text.
            sys.stdout.write("{0}\r\n".format(output))

    def print_registers(self):
        sys.stdout.write("\r\n- REGISTERS ----------------\r\n")
        sys.stdout.write("sp: \033[91m{0:04x}\033[0m\r\n".format(self.sp))
        sys.stdout.write("pc: \033[93m{0:04x}\033[0m\r\n".format(self.pc))

