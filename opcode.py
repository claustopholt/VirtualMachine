from enum import Enum


class Opcode(Enum):
    int = 10            # push an integer on the stack ("iconst 100")
    add = 11            # pop two integers off stack and add, push result onto stack
    sub = 12            # Pop two integers off stack and subtract, push result onto stack
    call = 20           # call function with n args ("call 10 1" calls 0x0010 with 1 arg from stack). Not implemented.
    branch = 30         # jump to memory address offset, a simple branch ("branch 0a00" will branch 10 bytes forward)
    bne = 31            # Branch if not equal
    output = 50         # pop one value from stack and send to stdout
    halt = 99           # halt program execution


