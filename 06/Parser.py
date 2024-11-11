"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing

A_COMMAND = "A_COMMAND"
L_COMMAND = "L_COMMAND"
C_COMMAND = "C_COMMAND"


class Parser:
    """Encapsulates access to the input code. Reads an assembly program
    by reading each command line-by-line, parses the current command,
    and provides convenient access to the commands components (fields
    and symbols). In addition, removes all white space and comments.
    """

    def __init__(self, input_file: typing.TextIO) -> None:
        """Opens the input file and gets ready to parse it.


        Args:
            input_file (typing.TextIO): input file.
        """
        # Your code goes here!
        # A good place to start is to read all the lines of the input:

        # with open(input_file,'r'):
        "put the file text into a list by the line "
        self.input_lines = input_file.read().splitlines()
        self.left = len(self.input_lines)
        self.cur = 0
        self.cur_command = ''

    def has_more_commands(self) -> bool:
        """Are there more commands in the input?

        Returns:
            bool: True if there are more commands, False otherwise.
        """
        # Your code goes here!
        if self.left != 0:
            return True

        return False

        pass

    def advance(self) -> None:
        """Reads the next command from the input and makes it the current command.
        Should be called only if has_more_commands() is true.
        """
        # Your code goes here!
        if not self.has_more_commands():
            pass
        else:
            self.cur_command = self.input_lines[self.cur]
            self.cur += 1
            self.left -= 1

    def check_A_command(self):
        try:
            cur_words = "".join(self.cur_command.split())
            if cur_words.startswith('@'):
                return True
            return False
        except:
            pass

    def check_L_command(self):
        try:
            if (self.cur_command.index('(') < self.cur_command.index(')')) and not self.cur_command.startswith('/'):
                return '(' in self.cur_command and ')' in self.cur_command
            return False
        except:
            pass

    def check_C_command(self):
        try:
            return (';' in self.cur_command or '=' in self.cur_command) and not self.cur_command.startswith('/')
        except:
            pass

    def command_type(self) -> str:
        """
        Returns:
            str: the type of the current command:
            "A_COMMAND" for @Xxx where Xxx is either a symbol or a decimal number
            "C_COMMAND" for dest=comp;jump
            "L_COMMAND" (actually, pseudo-command) for (Xxx) where Xxx is a symbol
        """
        # Your code goes here!

        if self.check_C_command():
            return C_COMMAND

        elif self.check_L_command():
            return L_COMMAND

        elif self.check_A_command():
            return A_COMMAND

    def symbol(self) -> str:
        """
        Returns:
            str: the symbol or decimal Xxx of the current command @Xxx or
            (Xxx). Should be called only when command_type() is "A_COMMAND" or
            "L_COMMAND".
        """
        # Your code goes here!
        if self.command_type() == A_COMMAND:
            cur_words = "".join(self.cur_command.split())
            try:
                index = cur_words.index('/')
                return cur_words[1:index]
            except:
                return cur_words[1:]

        elif self.command_type() == L_COMMAND:
            return self.cur_command[self.cur_command.index('(') + 1:self.cur_command.index(')')]

    def dest(self) -> str:
        """
        Returns:
            str: the dest mnemonic in the current C-command. Should be called
            only when commandType() is "C_COMMAND".
        """

        if self.command_type() == C_COMMAND:
            cur_words = "".join(self.cur_command.split())
            if '=' not in cur_words:
                return ''
            else:
                return cur_words.split('=')[0]

    def comp(self) -> str:
        """
        Returns:
            str: the comp mnemonic in the current C-command. Should be called
            only when commandType() is "C_COMMAND".
        """
        if self.command_type() == C_COMMAND:
            equal_cur = 0
            jump_cur = -1
            cur_words = "".join(self.cur_command.split())
            if '=' in cur_words:
                equal_cur = cur_words.index('=') + 1
            if ';' in cur_words:
                jump_cur = cur_words.index(';')
            if jump_cur == -1:
                try:
                    jump_cur = cur_words.index('//')
                    return cur_words[equal_cur:jump_cur]
                except:
                    return cur_words[equal_cur:]
            return cur_words[equal_cur:jump_cur]

    def jump(self) -> str:
        """
        Returns:
            str: the jump mnemonic in the current C-command. Should be called
            only when commandType() is "C_COMMAND".
        """
        if self.command_type() == C_COMMAND:
            cur_words = "".join(self.cur_command.split())
            if ';' in cur_words:
                index1 = cur_words.index(';')
                try:
                    jump_cur = cur_words.index('//')
                    return cur_words[index1 + 1:jump_cur]
                except:
                    return cur_words[index1 + 1:]
            return ''

    def renew(self, booli: bool):
        "dont return if booli create new perser else only initialised the cur_command "
        if booli:
            self.left = len(self.input_lines)
            self.cur = 0
            self.cur_command = ''
        else:
            self.cur_command = ''
