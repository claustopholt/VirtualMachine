from enum import Enum


class Opcode(Enum):
    int = 9910            # push an integer on the stack ("iconst 100")
    add = 9911            # pop two integers off stack and add, push result onto stack
    sub = 9912            # Pop two integers off stack and subtract, push result onto stack
    mul = 9913            # Pop two integers off stack and multiply, push result onto stack
    div = 9914            # Pop two integers off stack and divide, push result onto stack
    branch = 9930         # jump to memory address offset, a simple branch ("branch 0a00" will branch 10 bytes forward)
    bne = 9931            # Branch if not equal
    stfld = 9940          # Pop one integer off stack and store in field with data memory offset x
    ldfld = 9941          # Load integer value from data memory offset x and push onto stack
    output = 9950         # pop one value from stack and send to stdout
    halt = 9999           # halt program execution


