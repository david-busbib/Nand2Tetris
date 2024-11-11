"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing

THE_COMMAND_AFTER = '>'

THE_COMMAND_BEFORE = '<'

LINE = 'line'
VARDEC = "classVarDec"
END_COMMENT = "end"
START_COMMENT = 'start'

from JackTokenizer import JackTokenizer

KEYWORD = "keyword"
SYMBOL = "symbol"
IDENTIFIER = "identifier"
INT_CONST = "int_const"
STRING_CONST = "string_const"


class CompilationEngine:
    """Gets input from a JackTokenizer and emits its parsed structure into an
    output stream.
    """

    def __init__(self, input_stream: "JackTokenizer", output_stream: typing.TextIO) -> None:
        """
        Creates a new compilation engine with the given input and output. The
        next routine called must be compileClass()
        :param input_stream: The input stream.
        :param output_stream: The output stream.
        """
        # Your code goes here!
        # Note that you can write to output_stream like so:
        # output_stream.write("Hello world! \n")
        # self.compile_class()
        self.binaryOp = None
        self.num_of_tab = 0
        self.tab_r = 0
        self.tab = 0
        self.indexof = 0
        self.flag = True
        self.try_to_print_the_commands = False
        self.output_file = output_stream
        self.tokenizer = input_stream

    def write_start_end_line(self, start_or_out, command, word=None):
        if start_or_out == START_COMMENT:
            self.print_Tab()
            self.output_file.write(THE_COMMAND_BEFORE + command + THE_COMMAND_AFTER + '\n')
            self.num_of_tab += 1
        if start_or_out == 'end':
            self.num_of_tab -= 1
            self.print_Tab()
            self.output_file.write(THE_COMMAND_BEFORE + '/' + command + THE_COMMAND_AFTER + '\n')
        if start_or_out == 'line':
            self.print_Tab()
            self.output_file.write('<{}> '.format(command) + str(word) +
                                   ' </{}>'.format(command) + "\n")

    def print_Tab(self):
        self.output_file.write(self.num_of_tab * '  ')

    def go_to_next_word(self, flag=None):
        if (flag):
            self.output_file.write("the command of this file")
            i = 0
            while (self.tokenizer.return_list_line()):
                try:
                    print(self.tokenizer.return_list_line()[i])
                    i += 1
                except:
                    pass
        else:
            # self.num_of_tab+=' '
            if self.tokenizer.return_list_line() == []:
                self.first_case()
            else:
                if self.token_type_next_and_next_token().lower() == IDENTIFIER:
                    self.write_start_end_line(LINE, IDENTIFIER, self.tokenizer.identifier_next())
                elif self.token_type_next_and_next_token().lower() == KEYWORD:
                    self.write_start_end_line(LINE, KEYWORD, self.tokenizer.keyword_next())
                elif self.token_type_next_and_next_token().lower() == SYMBOL:
                    self.write_start_end_line(LINE, SYMBOL, self.tokenizer.symbol_next())
                elif self.token_type_next_and_next_token().lower() == STRING_CONST:
                    self.write_start_end_line(LINE, 'stringConstant',
                                              self.tokenizer.string_val_next())
                elif self.token_type_next_and_next_token().lower() == INT_CONST:
                    self.write_start_end_line(LINE, 'integerConstant',
                                              self.tokenizer.int_val_next())
            self.tokenizer.advance()
    def first_case(self):
        if self.tokenizer.return_list_line() == []:
            self.write_start_end_line(LINE, KEYWORD,'class')

    def help_class(self, b):
        if b:
            if (self.tokenizer.return_next_token_or_call_cur_line_att() in
                    ["static", "field"]):
                self.compile_class_var_dec()
                self.help_class(b)
        if not b:
            if (self.tokenizer.return_next_token_or_call_cur_line_att() in
                    ["function", "method", "constructor"]):
                self.compile_subroutine()
                self.help_class(b)
        return

    def do_go_to_next_words(self, num):
        for _ in range(num):
            self.tab_r += 1
            self.go_to_next_word(False)  # class and name and {

    def compile_class(self) -> None:
        """Compiles a complete class."""
        # Your code goes here!
        # self.num_of_tab+=' '
        self.write_start_end_line(START_COMMENT, 'class')
        self.do_go_to_next_words(3)
        self.help_class(True)
        self.help_class(False)
        self.go_to_next_word(False)  # for }
        self.write_start_end_line('end', 'class')

    def help_class_var_dec(self):
        self.go_to_next_word()
        self.help_class_var_dec()


    def compile_class_var_dec(self) -> None:
        """Compiles a static declaration or a field declaration."""
        # Your code goes here!
        self.write_start_end_line(START_COMMENT, VARDEC)
        self.help_class_var_dec()
        self.go_to_next_word()  # for ;
        self.write_start_end_line(END_COMMENT, VARDEC)

    def help_subroutine(self):
        if self.tokenizer.return_next_token_or_call_cur_line_att() == 'var':
            self.compile_var_dec()
            self.help_subroutine()

    def compile_subroutine(self) -> None:
        """
        Compiles a complete method, function, or constructor.
        You can assume that classes with constructors have at least one field,
        you will understand why this is necessary in project 11.
        """
        # Your code goes here!
        self.write_start_end_line(START_COMMENT, "subroutineDec")
        self.do_subrotineDec_inside()
        self.write_start_end_line("end", "subroutineDec")

        pass

    def do_subrotineDec_inside(self):
        self.do_go_to_next_words(4)
        self.write_start_end_line(START_COMMENT, "parameterList")
        while self.tokenizer.return_next_token_or_call_cur_line_att() != ")":
            self.go_to_next_word()  # for evrything insde the ()
        self.write_start_end_line('end', "parameterList")
        self.go_to_next_word()
        self.do_subrotineBody()

    def do_subrotineBody(self):
        self.write_start_end_line(START_COMMENT, "subroutineBody")
        self.do_go_to_next_words(1)
        self.help_subroutine()
        self.write_start_end_line('start', 'statements')
        self.help_compile_state()
        self.write_start_end_line('end', 'statements')
        self.go_to_next_word()
        self.write_start_end_line("end", "subroutineBody")

    def compile_parameter_list(self) -> None:
        """Compiles a (possibly empty) parameter list, not including the
        enclosing "()".
        """
        # Your code goes here!
        self.write_start_end_line(START_COMMENT, "parameterList")
        self.help_compile_parameter_list()
        self.write_start_end_line('end', "parameterList")

    def help_compile_parameter_list(self):
        if self.tokenizer.return_next_token_or_call_cur_line_att() != ")":
            self.go_to_next_word()
            self.hellp_compile_expresion()

    def compile_var_dec(self) -> None:
        """Compiles a var declaration."""
        # Your code goes here!
        self.write_start_end_line(START_COMMENT, "varDec")
        self.help_compile_var_dec()
        self.go_to_next_word()
        self.write_start_end_line('end', "varDec")

        pass

    def help_compile_var_dec(self):
        if self.tokenizer.return_next_token_or_call_cur_line_att() != ";":
            self.go_to_next_word()
            self.help_compile_var_dec()

    def help_compile_state(self):
        if (self.tokenizer.return_next_token_or_call_cur_line_att()
                in ["do","let","if","return","while"]):
            if self.tokenizer.return_next_token_or_call_cur_line_att() == "do":
                self.compile_do()
            elif self.tokenizer.return_next_token_or_call_cur_line_att() == "let":
                self.compile_let()
            elif self.tokenizer.return_next_token_or_call_cur_line_att() == "if":
                self.compile_if()
            elif self.tokenizer.return_next_token_or_call_cur_line_att() == "return":
                self.compile_return()
            elif self.tokenizer.return_next_token_or_call_cur_line_att() == "while":
                self.compile_while()
            if self.tokenizer.return_next_token_or_call_cur_line_att() != "}":
                self.help_compile_state()
        if self.tokenizer.return_next_token_or_call_cur_line_att() != "}":
            self.help_compile_state()
        return

    def compile_statements(self) -> None:
        """Compiles a sequence of statements, not including the enclosing
        "{}".
        """
        # Your code goes here!
        # self._compile_advance()

        self.write_start_end_line('start', 'statements')
        self.help_compile_state()
        self.write_start_end_line('end', 'statements')

        pass

    def compile_do(self) -> None:
        """Compiles a do statement."""
        # Your code goes here!
        self.write_start_end_line(START_COMMENT, 'doStatement')
        self.do_inside_do_sentence()
        self.write_start_end_line('end', 'doStatement')

        pass

    def do_inside_do_sentence(self):
        cur = 1
        self.do_go_to_next_words(2)
        if self.tokenizer.return_next_token_or_call_cur_line_att() == '.':
            cur += 2
        self.do_go_to_next_words(cur)
        self.write_start_end_line(START_COMMENT, 'expressionList')
        cur_tour = 0
        cur_tour =self.do_while_for_compile_expresion(cur_tour)
        self.write_start_end_line('end', 'expressionList')
        self.do_go_to_next_words(2)

    def compile_let(self) -> None:
        """Compiles a let statement."""
        # Your code goes here!
        self.write_start_end_line(START_COMMENT, 'letStatement')
        self.do_inside_let()
        self.write_start_end_line('end', 'letStatement')

        pass

    def do_inside_let(self):
        self.do_go_to_next_words(2)
        if self.tokenizer.return_next_token_or_call_cur_line_att() == '=':
            self.go_to_next_word()  # for =
        elif self.tokenizer.return_next_token_or_call_cur_line_att() == '[':
            self.go_to_next_word()
            self.help_do_inside()
            self.go_to_next_word()
        self.write_start_end_line(START_COMMENT, 'expression')
        if self.flag:
            self.compile_term()
        else:
            print(self.tokenizer.return_next_token_or_call_cur_line_att())
        self.hellp_compile_expresion()
        self.write_start_end_line('end', 'expression')
        self.go_to_next_word()

    def help_do_inside(self):
        while self.tokenizer.return_next_token_or_call_cur_line_att() != '=':
            self.write_start_end_line(START_COMMENT, 'expression')
            if self.flag:
                self.compile_term()
            self.hellp_compile_expresion()
            self.write_start_end_line('end', 'expression')  # for all []
            if self.tokenizer.return_next_token_or_call_cur_line_att() == ']':
                self.go_to_next_word()
                break

    def compile_while(self) -> None:
        """Compiles a while statement."""
        # Your code goes here!
        self.write_start_end_line(START_COMMENT, 'whileStatement')
        self.do_inside_while_sentence()
        self.write_start_end_line('end', 'whileStatement')

        pass

    def do_inside_while_sentence(self):
        self.do_go_to_next_words(2)
        if self.tokenizer.return_next_token_or_call_cur_line_att() != ')':
            if self.try_to_print_the_commands:
                for _ in self.tokenizer.return_list_line():
                    print(_)
            self.write_start_end_line(START_COMMENT, 'expression')
            if self.flag:
                self.compile_term()
            self.hellp_compile_expresion()
            self.write_start_end_line('end', 'expression')
        self.do_go_to_next_words(2)
        # finish
        self.write_start_end_line('start', 'statements')
        self.help_compile_state()
        self.write_start_end_line('end', 'statements')
        self.go_to_next_word()

    def compile_return(self) -> None:
        """Compiles a return statement."""
        # Your code goes here!
        self.write_start_end_line(START_COMMENT, 'returnStatement')
        self.go_to_next_word()  # return
        if self.tokenizer.return_next_token_or_call_cur_line_att() == ';':
            self.go_to_next_word()
            self.write_start_end_line('end', 'returnStatement')
        elif  self.tokenizer.return_next_token_or_call_cur_line_att() =='.':
            try:
                # self.go_to_next_word()
                print("ilegal enter_input")
                for _ in self.tokenizer.return_list_line():
                    self.tab_r+=1
            except:
                pass
        elif self.tokenizer.return_next_token_or_call_cur_line_att() != ';':
            self.write_start_end_line(START_COMMENT, 'expression')
            if self.flag:
                self.compile_term()
            else:
                print(self.tokenizer.return_next_token_or_call_cur_line_att())
            self.hellp_compile_expresion()
            self.write_start_end_line('end', 'expression')
            self.go_to_next_word()
            self.write_start_end_line('end', 'returnStatement')

        pass

    def compile_if(self) -> None:
        """Compiles a if statement, possibly with a trailing else clause."""
        # Your code goes here!
        self.write_start_end_line(START_COMMENT, 'ifStatement')
        self.do_go_to_next_words(2)
        self.first_if()
        self.for_else_case()
        self.write_start_end_line('end', 'ifStatement')

    def for_else_case(self):
        if self.tokenizer.return_next_token_or_call_cur_line_att() == 'else':
            self.if_else()

    def first_if(self):
        if self.tokenizer.return_next_token_or_call_cur_line_att() != ')':
            self.write_start_end_line(START_COMMENT, 'expression')
            if self.flag:
                self.compile_term()
            self.hellp_compile_expresion()
            self.write_start_end_line('end', 'expression')  # for inside word
        self.do_go_to_next_words(2)
        if self.tokenizer.return_next_token_or_call_cur_line_att() != '}':
            self.help_if_for_soger_type()
        elif self.tokenizer.return_next_token_or_call_cur_line_att() == '}':
            self.if_soger()
        else :
            pass


    def if_soger(self):
        if self.tokenizer.return_next_token_or_call_cur_line_att() != '}':
            try:
                # self.go_to_next_word()
                print("ilegal enter_input")
                for _ in self.tokenizer.return_list_line():
                    self.tab_r += 1
            except:
                pass
        self.write_start_end_line('start', 'statements')
        self.help_compile_state()
        self.write_start_end_line('end', 'statements')
        self.go_to_next_word()

    def if_else(self):
        self.do_go_to_next_words(2)
        if  self.tokenizer.return_next_token_or_call_cur_line_att() =='else':
            try:
                # self.go_to_next_word()
                print("ilegal enter_input")
                for _ in self.tokenizer.return_list_line():
                    self.tab_r += 1
            except:
                pass

        self.write_start_end_line('start', 'statements')
        self.help_compile_state()
        self.write_start_end_line('end', 'statements')
        self.go_to_next_word()  # for }

    def help_if_for_soger_type(self):
        if self.tokenizer.return_next_token_or_call_cur_line_att() == '}':
            try:
                # self.go_to_next_word()
                print("ilegal enter_input")
                for _ in self.tokenizer.return_list_line():
                    self.tab_r += 1
            except:
                pass
        self.write_start_end_line('start', 'statements')
        self.help_compile_state()
        self.write_start_end_line('end', 'statements')
        self.go_to_next_word()

    def compile_expression(self) -> None:
        """Compiles an expression."""
        # Your code goes here!
        self.write_start_end_line(START_COMMENT, 'expression')
        if self.flag:
            self.compile_term()
        else:
            print(self.tokenizer.return_next_token_or_call_cur_line_att())

        self.hellp_compile_expresion()

        self.write_start_end_line('end', 'expression')

        pass

    def hellp_compile_expresion(self):
        if self.in_keys():
            self.go_to_next_word()
            if self.try_to_print_the_commands:
                print("enter compile expresion in the while  for checking the program")
            self.compile_term()
            self.hellp_compile_expresion()

    def in_keys(self):
        return (self.tokenizer.return_next_token_or_call_cur_line_att() in
                ['+', '-', '*', '/', '&', '<', '>', '|', '&', '=']
                or self.tokenizer.return_next_token_or_call_cur_line_att()
                in ["&lt;", "&gt;", "&amp;"])

    def token_type_next_and_next_token(self) -> str:
        """
        Returns:
            str: the type of the current token, can be
            "KEYWORD", "SYMBOL", "IDENTIFIER", "INT_CONST", "STRING_CONST"
        """
        # Your code goes here!
        if (self.tokenizer.return_next_token_or_call_cur_line_att() in
                ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+',
                 '-', '*', '/', '&', '|', '<', '>',
                 '=', '~']):
            return "SYMBOL"
        if self.tokenizer.return_next_token_or_call_cur_line_att() in ['class', 'constructor', 'function', 'method'
            , 'field', 'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 'false',
                                                                       'null', 'this', 'let', 'do', 'if', 'else',
                                                                       'while', 'return']:
            return "KEYWORD"

        try:
            tr = int(self.tokenizer.return_next_token_or_call_cur_line_att())
            if tr >= 0 and tr < 32767:
                return "INT_CONST"
        except:
            pass
        try:
            if (self.tokenizer.return_next_token_or_call_cur_line_att().startswith('"') and
                    self.tokenizer.return_next_token_or_call_cur_line_att().endswith('"')):
                return "STRING_CONST"
        except:
            pass

        try:
            if int(self.tokenizer.return_next_token_or_call_cur_line_att()[0]):
                pass
        except:
            return "IDENTIFIER"

    def compile_term(self) -> None:
        """Compiles a term.
        This routine is faced with a slight difficulty when
        trying to decide between some of the alternative parsing rules.
        Specifically, if the current token is an identifier, the routing must
        distinguish between a variable, an array entry, and a subroutine call.
        A single look-ahead token, which may be one of "[", "(", or "." suffices
        to distinguish between the three possibilities. Any other token is not
        part of this term and should not be advanced over.
        """
        self.write_start_end_line(START_COMMENT, 'term')
        self.do_inside_term()
        self.write_start_end_line('end', 'term')
        # Your code goes here!

    def do_inside_term(self):
        self.help_term_with_first_part()
        while self.tokenizer.return_next_token_or_call_cur_line_att() == "(":
            self.go_to_next_word()
            self.write_start_end_line(START_COMMENT, 'expression')
            if self.flag:
                self.compile_term()

            self.hellp_compile_expresion()

            self.write_start_end_line('end', 'expression') # for ( and expresion  and )
            self.go_to_next_word()

    def help_term_with_first_part(self):
        if self.token_type_next_and_next_token() in IDENTIFIER.upper():
            self.help_term()
        elif self.find_intype():
            self.go_to_next_word()
            if self.tokenizer.return_token() in ['~', '-']:
                self.compile_term()

    def find_intype(self):
        return (self.token_type_next_and_next_token() == STRING_CONST.upper()
                or self.token_type_next_and_next_token() == INT_CONST.upper()
                or self.token_type_next_and_next_token() == KEYWORD.upper()
                or self.tokenizer.return_next_token_or_call_cur_line_att()
                in ['~', '-'])

    def help_term(self):
        self.go_to_next_word()  # varname
        if self.try_to_print_the_commands:
            for _ in self.tokenizer.return_list_line():
                print(_)
        if self.tokenizer.return_next_token_or_call_cur_line_att() in ['"', ':']:
            try:
                # self.go_to_next_word()
                print("ilegal enter_input")
                for _ in self.tokenizer.return_list_line():
                    self.tab_r += 1
            except:
                pass
        if self.tokenizer.return_next_token_or_call_cur_line_att() == "[":
            self.go_to_next_word()
            self.write_start_end_line(START_COMMENT, 'expression')
            if self.flag:
                self.compile_term()
            else:
                print(self.tokenizer.return_next_token_or_call_cur_line_att())
            self.hellp_compile_expresion()
            self.write_start_end_line('end', 'expression')
            self.go_to_next_word()  # for [ and expresion and ]
        elif self.tokenizer.return_next_token_or_call_cur_line_att() == "(":
            self.go_to_next_word()
            self.write_start_end_line(START_COMMENT, 'expressionList')
            cur_tour = 0
            cur_tour = self.do_while_for_compile_expresion(cur_tour)
            self.write_start_end_line('end', 'expressionList')  # for ( and listexpresion and )
            self.go_to_next_word()
        elif self.tokenizer.return_next_token_or_call_cur_line_att() == ".":
            self.do_go_to_next_words(3)
            self.write_start_end_line(START_COMMENT, 'expressionList')
            cur_tour = 0
            cur_tour = self.do_while_for_compile_expresion(cur_tour)
            self.write_start_end_line('end', 'expressionList') # for name and .( and listexpresion and )
            self.do_go_to_next_words(1)

    def compile_expression_list(self) -> int:
        """Compiles a (possibly empty) comma-separated list of expressions."""
        # Your code goes here!
        self.write_start_end_line(START_COMMENT, 'expressionList')
        cur_tour = 0
        cur_tour = self.do_while_for_compile_expresion(cur_tour)
        try:
            if cur_tour == -1:
                self.do_helo_exprsion()
        except:
            pass
        self.write_start_end_line('end', 'expressionList')
        # return cur_tour  #check no sur
        return cur_tour

    def do_while_for_compile_expresion(self, cur_tour):
        while self.tokenizer.return_next_token_or_call_cur_line_att() != ')':
            if cur_tour:
                self.go_to_next_word()  # for ,
            self.compile_expression()
            cur_tour += 1
        return cur_tour

    def do_helo_exprsion(self):
        cur = self.tokenizer.return_next_token_or_call_cur_line_att()
        print(cur, "ilega enter no need to do nothing")
