"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing


C_PUSH = 'C_PUSH'
C_POP = 'C_POP'
LINE = '\n'


class CodeWriter:
    remember =[0]
    """Translates VM commands into Hack assembly code."""

    def __init__(self, output_stream: typing.TextIO) -> None:
        """Initializes the CodeWriter.

        Args:
            output_stream (typing.TextIO): output stream.
        """
        # Your code goes here!
        # Note that you can write to output_stream like so:
        # output_stream.write("Hello world! \n")
        self.output_file = output_stream
        self.file_name = ''
        self.index = self.remember[0]

        pass

    def set_file_name(self, filename: str) -> None:
        """Informs the code writer that the translation of a new VM file is
        started.

        Args:
            filename (str): The name of the VM file.
        """
        self.file_name = filename

        pass

    def write_add_sub_or_and(self, command: str) -> None:
        self.output_file.write('@SP' + LINE + 'AM=M-1' + LINE)
        self.output_file.write('@SP' + LINE + 'A=M' + LINE + 'D=M' + LINE)

        self.output_file.write('D=M' + LINE)
        self.output_file.write('@SP' + LINE + 'AM=M-1' + LINE)
        cur = ''
        if command == "add":
            cur = "+"
        elif command == "sub":
            cur = "-"
        elif command == "and":
            cur = '&'
        elif command == "or":
            cur = "|"
        self.output_file.write('M=M{}D'.format(cur) + LINE)
        self.output_file.write('@SP' + LINE + 'M=M+1' + LINE)

    def write_not_neg(self, command: str) -> None:
        self.output_file.write('@SP' + LINE + 'AM=M-1' + LINE)
        cur = ''
        if command == "not":
            cur = "!"
        elif command == "neg":
            cur = "-"
        self.output_file.write('M={}M'.format(cur) + LINE)
        self.output_file.write('@SP' + LINE + 'M=M+1' + LINE)


    def if_case_2_3(self, index: str) -> None:
        # self.output_file.write('D=' + index + LINE)
        self.output_file.write('@SP' + LINE + 'D=M' + LINE)
        self.output_file.write('@R13' + LINE + 'M=' + index + LINE)
        self.output_file.write('@FINISH_LEVEL1_{}'.format(self.index) + LINE + '0;JMP' + LINE)

    def write_gt_lt_eq(self, command: str) -> None:
        self.output_file.write('@SP' + LINE + 'AM=M-1' + LINE + 'D=M' + LINE)
        self.output_file.write('@R14' + LINE + 'M=D' + LINE)
        self.output_file.write('@R13' + LINE + 'M=D' + LINE)
        self.output_file.write('@R13' + LINE + 'D=M' + LINE)
        self.output_file.write('@CASE1_{}'.format(self.index) + LINE + 'D;JLT' + LINE)
        self.output_file.write('@SP' + LINE + 'D=M' + LINE)

        self.output_file.write('@SP' + LINE + 'AM=M-1' + LINE + 'D=M' + LINE)
        self.output_file.write('@R13' + LINE + 'M=D' + LINE)

        self.output_file.write('@CASE2_{}'.format(self.index) + LINE + 'D;JLT' + LINE)

        self.output_file.write('@R14' + LINE + 'D=D-M' + LINE)
        self.output_file.write('@R13' + LINE + 'M=D' + LINE)
        self.output_file.write('@SP' + LINE + 'D=M' + LINE)
        self.output_file.write('@FINISH_LEVEL1_{}'.format(self.index) + LINE + '0;JMP' + LINE)

        self.output_file.write('(CASE1_{})'.format(self.index) + LINE)
        self.output_file.write('@SP' + LINE + 'D=M' + LINE)
        self.output_file.write('@SP' + LINE + 'AM=M-1' + LINE + 'D=M' + LINE)
        self.output_file.write('@CASE3_{}'.format(self.index) + LINE + 'D;JGT' + LINE)
        self.output_file.write('@R14' + LINE + 'D=D-M' + LINE)
        self.output_file.write('@R13' + LINE + 'M=D' + LINE)
        self.output_file.write('@SP' + LINE + 'D=M' + LINE)
        self.output_file.write('@FINISH_LEVEL1_{}'.format(self.index) + LINE + '0;JMP' + LINE)

        self.output_file.write('(CASE2_{})'.format(self.index) + LINE)
        self.if_case_2_3('-1')

        self.output_file.write('(CASE3_{})'.format(self.index) + LINE)
        self.if_case_2_3('1')
        cur = ''
        cur_at = ''
        if command == "eq":
            cur = 'EQ'
            cur_at = 'EQUAL' + str(self.index)
        if command == "gt":
            cur = 'GT'
            cur_at = 'X_BIGGER_Y' + str(self.index)
        if command == "lt":
            cur = 'LT'
            cur_at = 'Y_BIGGER_X' + str(self.index)
        self.output_file.write('(FINISH_LEVEL1_{})'.format(self.index) + LINE)
        self.output_file.write('@R13' + LINE + 'D=M' + LINE)
        self.output_file.write('@{}'.format(cur_at) + LINE + 'D;J{}'.format(cur) + LINE)
        self.output_file.write('@SP' + LINE + 'A=M' + LINE + 'M=0' + LINE)
        self.output_file.write('@END{}'.format(self.index) + LINE + '0;JMP' + LINE)
        self.output_file.write('({})'.format(cur_at) + LINE)
        self.output_file.write('@SP' + LINE + 'A=M' + LINE + 'M=-1' + LINE)
        self.output_file.write('(END{})'.format(self.index) + LINE + '@SP' + LINE + 'M=M+1' + LINE)
        self.output_file.write('@R14' + LINE + 'M=0' + LINE)
        self.output_file.write('@R13' + LINE + 'M=0' + LINE)
        self.index += 1
        self.remember[0]+=1

    def write_arithmetic(self, command: str) -> None:
        """Writes assembly code that is the translation of the given
        arithmetic command. For the commands eq, lt, gt, you should correctly
        compare between all numbers our computer supports, and we define the
        value "true" to be -1, and "false" to be 0.

        Args:
            command (str): an arithmetic command.
        """
        # Your code goes here!
        if command in {"add", "sub", "or", "and"}:
            self.write_add_sub_or_and(command)
        if command in {'not', 'neg'}:
            self.write_not_neg(command)
        if command in {'eq', 'gt', 'lt'}:
            self.write_gt_lt_eq(command)
        if command == "shiftleft":
            self.output_file.write("@SP" + LINE + "A=M-1" + LINE + "M<<" + LINE)
        elif command == "shiftright":
            self.output_file.write("@SP" + LINE + "A=M-1" + LINE + "M>>" + LINE)

    def write_push(self, segment: str, index: int) -> None:
        cur1 = None
        if segment == 'pointer':
            if int(index) == 0:
                cur1 = 0
            elif int(index) == 1:
                cur1 = 1

        if segment == 'temp' and 0 <= int(index) <= 7:
            self.output_file.write('@R{}'.format(str(int(index) + 5)) + LINE + 'D=M' + LINE)
            self.output_file.write('@SP' + LINE + 'A=M' + LINE + 'M=D' + LINE + '@SP' + LINE + 'M=M+1' + LINE)

        if segment == 'static':
            self.output_file.write('@{}.'.format(self.file_name) + str(index) + LINE + 'D=M' + LINE)
            self.output_file.write('@SP' + LINE + 'A=M' + LINE + 'M=D' + LINE + '@SP' + LINE + 'M=M+1' + LINE)

        if segment in ['local', 'argument', 'constant', 'this', 'that'] or cur1 in {0, 1}:
            cur = ''
            new_ind = 3
            letter = 'A'
            if cur1 in {1, 0}:
                new_ind += cur1
                letter = 'M'
            else:
                new_ind = index
            self.output_file.write('@{}'.format(new_ind) + LINE + 'D={}'.format(letter) + LINE)
            if segment == 'local':
                cur = 'LCL'
            if segment == 'argument':
                cur = 'ARG'
            if segment == 'this' or cur1 == 0:
                cur = 'THIS'
            if segment == 'that' or cur1 == 1:
                cur = 'THAT'
            if cur != '' and cur1 not in {1, 0}:
                # change from A=M+D to A=M
                self.output_file.write('@{}'.format(cur) + LINE + 'A=M+D' + LINE + 'D=M' + LINE)
            # elif cur1 not  in {1, 0}:
            #     self.output_file.write('@{}'.format(cur) + LINE + 'A=M' + LINE + 'D=M' + LINE)

            self.output_file.write('@SP' + LINE + 'A=M' + LINE + 'M=D' + LINE + '@SP' + LINE + 'M=M+1' + LINE)

    def write_pop(self, segment: str, index: int) -> None:

        if segment == 'static':
            self.output_file.write('@SP' + LINE + 'AM=M-1' + LINE + 'D=M' + LINE + 'M=0' + LINE)
            self.output_file.write('@{}.'.format(self.file_name) + str(index) + LINE + 'M=D' + LINE)
        cur1 = None
        if segment == 'pointer':
            if int(index) == 0:
                cur1 = 0
            if int(index) == 1:
                cur1 = 1
        if segment in ['local', 'argument', 'this', 'that'] or cur1 in {1, 0}:
            cur = ''
            new_ind = 3
            if cur1 in {1, 0}:
                new_ind += cur1
            else:
                new_ind = index
            self.output_file.write('@{}'.format(new_ind) + LINE + 'D=A' + LINE)
            if segment == 'local':
                cur = 'LCL'
            if segment == 'argument':
                cur = 'ARG'
            if segment == 'this' or cur1 == 0:
                cur = 'THIS'
            if segment == 'that' or cur1 == 1:
                cur = 'THAT'

            if cur != '' and cur1 not in {1, 0}:
                self.output_file.write('@{}'.format(cur) + LINE + 'D=M+D' + LINE)
            self.output_file.write("@R13" + LINE + 'M=D' + LINE)
            self.output_file.write("@R14" + LINE + 'M=D' + LINE)

            self.output_file.write('@SP' + LINE + 'AM=M-1' + LINE + 'D=M' + LINE + 'M=0' + LINE)
            self.output_file.write("@R14" + LINE + 'M=D' + LINE)

            self.output_file.write("@R13" + LINE + 'A=M' + LINE + 'M=D' + LINE)
            self.output_file.write("@R13" + LINE + 'M=0' + LINE)
            self.output_file.write("@R14" + LINE + 'M=0' + LINE)


        if segment == 'temp' and 0 <= int(index) <= 7:
            self.output_file.write('@SP' + LINE + 'AM=M-1' + LINE + 'D=M' + LINE + 'M=0' + LINE)
            self.output_file.write('@R{}'.format(str(int(index) + 5)) + LINE + 'M=D' + LINE)

    def write_push_pop(self, command: str, segment: str, index: int) -> None:
        """Writes assembly code that is the translation of the given
        command, where command is either C_PUSH or C_POP.

        Args:
            command (str): "C_PUSH" or "C_POP".
            segment (str): the memory segment to operate on.
            index (int): the index in the memory segment.
        """
        # Your code goes here!
        # Note: each reference to "static i" appearing in the file Xxx.vm should
        # be translated to the assembly symbol "Xxx.i". In the subsequent
        # assembly process, the Hack assembler will allocate these symbolic
        # variables to the RAM, starting at address 16.
        if command == C_PUSH:
            self.write_push(segment, index)
        elif command == C_POP:
            self.write_pop(segment, index)


