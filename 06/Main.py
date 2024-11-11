"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import os
import sys
import typing
from SymbolTable import SymbolTable
from Parser import Parser
from Code import Code


def decimal_to_bi_recursive(number: int, bits=16):
    if bits == 0:
        return ""
    else:
        bit = str(number % 2)
        remaining_bits = decimal_to_bi_recursive(number // 2, bits - 1)

    return remaining_bits + bit


def assemble_file(
        input_file: typing.TextIO, output_file: typing.TextIO) -> None:
    """Assembles a single file.

    Args:
        input_file (typing.TextIO): the file to assemble.
        output_file (typing.TextIO): writes all output to this file.
    """

    symbol_table = SymbolTable()

    parser = Parser(input_file)
    rom_count = 0
    code_q = Code()
    while parser.has_more_commands():
        parser.advance()
        if parser.check_A_command() or parser.check_C_command():
            rom_count += 1
        elif parser.check_L_command():
            symbol_table.add_entry(parser.symbol(), rom_count)

    "seconod pass "

    plus_16 = 16
    parser.renew(True)
    while parser.has_more_commands():

        parser.advance()
        if parser.check_A_command():
            cur_change = parser.symbol()
            "check if the correct command  already exist if so we will transform to is binary form and write to the "
            " output file ,base on the value of the exists command in the symbol table "
            """if the command cant be found in the symbol table  we will check if it already a number or need a"""
            """transformation, if so we will put on the output file the value that we kept begin by 16 and each time 
             use we will add one """
            if parser.symbol() in symbol_table.symbol_table:  # check if in the symbol table
                cur_dict = symbol_table.symbol_table
                binary_representation = decimal_to_bi_recursive(int(cur_dict[cur_change]))
                output_file.write(binary_representation + '\n')

            else:  # if not put is bineary form
                binary_representation2 = 0
                if not cur_change.isdigit():  # check if already a number if nut put the binary form of plus16
                    symbol_table.add_entry(cur_change, plus_16)
                    binary_representation2 = decimal_to_bi_recursive(int(plus_16))
                    plus_16 += 1
                if cur_change.isdigit():  # if is a digit wrute to the output file is bineary value
                    binary_representation2 = decimal_to_bi_recursive(int(cur_change))

                output_file.write(binary_representation2 + '\n')

        elif parser.check_C_command():  # if is c_command do the next step
            comp_a = code_q.comp(parser.comp())
            jump_b = code_q.jump(parser.jump())
            dest_c = code_q.dest(parser.dest())
            first = ''
            check = parser.comp()
            if check not in ["A<<", "M<<", "D<<", "M>>", "D>>", "A>>"]:
                first = first + '111'
            else:
                first = first + '101'
            output_file.write(first + comp_a + dest_c + jump_b + '\n')


if "__main__" == __name__:
    # Parses the input path and calls assemble_file on each input file.
    # This opens both the input and the output files!
    # Both are closed automatically when the code finishes running.
    # If the output file does not exist, it is created automatically in the
    # correct path, using the correct filename.
    if not len(sys.argv) == 2:
        sys.exit("Invalid usage, please use: Assembler <input path>")
    argument_path = os.path.abspath(sys.argv[1])
    if os.path.isdir(argument_path):
        files_to_assemble = [
            os.path.join(argument_path, filename)
            for filename in os.listdir(argument_path)]
    else:
        files_to_assemble = [argument_path]
    for input_path in files_to_assemble:
        filename, extension = os.path.splitext(input_path)
        if extension.lower() != ".asm":
            continue
        output_path = filename + ".hack"
        with open(input_path, 'r') as input_file, \
                open(output_path, 'w') as output_file:
            assemble_file(input_file, output_file)
