import sys
import io
import struct
import json
import pickle
from vmopcode import VMOpcode


class SerializableObject():
    # A class used for simple serialization/deserialization because cpu can't be pickled.
    pass


class Cpu():

    def __init__(self, code, mem_size, program_start_address, stack_start_address, data_start_address):
        # Store mem size as well as program and stack start addresses.
        self.mem_size = mem_size
        self.program_start_address = program_start_address
        self.stack_start_address = stack_start_address
        self.data_start_address = data_start_address

        # Create a memory block to hold stack, code and data. This is the foundation of all cpu operations.
        self.mem = bytearray(self.mem_size)

        # Create stack pointer and program counter.
        self.sp = stack_start_address
        self.pc = program_start_address

        # Create a counter for how many instructions have been processed.
        self.counter = 0

        # Convert code to bytes and and store in self.mem.
        # We are little-endinan, so 1000 decimal = 0x03e8 is stored as e803 and 10 decimal = 0a, stored as 0a00.
        program_bytes = struct.pack("{0}h".format(len(code)), *code)
        self.mem[program_start_address:program_start_address + len(program_bytes)] = program_bytes
        self.program_size = len(program_bytes)

    def serialize_cpu(self):
        # Serialize the cpu using a temporary object that can be pickled.
        temp_obj = SerializableObject()
        temp_obj.mem_size = self.mem_size
        temp_obj.program_start_address = self.program_start_address
        temp_obj.stack_start_address = self.stack_start_address
        temp_obj.data_start_address = int(self.data_start_address)
        temp_obj.mem = bytearray(self.mem_size)
        temp_obj.mem[:] = self.mem
        temp_obj.sp = self.sp
        temp_obj.pc = self.pc
        temp_obj.counter = self.counter
        temp_obj.program_size = self.program_size
        serialized_obj = pickle.dumps(temp_obj)
        return serialized_obj

    def deserialize_cpu(self, serialized_obj):
        # Deserialize by unpickling to a temporary object and then setting self values.
        temp_obj = pickle.loads(serialized_obj)
        self.mem_size = temp_obj.mem_size
        self.program_start_address = temp_obj.program_start_address
        self.stack_start_address = temp_obj.stack_start_address
        self.data_start_address = temp_obj.data_start_address
        self.mem[:] = temp_obj.mem
        self.sp = temp_obj.sp
        self.pc = temp_obj.pc
        self.counter = temp_obj.counter
        self.program_size = temp_obj.program_size

    def stack_pop(self):
        # Pop one value from the stack.
        self.sp -= 2
        pop_value = struct.unpack("h", str(self.mem[self.sp:self.sp + 2]))[0]
        return pop_value

    def stack_peek(self):
        # Peek at the next value in the stack.
        peek_value = struct.unpack("h", str(self.mem[self.sp - 2:self.sp]))[0]
        return peek_value

    def stack_push(self, push_value):
        # Push a value onto the stack.
        self.mem[self.sp:self.sp + 2] = struct.pack("h", push_value)
        self.sp += 2

    def code_next(self):
        # Get next code value (typically an argument to an instruction).
        code_value = struct.unpack("h", str(self.mem[self.pc:self.pc + 2]))[0]
        self.pc += 2
        return code_value

    def data_set(self, offset, value):
        # Set a data memory value (a variable).
        addr = self.data_start_address + (offset * 2)
        self.mem[addr:addr + 2] = struct.pack("h", value)

    def data_get(self, offset):
        # Get a data memory value (a variable).
        addr = self.data_start_address + (offset * 2)
        value = struct.unpack("h", str(self.mem[addr:addr + 2]))[0]
        return value

    def execute_step(self):
        # Execute one instruction.
        output = ""
        try:
            # Get the next instruction to process.
            opcode_word = struct.unpack("h", str(self.mem[self.pc:self.pc + 2]))[0]
            opcode = VMOpcode._value2member_map_[opcode_word]
            self.pc += 2
            self.counter += 1

            # Process instruction based on type.
            if opcode == VMOpcode.int:
                code_value = self.code_next()
                self.stack_push(code_value)
            elif opcode == VMOpcode.add:
                pop1_value = self.stack_pop()
                pop2_value = self.stack_pop()
                self.stack_push(pop1_value + pop2_value)
            elif opcode == VMOpcode.sub:
                pop1_value = self.stack_pop()
                pop2_value = self.stack_pop()
                self.stack_push(pop2_value - pop1_value)
            elif opcode == VMOpcode.mul:
                pop1_value = self.stack_pop()
                pop2_value = self.stack_pop()
                self.stack_push(pop1_value * pop2_value)
            elif opcode == VMOpcode.div:
                pop1_value = self.stack_pop()
                pop2_value = self.stack_pop()
                self.stack_push(int(pop2_value / pop1_value))
            elif opcode == VMOpcode.output:
                pop1_value = self.stack_pop()
                output = "{0}\r\n".format(pop1_value)
            elif opcode == VMOpcode.branch:
                offset = self.code_next()
                self.pc = self.program_start_address + (offset * 2)
            elif opcode == VMOpcode.branchne:
                pop1_value = self.stack_pop()
                pop2_value = self.stack_pop()
                offset = self.code_next()
                if pop1_value != pop2_value:
                    self.pc = self.program_start_address + (offset * 2)
            elif opcode == VMOpcode.brancheq:
                pop1_value = self.stack_pop()
                pop2_value = self.stack_pop()
                offset = self.code_next()
                if pop1_value == pop2_value:
                    self.pc = self.program_start_address + (offset * 2)
            elif opcode == VMOpcode.branchgt:
                pop1_value = self.stack_pop()
                pop2_value = self.stack_pop()
                offset = self.code_next()
                if pop2_value > pop1_value:
                    self.pc = self.program_start_address + (offset * 2)
            elif opcode == VMOpcode.branchlt:
                pop1_value = self.stack_pop()
                pop2_value = self.stack_pop()
                offset = self.code_next()
                if pop2_value < pop1_value:
                    self.pc = self.program_start_address + (offset * 2)
            elif opcode == VMOpcode.stfld:
                offset = self.code_next()
                pop_value = self.stack_pop()
                self.data_set(offset, pop_value)
            elif opcode == VMOpcode.ldfld:
                offset = self.code_next()
                value = self.data_get(offset)
                self.stack_push(value)

            elif opcode == VMOpcode.halt:
                raise StopIteration("Halt!")

            if self.pc >= self.mem_size:
                raise Exception("Program counter exceeded memory size, terminating.\r\n")

        except Exception as ex:
            raise Exception("Program crash!! Message: {0}\r\n".format(ex.message))

        return output

    def get_mem(self):
        # Output memory as WORDs (little-endian).
        output = ""
        for i in range(0, self.mem_size, 2):
            if i % 32 == 0:
                if i > 0:
                    output += "\r\n"
                output += "{0:04x}:   ".format(i)

            color = ""
            if self.mem[i] + self.mem[i+1] == 0:
                color = ""
            output += "{0}{1:02x}{2:02x} ".format(color, self.mem[i], self.mem[i + 1])

        output += "\r\n"
        return output

    def get_disassembly(self):
        # Generate human-readable disassembly from memory block.
        full_output = ""
        address = self.program_start_address
        while address < self.program_start_address + self.program_size:
            output = "{0:04x}:   ".format(address)

            # Get next instruction.
            opcode_word = struct.unpack("h", str(self.mem[address:address + 2]))[0]
            opcode = VMOpcode._value2member_map_[opcode_word]
            output += "{0:02x}{1:02x} ".format(self.mem[address], self.mem[address + 1])
            address += 2

            # Output something for each instruction type.
            if opcode == VMOpcode.int:
                arg_word = struct.unpack("h", str(self.mem[address:address + 2]))[0]
                output += "{0:02x}{1:02x}       INT        {2}".format(self.mem[address],
                                                                     self.mem[address + 1],
                                                                     arg_word)
                address += 2
            elif opcode == VMOpcode.add:
                output += "           ADD"
            elif opcode == VMOpcode.sub:
                output += "           SUB"
            elif opcode == VMOpcode.mul:
                output += "           MUL"
            elif opcode == VMOpcode.div:
                output += "           DIV"
            elif opcode == VMOpcode.output:
                output += "           OUTPUT"
            elif opcode == VMOpcode.ldfld:
                arg_word = struct.unpack("h", str(self.mem[address:address + 2]))[0]
                output += "{0:02x}{1:02x}       LDFLD      {2}".format(self.mem[address],
                                                                  self.mem[address + 1],
                                                                  arg_word)
                address += 2
            elif opcode == VMOpcode.stfld:
                arg_word = struct.unpack("h", str(self.mem[address:address + 2]))[0]
                output += "{0:02x}{1:02x}       STFLD      {2}".format(self.mem[address],
                                                                  self.mem[address + 1],
                                                                  arg_word)
                address += 2
            elif opcode == VMOpcode.branch:
                arg_word = struct.unpack("h", str(self.mem[address:address + 2]))[0]
                output += "{0:02x}{1:02x}       BRANCH     {2:04x}".format(self.mem[address],
                                                                     self.mem[address + 1],
                                                                     self.program_start_address + arg_word * 2)
                address += 2
            elif opcode == VMOpcode.branchne:
                arg_word = struct.unpack("h", str(self.mem[address:address + 2]))[0]
                output += "{0:02x}{1:02x}       BRANCHNE   {2:04x}".format(self.mem[address],
                                                                     self.mem[address + 1],
                                                                     self.program_start_address + arg_word * 2)
                address += 2
            elif opcode == VMOpcode.brancheq:
                arg_word = struct.unpack("h", str(self.mem[address:address + 2]))[0]
                output += "{0:02x}{1:02x}       BRANCHEQ   {2:04x}".format(self.mem[address],
                                                                     self.mem[address + 1],
                                                                     self.program_start_address + arg_word * 2)
                address += 2
            elif opcode == VMOpcode.branchgt:
                arg_word = struct.unpack("h", str(self.mem[address:address + 2]))[0]
                output += "{0:02x}{1:02x}       BRANCHGT   {2:04x}".format(self.mem[address],
                                                                     self.mem[address + 1],
                                                                     self.program_start_address + arg_word * 2)
                address += 2
            elif opcode == VMOpcode.branchlt:
                arg_word = struct.unpack("h", str(self.mem[address:address + 2]))[0]
                output += "{0:02x}{1:02x}       BRANCHLT   {2:04x}".format(self.mem[address],
                                                                     self.mem[address + 1],
                                                                     self.program_start_address + arg_word * 2)
                address += 2
            elif opcode == VMOpcode.halt:
                output += "           HALT"

            # Add to output text.
            full_output += "{0}\r\n".format(output)

        return full_output

    def print_registers(self):
        # TODO: Return through Redis.
        sys.stdout.write("\r\n- REGISTERS ----------------\r\n")
        sys.stdout.write("sp: \033[91m{0:04x}\033[0m\r\n".format(self.sp))
        sys.stdout.write("pc: \033[93m{0:04x}\033[0m\r\n".format(self.pc))

