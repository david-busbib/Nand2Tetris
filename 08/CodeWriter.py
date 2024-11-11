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
N = '\n'
C_ARM = 'CALL'


class CodeWriter:
    """Translates VM commands into Hack assembly code."""
    remember = [0]

    def __init__(self, output_stream: typing.TextIO) -> None:
        """Initializes the CodeWriter.

        Args:
            output_stream (typing.TextIO): output stream.
        """
        # Your code goes here!
        # Note that you can write to output_stream like so:
        # output_stream.write("Hello world! \n")
        C_PUSH = 'C_PUSH'
        C_POP = 'C_POP'
        self.output_file = output_stream
        self.file_name = ''
        self.index = self.remember[0]
        self.name = ''
        self.lab = 0
        self.cur_func = "BootStrapfirstFunc"

        pass

    def set_file_name(self, filename: str) -> None:
        self.file_name = filename

    def write_add_sub_or_and(self, command: str) -> None:
        self.output_file.write('@SP \nAM=M-1 \n'
                               ' @SP \nA=M \nD=M \n'
                               'D=M \n'
                               '@SP \nAM=M-1 \n')
        cur = ''
        if command == "add":
            cur = "+"
        elif command == "sub":
            cur = "-"
        elif command == "and":
            cur = '&'
        elif command == "or":
            cur = "|"
        self.output_file.write('M=M{}D\n'.format(cur))
        self.output_file.write('@SP \nM=M+1 \n')

    def write_not_neg(self, command: str) -> None:
        self.output_file.write('@SP \nAM=M-1 \n')
        cur = ''
        if command == "not":
            cur = "!"
        elif command == "neg":
            cur = "-"
        self.output_file.write('M={}M \n'.format(cur))
        self.output_file.write('@SP \nM=M+1 \n')

    def if_case_2_3(self, index: str) -> None:
        self.output_file.write('@SP \nD=M \n'
                               '@R13 \nM=' + index + ' \n'
                                                     '@FINISH_LEVEL1_{}'.format(self.index) +
                               ' \n' + '0;JMP \n')

    def write_gt_lt_eq(self, command: str) -> None:
        self.output_file.write('@SP \n'  'AM=M-1 \nD=M \n'
                               '@R14 \nM=D \n'
                               '@R13 \nM=D \n'
                               '@R13 \nD=M \n'
                               '@CASE1_{}'.format(self.index) + ' \n' + 'D;JLT \n'
                                                                        '@SP \nD=M \n')

        self.output_file.write(
            '@SP' + N + 'AM=M-1' + N + 'D=M' + N +
            '@R13' + N + 'M=D' + N +
            '@CASE2_{}'.format(self.index) + N + 'D;JLT' + N +
            '@R14' + N + 'D=D-M' + N +
            '@R13' + N + 'M=D' + N +
            '@SP' + N + 'D=M' + N +
            '@FINISH_LEVEL1_{}'.format(self.index) + N +
            '0;JMP' + N +
            '(CASE1_{})'.format(self.index) + N +
            '@SP' + N + 'D=M' + N +
            '@SP' + N + 'AM=M-1' + N + 'D=M' + N +
            '@CASE3_{}'.format(self.index) +
            N + 'D;JGT' + N +
            '@R14' + N + 'D=D-M' + N +
            '@R13' + N + 'M=D' + N +
            '@SP' + N + 'D=M' + N +
            '@FINISH_LEVEL1_{}'.format(self.index) + N
            + '0;JMP' + N +
            '(CASE2_{})'.format(self.index) + N)
        self.if_case_2_3('-1')
        self.output_file.write('(CASE3_{})'.format(self.index) + N)
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
        self.output_file.write('(FINISH_LEVEL1_{})'.format(self.index) + N +
                               '@R13' + N + 'D=M' + N +
                               '@{}'.format(cur_at) + N + 'D;J{}'.format(cur) +
                               N +
                               '@SP' + N + 'A=M' + N + 'M=0' +
                               N +
                               '@END{}'.format(self.index) + N + '0;JMP' +
                               N +
                               '({})'.format(cur_at) + N +
                               '@SP' + N + 'A=M' + N +
                               'M=-1' + N +
                               '(END{})'.format(self.index) + N +
                               '@SP' + N +
                               'M=M+1' + N +
                               '@R14' + N + 'M=0' + N +
                               '@R13' + N + 'M=0' + N)
        self.index += 1
        self.remember[0] += 1

    def write_arithmetic(self, command: str) -> None:
        """Writes assembly code that is the translation of the given
        arithmetic command. For the commands eq, lt, gt, you should correctly
        compare between all numbers our computer supports, and we define the
        value "true" to be -1, and "false" to be 0.

        Args:
            command (str): an arithmetic command.
        """
        # Your code goes here!
        self.output_file.write("//arithmetic command " + command + N)

        if command in {"add", "sub", "or", "and"}:
            self.write_add_sub_or_and(command)
        if command in {'not', 'neg'}:
            self.write_not_neg(command)
        if command in {'eq', 'gt', 'lt'}:
            self.write_gt_lt_eq(command)
        if command == "shiftleft":
            self.output_file.write(
                "@SP" + N + "A=M-1" + N + "M=M<<" + N)
        if command == "shiftright":
            self.output_file.write(
                "@SP" + N + "A=M-1" + N + "M=M>>" + N)

    def write_push(self, segment: str, index: int) -> None:

        cur1 = None
        if segment == 'pointer':
            if int(index) == 0:
                cur1 = 0
            elif int(index) == 1:
                cur1 = 1

        if segment == 'temp' and 0 <= int(index) <= 7:
            self.output_file.write(
                '@R{}'.format(str(int(index) + 5)) +
                N + 'D=M' + N)
            self.output_file.write(
                '@SP' + N + 'A=M' + N
                + 'M=D' + N + '@SP' + N + 'M=M+1' + N)

        if segment == 'static':
            self.output_file.write(
                '@{}.'.format(self.file_name) + str(index) + N + 'D=M' + N)
            self.output_file.write(
                '@SP' + N + 'A=M' + N + 'M=D' + N + '@SP' + N + 'M=M+1' + N)

        if segment in ['local', 'argument', 'constant', 'this', 'that'] or cur1 in {0, 1}:
            cur = ''
            new_ind = 3
            letter = 'A'
            if cur1 in {1, 0}:
                new_ind += cur1
                letter = 'M'
            else:
                new_ind = index
            self.output_file.write(
                '@{}'.format(new_ind) + N + 'D={}'.format(letter) + N)
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
                self.output_file.write('@{}'.format(
                    cur) + N + 'A=M+D' + N + 'D=M' + N)
            self.output_file.write(
                '@SP' + N + 'A=M' + N + 'M=D' + N + '@SP' + N + 'M=M+1' + N)

    def write_pop(self, segment: str, index: int) -> None:

        if segment == 'static':
            self.output_file.write(
                '@SP' + N + 'AM=M-1' + N + 'D=M' + N + 'M=0' + N)
            self.output_file.write(
                '@{}.'.format(self.file_name) + str(index) + N + 'M=D' + N)
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
            self.output_file.write('@{}'.format(new_ind) + N + 'D=A' + N)
            if segment == 'local':
                cur = 'LCL'
            if segment == 'argument':
                cur = 'ARG'
            if segment == 'this' or cur1 == 0:
                cur = 'THIS'
            if segment == 'that' or cur1 == 1:
                cur = 'THAT'

            if cur != '' and cur1 not in {1, 0}:
                self.output_file.write('@{}'.format(cur) + N + 'D=M+D' +
                                       N)
            self.output_file.write("@R13" + N + 'M=D' + N +
                                   "@R14" + N + 'M=D' + N +
                                   '@SP' + N + 'AM=M-1' + N +
                                   'D=M' + N + 'M=0' + N +
                                   "@R14" + N + 'M=D' + N +
                                   "@R13" + N + 'A=M' + N +
                                   'M=D' + N + "@R13" + N +
                                   'M=0' + N +
                                   "@R14" + N + 'M=0' + N)

        if segment == 'temp' and 0 <= int(index) <= 7:
            self.output_file.write(
                '@SP' + N + 'AM=M-1' + N + 'D=M' +
                N + 'M=0' + N)
            self.output_file.write(
                '@R{}'.format(str(int(index) + 5)) + N + 'M=D' + N)

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
            self.output_file.write("//push command " + segment + " and index " + str(index)
                                   + N)

            self.write_push(segment, index)
        elif command == C_POP:
            self.output_file.write("//pop command " + segment + "and index " + str(index)
                                   + N)

            self.write_pop(segment, index)

    def write_label(self, label: str) -> None:
        self.output_file.write("//label command " + self.cur_func + '$' + label + "\n")
        self.output_file.write('({})'.format(self.cur_func + '$' + label) + "\n")

    def initializebootstrap(self):
        self.output_file.write('@256' "\n"  'D=A'  "\n" '@SP' "\n"  'M=D'  "\n")
        self.write_call('Sys.init', 0)

    def write_goto(self, label: str) -> None:
        self.output_file.write("//goto the {}".format(self.cur_func + "$" + label) + "\n" +
                               '@{}'.format(self.cur_func + "$" + label) +
                               "\n" + '0;JMP' + "\n")

    def write_if(self, label: str) -> None:
        self.output_file.write("//if command " + self.cur_func + '$' + label + "\n")

        self.output_file.write('@SP'  "\n" 'AM=M-1'  "\n" 'D=M'  "\n"
                               '@{}'.format(self.cur_func + '$' + label) +
                               "\n"  'D;JNE'  "\n")

    def write_function(self, function_name: str, n_vars: int) -> None:
        self.cur_func = function_name
        self.lab = 0
        self.output_file.write("//func command " + self.cur_func + "\n")
        self.output_file.write("({})".format(self.cur_func) + "\n"
                                                              
                                                              )

        for _ in range(int(n_vars)):
            self.output_file.write('@SP' "\n"  'A=M'  "\n"  'M={}'.format(0) + "\n"
                            "@R13"  "\n"  "M=D" "\n"  '@SP'  "\n"  'M=M+1'  "\n")
        self.output_file.write("@R13"  "\n"  "M=0"  "\n")

    def write_call(self, function_name: str, n_args: int) -> None:
        label = "ret." + str(self.lab)
        self.output_file.write("//call command " + self.cur_func + '$' + label + "\n")

        self.output_file.write('@{}'.format(self.cur_func + "$" + label) +
                               "\n" 'D=A'  "\n"  '@SP'  "\n" 'M=M+1' "\n" 'A=M-1'  "\n"  'M=D'  "\n")

        for i in ['LCL', 'ARG', 'THIS', 'THAT']:
            self.output_file.write('@{}'.format(i) + "\n"
                                                     'D=M'  "\n"  '@SP'    "\n"  'M=M+1' 
                                                     "\n"  'A=M-1'  "\n"  'M=D' "\n")

        cur = int(n_args) + 5
        self.output_file.write('@{}'.format(cur) + "\n"  'D=A' "\n"  '@SP'   "\n"  'D=M-D' "\n"
                                                   '@ARG'  "\n"  'M=D'  "\n")

        # LCL = SP              // repositions LCL
        self.output_file.write('@SP'    "\n" 'D=M'  "\n" '@LCL'   "\n" 'M=D'  "\n")
        # goto function_name    // transfers control to the callee

        self.output_file.write("@" + function_name + "\n" + "0;JMP" + "\n")
        self.write_label(label)
        self.lab += 1
        # (return_address)      // injects the return address label into the code

    def help_return_with(self, num: int, where: str):

        # "help the return finc to work better"
        self.output_file.write('@{}'.format(num) + "\n" 'D=A'  "\n" '@R15'   "\n" 'D=M-D'
                                                   "\n" 'A=D' "\n"   'D=M' "\n"
                                                   '@{}'.format(where) + "\n" 'M=D'  "\n")

    def write_return(self) -> None:
        self.output_file.write("//return command \n")

        self.output_file.write('@LCL\n'  'D=M\n'
                               '@R15\n'  'M=D\n')  # r15 is frame
        # return_address = *(frame-5)   // puts the return address in a temp var
        self.help_return_with(5, 'R14')

        self.output_file.write('@{}'.format('SP') + "\n" 'D=A\n' '@{}'.format('ARG')
                               + "\n" 'D=M+D' "\n"
                               "@R13" "\n"  'M=D'  
                                 "\n" '@SP'  "\n" 'AM=M-1' "\n"  'D=M' "\n" "@R13" "\n" 'A=M'  "\n" 'M=D'
                                 "\n" "@R13 \nM=0 \n")
        self.output_file.write('@ARG' "\n" 'D=M' "\n"  'D=D+1'  "\n"'@SP' "\n" 'M=D' "\n")

        self.help_return_with(1, 'THAT')

        self.help_return_with(2, 'THIS')

        self.help_return_with(3, 'ARG')

        self.help_return_with(4, 'LCL')

        self.output_file.write('@{}'.format('R14') + "\n"  'A=M'  "\n"  '0;JMP'  "\n")
