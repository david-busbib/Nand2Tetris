"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing

C_ARITHMETIC = "C_ARITHMETIC"
C_PUSH = 'C_PUSH'
C_POP = 'C_POP'
C_LABAL = 'C_LABAL'
C_GOTO = 'C_GOTO'
C_IF = 'C_IF'
C_FUNCTION = 'C_FUNCTION'
C_RETURN = 'C_RETURN'
C_CALL = 'C_CALL'
C_ARM_ = ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not','shiftleft','shiftright']


class Parser:
    """
    # Parser

    Handles the parsing of a single .vm file, and encapsulates access to the
    input code. It reads VM commands, parses them, and provides convenient
    access to their components.
    In addition, it removes all white space and comments.

    ## VM Language Specification

    A .vm file is a stream of characters. If the file represents a
    valid program, it can be translated into a stream of valid assembly
    commands. VM commands may be separated by an arbitrary number of whitespace
    characters and comments, which are ignored. Comments begin with "//" and
    last until the lines end.
    The different parts of each VM command may also be separated by an arbitrary
    number of non-newline whitespace characters.

    - Arithmetic commands:
      - add, sub, and, or, eq, gt, lt
      - neg, not, shiftleft, shiftright
    - Memory segment manipulation:
      - push <segment> <number>
      - pop <segment that is not constant> <number>
      - <segment> can be any of: argument, local, static, constant, this, that,
                                 pointer, temp
    - Branching (only relevant for project 8):
      - label <label-name>
      - if-goto <label-name>
      - goto <label-name>
      - <label-name> can be any combination of non-whitespace characters.
    - Functions (only relevant for project 8):
      - call <function-name> <n-args>
      - function <function-name> <n-vars>
      - return
    """

    def __init__(self, input_file: typing.TextIO) -> None:
        """Gets ready to parse the input file.

        Args:
            input_file (typing.TextIO): input file.
        """
        # Your code goes here!

        # A good place to start is to read all the lines of the input:
        self.cur_command_line = 0
        self.cur_command = ''
        self.input_lines = input_file.read().splitlines()
        self.left = len(self.input_lines)
        pass

    def has_more_commands(self) -> bool:
        """Are there more commands in the input?

        Returns:
            bool: True if there are more commands, False otherwise.
        """
        # Your code goes here!
        if self.left == 0:
            return False
        return True
        pass

    def advance(self) -> None:
        """Reads the next command from the input and makes it the current
        command. Should be called only if has_more_commands() is true. Initially
        there is no current command.
        """
        # Your code goes here!
        if self.has_more_commands():
            self.cur_command = self.input_lines[self.cur_command_line]
            self.left -= 1
            self.cur_command_line += 1

        pass

    def del_com(self):
        """
        return the cur line command without any space or explication
        """
        if self.cur_command.startswith('//'):
            return ''
        cur_words = " ".join(self.cur_command.split())
        try:
            if cur_words.index('//'):
                return cur_words[:cur_words.index('//')-1]
            return cur_words
        except:
            return cur_words

    def check_c_arm(self, cur_line: str):
        "check if the command is c_aothemetic"
        try:
            if cur_line in C_ARM_:
                return True
            return False
        except:
            return False

    #         return C_ARITHMETIC

    def command_type(self) -> str:
        """
        Returns:
            str: the type of the current VM command.
            "C_ARITHMETIC" is returned for all arithmetic commands.
            For other commands, can return:
            "C_PUSH", "C_POP", "C_LABEL", "C_GOTO", "C_IF", "C_FUNCTION",
            "C_RETURN", "C_CALL".
        """
        # Your code goes here!
        cur_line = self.del_com()

        if cur_line:
            if self.check_c_arm(cur_line):
                return C_ARITHMETIC
            if cur_line.startswith('push'):
                return C_PUSH
            if cur_line.startswith('pop'):
                return C_POP

            if cur_line.startswith('label'):
                return C_LABAL
            if cur_line == 'return':
                return C_RETURN
            if cur_line.startswith('goto'):
                return C_GOTO
            if cur_line.startswith('function'):
                return C_FUNCTION
            if cur_line.startswith('if-'):
                return C_IF
            if cur_line.startswith('call'):
                return C_CALL



    def arg1(self) -> str:
        """
        Returns:
            str: the first argument of the current command. In case of
            "C_ARITHMETIC", the command itself (add, sub, etc.) is returned.
            Should not be called if the current command is "C_RETURN".
        """
        # Your code goes here!
        cur_line = self.del_com()

        if self.check_c_arm(cur_line):
            return cur_line
        if self.command_type() != C_RETURN:
            words = cur_line.split()
            return words[1]
        else:
            return ''

    def arg2(self) -> int:
        """
        Returns:
            int: the second argument of the current command. Should be
            called only if the current command is "C_PUSH", "C_POP",
            "C_FUNCTION" or "C_CALL".
        """
        # Your code goes here!
        if self.command_type() in [C_CALL, C_FUNCTION, C_POP, C_PUSH]:
            cur_line = self.del_com()
            words = cur_line.split()
            return int(words[2])


