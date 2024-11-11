"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing

from SymbolTable import SymbolTable
from VMWriter import VMWriter

THIS_ = {
    "var": "local",
    "static": "static",
    "pointer": "pointer",
    "argument": "argument",
    "that": "that",
    "this": "this",
    "field": "this",
    None: "this",
}

SEGMENT_LIST = {
    "var": "local",
    "static": "static",
    "pointer": "pointer",
    "argument": "argument",
    "that": "that",
    "this": "this",
    "field": "this",
}

NEXT = '\n'
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
        # self.binaryOp = None
        # self.tab_r = 0
        # self.tab = 0

        self.index = None
        self.output_file = output_stream
        self.tokenizer = input_stream
        self.vmwriter1 = VMWriter(output_stream)
        self.symbol_tab = SymbolTable()
        self.kind_of = ''
        self.name_backup = ''
        self.ty = ''
        self.count = 0
        self.name = ''
        self.class_name = ''


    def token_type_next_and_next_token(self) -> str:
        """
        Returns:
            str: the type of the current token, can be
            "KEYWORD", "SYMBOL", "IDENTIFIER", "INT_CONST", "STRING_CONST"
        """
        # Your code goes here!
        if (self.tokenizer.retrun_list_ir_next_token() in
                ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+',
                 '-', '*', '/', '&', '|', '<', '>',
                 '=', '~',"#","^"]):
            return "SYMBOL"
        if self.tokenizer.retrun_list_ir_next_token() in ['class', 'constructor', 'function', 'method'
            , 'field', 'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 'false',
                                                          'null', 'this', 'let', 'do', 'if', 'else',
                                                          'while', 'return']:
            return "KEYWORD"

        try:
            tr = int(self.tokenizer.retrun_list_ir_next_token())
            if tr >= 0 and tr < 32767:
                return "INT_CONST"
        except:
            pass
        try:
            if (self.tokenizer.retrun_list_ir_next_token().startswith('"') and
                    self.tokenizer.retrun_list_ir_next_token().endswith('"')):
                return "STRING_CONST"
        except:
            pass

        try:
            if int(self.tokenizer.retrun_list_ir_next_token()[0]):
                pass
        except:
            return "IDENTIFIER"

    def help_class(self, b):
        if b:
            if self.tokenizer.retrun_list_ir_next_token() in ["static", "field"]:
                self.compile_class_var_dec()
                self.help_class(b)
        if not b:
            if self.tokenizer.retrun_list_ir_next_token() in ["function", "method", "constructor"]:
                self.compile_subroutine()
                self.help_class(b)
        print(self.tokenizer.return_list_line())
        return

    def do_go_to_next_words(self, num):
        for _ in range(num):
            self.tokenizer.advance()

    def compile_class(self) -> None:
        """Compiles a complete class."""
        # Your code goes here!
        self.help_class_first_part(3)
        self.help_class(True)
        self.help_class(False)
        self.start_var()

    def help_class_first_part(self, num):
        for _ in range(num):
            self.tokenizer.advance()  # class and name and {
            if _ == 1:
                self.tokenizer.define_class_name(self.tokenizer.return_token())

    def compile_class_var_dec(self) -> None:
        """Compiles a static declaration or a field declaration."""
        # Your code goes here!
        self.first_part_var_dec(3)
        self.symbol_tab.define(self.name, self.ty, self.kind_of)
        self.until_next_advance()
        self.tokenizer.advance()
        self.start_var()

    def until_next_advance(self):
        if self.tokenizer.retrun_list_ir_next_token() != ";":
            self.tokenizer.advance()  # for , and the name
            if self.tokenizer.cur_token != ',':
                self.name = self.tokenizer.return_token()
                self.symbol_tab.define(self.name, self.ty, self.kind_of)
            self.until_next_advance()

    def first_part_var_dec(self, num):
        for _ in range(num):
            self.tokenizer.advance()  # field/static and type and name
            if _ == 0:
                self.kind_of = self.tokenizer.return_token()
            if _ == 1:
                self.ty = self.tokenizer.return_token()
            if _ == 2:
                self.name = self.tokenizer.return_token()

    def help_subroutine(self):
        if self.tokenizer.retrun_list_ir_next_token() == 'var':
            self.compile_var_dec()
            self.help_subroutine()

    def compile_subroutine(self) -> None:
        """
        Compiles a complete method, function, or constructor.
        You can assume that classes with constructors have at least one field,
        you will understand why this is necessary in project 11.
        """
        # Your code goes here!
        # self.write_start_end_line("start","subroutineDec")
        self.symbol_tab.start_subroutine()
        name_of_method = ''
        name_of_method = self.first_part_com_subrotibe(name_of_method)
        if self.kind_of == "method":
            self.symbol_tab.define('this', self.tokenizer.get_class_name(), 'argument')
        count = 0
        self.inside_sub(count)
        self.help_while()
        self.help_subroutine()
        self.three_case(name_of_method)
        self.help_compile_state()
        self.tokenizer.advance()
        self.start_var()

        pass

    def three_case(self, name_of_method):
        if self.kind_of == "method":
            num = self.symbol_tab.var_count("var")
            if num == None:
                num = 0
            self.vmwriter1.write_function(self.tokenizer.get_class_name() + "{}{}".format(".",
                                                                                          name_of_method), num)
            self.vmwriter1.write_push('argument', 0)
            self.vmwriter1.write_pop('pointer', 0)
        elif self.kind_of == 'function':
            num = self.symbol_tab.var_count("var")
            if num == None:
                num = 0
            self.vmwriter1.write_function(self.tokenizer.get_class_name() + "{}{}".format(".",
                                                                                          name_of_method), num)
        elif self.kind_of == "constructor":
            num_field = self.symbol_tab.var_count("field")
            num_var = self.symbol_tab.var_count("var")
            if num_var == None:
                num_var = 0
            self.vmwriter1.write_function(self.tokenizer.get_class_name() + "." + name_of_method, num_var)
            self.vmwriter1.write_push("constant", num_field)
            self.vmwriter1.write_call("Memory.alloc", 1)
            self.vmwriter1.write_pop('pointer', 0)

    def inside_sub(self, count):
        # print(self.class_name )
        while self.tokenizer.retrun_list_ir_next_token() != ")":
            self.tokenizer.advance()  # for evrything insde the ()
            if count == 0:  # type
                self.ty = self.tokenizer.return_token()
            if count == 1:  # name
                self.name = self.tokenizer.return_token()
            if count == 2:  # ,
                self.symbol_tab.define(self.name, self.ty, 'argument')
                count, self.ty, self.name = -1, '', ''
            count += 1
        if count == 2:  # ,
            self.symbol_tab.define(self.name, self.ty, 'argument')
        self.start_var()

    def first_part_com_subrotibe(self, name_of_method):
        for _ in range(4):
            self.tokenizer.advance()
            if _ == 0:  # mean the name of the func or method
                self.kind_of = self.tokenizer.return_token()
            if _ == 2:
                name_of_method = self.tokenizer.return_token()
        return name_of_method


    def compile_parameter_list(self) -> None:
        """Compiles a (possibly empty) parameter list, not including the
        enclosing "()".
        """
        def compile_parameters():
            nonlocal count
            if self.tokenizer.retrun_list_ir_next_token() != ")":
                self.tokenizer.advance()
                if count == 0:  # type
                    self.ty = self.tokenizer.return_token()
                elif count == 1:  # name
                    self.name = self.tokenizer.return_token()
                elif count == 2:  # ,
                    self.symbol_tab.define(self.name, self.ty, 'argument')
                    count, self.ty, self.name = -1, '', ''
                count += 1
                compile_parameters()
        count = 0
        compile_parameters()
        if count == 2:
            self.symbol_tab.define(self.name, self.ty, 'argument')
        self.start_var()



    def compile_var_dec(self) -> None:
        """Compiles a (possibly empty) parameter list, not including the
        enclosing "()".
        """
        def compile_var_dec_():
            nonlocal count1
            if self.tokenizer.retrun_list_ir_next_token() != ";":
                self.tokenizer.advance()  ##for all the token until the ; symbol
                if count1 == 1:
                    self.ty = self.tokenizer.return_token()
                if count1 == 2:
                    self.name = self.tokenizer.return_token()
                    self.symbol_tab.define(self.name, self.ty, "var")
                if count1 > 2:  # mean ,
                    self.tokenizer.advance()  ##for all the token until the ; symbol
                    self.name = self.tokenizer.return_token()
                    self.symbol_tab.define(self.name, self.ty, "var")
                count1 += 1
                compile_var_dec_()
        count1 = 0
        compile_var_dec_()
        self.tokenizer.advance()
        self.start_var()


    def help_compile_state(self):
        if (self.tokenizer.retrun_list_ir_next_token()
                in ["do", "let", "if", "return", "while"]):
            if self.tokenizer.retrun_list_ir_next_token() == "do":
                self.compile_do()
            elif self.tokenizer.retrun_list_ir_next_token() == "let":
                self.compile_let()
            elif self.tokenizer.retrun_list_ir_next_token() == "if":
                self.compile_if()
            elif self.tokenizer.retrun_list_ir_next_token() == "return":
                self.compile_return()
            elif self.tokenizer.retrun_list_ir_next_token() == "while":
                self.compile_while()
            if self.tokenizer.retrun_list_ir_next_token() != "}":
                self.help_compile_state()
        if self.tokenizer.retrun_list_ir_next_token() != "}":
            self.help_compile_state()
        self.start_var()

        return

    def compile_statements(self) -> None:
        """Compiles a sequence of statements, not including the enclosing
        "{}".
        """
        self.help_compile_state()
        pass


    def write_push_and_pop_to_help_other_func(self, name, number, pop_or_push):
        segment_map = THIS_
        if name in segment_map:
            segment = segment_map[name]
            if pop_or_push == "pop":
                self.vmwriter1.write_pop(segment, number)
            elif pop_or_push == "push":
                self.vmwriter1.write_push(segment, number)

    def compile_do(self) -> None:
        """Compiles a do statement."""
        # Your code goes here!
        cur = 1
        index_backup = None
        self.first_part_do()
        if self.tokenizer.retrun_list_ir_next_token() == '.':
            cur += 2
        self.name_backup = ''
        if self.write_do_help(cur):
            self.name_backup = self.name
            self.index = self.compile_expression_list() + 1
            self.vmwriter1.write_call(self.name_backup, self.index)

        else:
            self.name_backup = self.name
            self.index = self.compile_expression_list()
            self.vmwriter1.write_call(self.name_backup, self.index)

        self.vmwriter1.write_pop("temp", 0)
        self.help_while()
        self.start_var()

    def first_part_do(self):
        for _ in range(2):
            self.tokenizer.advance()
            if _ == 1:
                self.name = self.tokenizer.return_token()

    def write_do_help(self, cur):
        cur_cimpile = True
        kind, index = '', ''
        for _ in range(cur):
            self.tokenizer.advance()
            if cur == 1:
                self.name = self.tokenizer.get_class_name() + '{}{}'.format(".", self.name)
                self.vmwriter1.write_push("pointer", 0)
            else:
                if _ == 1:
                    self.kind_of = self.tokenizer.return_token()
                    self.ty = self.symbol_tab.type_of(self.name)
                    kind = self.symbol_tab.kind_of(self.name)
                    index = self.symbol_tab.index_of(self.name)
                if _ == 2:
                    if self.ty == None:
                        self.name = self.name + '{}{}'.format(".", self.kind_of)
                        cur_cimpile = False
                    else:
                        self.write_push_and_pop_to_help_other_func(kind, index, "push")
                        self.name = self.ty + '{}{}'.format(".", self.kind_of)
        return cur_cimpile

    def compile_let(self) -> None:
        """Compiles a let statement."""
        # Your code goes here!
        counter = 1
        name = ''
        for _ in range(2):
            self.tokenizer.advance()
            if _ == 1:
                name = self.tokenizer.return_token()

        if (self.tokenizer.retrun_list_ir_next_token() == '='
                or self.tokenizer.retrun_list_ir_next_token() == '['):
            if self.tokenizer.retrun_list_ir_next_token() == '[':
                self.tokenizer.advance()  # for =
                while self.tokenizer.retrun_list_ir_next_token() != '=':
                    self.compile_expression()  # for all []
                    counter = 0
                    if self.tokenizer.retrun_list_ir_next_token() == ']':
                        self.tokenizer.advance()
                        break
                self.tokenizer.advance()
            else :
                self.tokenizer.advance()
        #try
        if counter == 0:
            self.write_push_and_pop_to_help_other_func(self.symbol_tab.kind_of(name),
                                                       self.symbol_tab.index_of(name), "push")
            self.vmwriter1.write_arithmetic("add")
        self.compile_expression()
        self.tokenizer.advance()

        self.ty = self.symbol_tab.kind_of(name)
        self.index = self.symbol_tab.index_of(name)
        if counter == 1:
            self.write_push_and_pop_to_help_other_func(self.ty, self.index, "pop")
        if counter == 0:
            self.vmwriter1.write_pop('temp', 0)
            self.vmwriter1.write_pop('pointer', 1)
            self.vmwriter1.write_push('temp', 0)
            self.vmwriter1.write_pop("that", 0)
        self.start_var()

        pass

    def compile_while(self) -> None:
        cur_num = self.count
        self.count += 1
        """Compiles a while statement."""
        # Your code goes here!
        self.vmwriter1.write_label(self.tokenizer.get_class_name() + ".WHILE_BG_ITERATION_WHILE_STATE_{}"
                                   .format(cur_num))

        self.help_while()
        if self.tokenizer.retrun_list_ir_next_token() != ')':
            self.compile_expression()
            self.vmwriter1.write_arithmetic("not")
            self.vmwriter1.write_if(self.tokenizer.get_class_name() + ".WHILE_LINE_ITERATION_WHILE_STATE_{}"
                                    .format(cur_num))
        self.help_while()
        # finish
        self.compile_statements()
        self.vmwriter1.write_goto(self.tokenizer.get_class_name() + ".WHILE_BG_ITERATION_WHILE_STATE_{}"
                                  .format(cur_num))
        self.vmwriter1.write_label(self.tokenizer.get_class_name() + ".WHILE_LINE_ITERATION_WHILE_STATE_{}"
                                   .format(cur_num))
        self.tokenizer.advance()
        self.start_var()

        pass

    def help_while(self):
        for _ in range(2):
            self.tokenizer.advance()

    def compile_return(self) -> None:
        """Compiles a return statement."""
        # Your code goes here!
        self.tokenizer.advance()  # return
        is_return = True
        if self.tokenizer.retrun_list_ir_next_token() == ';':
            self.tokenizer.advance()
        elif self.tokenizer.retrun_list_ir_next_token() != ';':
            is_return = False
            self.compile_term()
            self.help_expre()
            self.tokenizer.advance()
        if is_return:
            self.vmwriter1.write_push('constant', 0)
        self.vmwriter1.write_return()

        pass

    def compile_if(self) -> None:
        """Compiles a if statement, possibly with a trailing else clause."""
        # Your code goes here!

        self.help_while()
        cur_num = self.count
        self.count += 1
        if self.tokenizer.retrun_list_ir_next_token() != ')':
            self.compile_expression()  # for inside word
        self.help_while()

        self.vmwriter1.write_if(self.tokenizer.get_class_name() + ".IF_IS_FIRST_CASE_{}".format(cur_num))
        self.vmwriter1.write_goto(self.tokenizer.get_class_name() + ".IF_IS_SECOND_CASE_{}".format(cur_num))
        self.vmwriter1.write_label(self.tokenizer.get_class_name() + ".IF_IS_FIRST_CASE_{}".format(cur_num))
        if self.tokenizer.retrun_list_ir_next_token() != '}':
            self.compile_statements()
            self.tokenizer.advance()
        elif self.tokenizer.retrun_list_ir_next_token() == '}':
            self.compile_statements()
            self.tokenizer.advance()
        if self.tokenizer.retrun_list_ir_next_token() == 'else':
            self.help_while()
            self.vmwriter1.write_goto(self.tokenizer.get_class_name() + ".ELSE_IF_THIRD_CASE{}".format(cur_num))
            self.vmwriter1.write_label(self.tokenizer.get_class_name() + ".IF_IS_SECOND_CASE_{}".format(cur_num))
            self.compile_statements()
            self.vmwriter1.write_label(self.tokenizer.get_class_name() + ".ELSE_IF_THIRD_CASE{}".format(cur_num))
            self.tokenizer.advance()  # for }
            return
        self.vmwriter1.write_label(self.tokenizer.get_class_name() + ".IF_IS_SECOND_CASE_{}".format(cur_num))

    def compile_expression(self) -> None:
        """Compiles an expression."""
        # Your code goes here!
        self.compile_term()
        self.help_expre()

        pass

    def help_expre(self):
        dic_cur = {'+': 'add', '-': 'sub', '*': '', '/': '', '&': 'and', '<': 'lt',
                   '>': 'gt', '|': 'or', '=': 'eq', "&lt;": 'lt', "&gt;": 'gt', "&amp;": 'and',
                   '^': "shiftright", '#': "shiftleft"}
        if (self.tokenizer.retrun_list_ir_next_token() in
                dic_cur):
            cur = self.tokenizer.retrun_list_ir_next_token()
            self.tokenizer.advance()
            self.compile_term()
            if cur == '*':
                self.vmwriter1.write_call('Math.multiply', 2)
            if cur == '/':
                self.vmwriter1.write_call('Math.divide', 2)
            else:
                self.vmwriter1.write_arithmetic(dic_cur[cur])
            self.help_expre()

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

        if self.token_type_next_and_next_token() in IDENTIFIER.upper():
            self.name = self.tokenizer.retrun_list_ir_next_token()
            if self.help_term_identifier():
                self.vmwriter1.write_pop('pointer', 1)
                self.vmwriter1.write_push('that', 0)
            elif self.kind_of != None:
                (self.write_push_and_pop_to_help_other_func
                 (self.kind_of, self.symbol_tab.index_of(self.name), 'push'))
        elif self.bool_of_kind():
            self.help_term_str_int_keyword()
        self.help_to_close()
        # self.start_var()

        # Your code goes here!

    def help_to_close(self):
        if self.tokenizer.retrun_list_ir_next_token() == "(":
            self.tokenizer.advance()
            self.compile_expression()
            self.tokenizer.advance()
            self.help_to_close()

    def bool_of_kind(self):
        return (self.token_type_next_and_next_token() == STRING_CONST.upper() or
                self.token_type_next_and_next_token() == INT_CONST.upper()
                or self.token_type_next_and_next_token() == KEYWORD.upper()
                or self.tokenizer.retrun_list_ir_next_token() in {
                    "-": "NEG", "~": "NOT", '^': "SHIFTLEFT", '#': "SHIFTRIGHT"}

                or self.tokenizer.retrun_list_ir_next_token() in {'#', '^'})

    def help_term_str_int_keyword(self):
        bin_of = {'~'  :"not", '-' : "neg" }
        if self.token_type_next_and_next_token() == STRING_CONST.upper():
            self.vmwriter1.write_push("constant", len(self.tokenizer.retrun_list_ir_next_token()))
            self.vmwriter1.write_call("String.new", 1)
            self.tokenizer.advance()
            cur = 0
            cur_word = self.tokenizer.return_token()
            while cur < len(cur_word):
                x = ord(cur_word[cur])
                self.vmwriter1.write_push("constant", x)
                self.vmwriter1.write_call("String.appendChar", 2)
                cur += 1

        elif self.token_type_next_and_next_token() == INT_CONST.upper():
            self.tokenizer.advance()
            self.vmwriter1.write_push('constant', int(self.tokenizer.return_token()))
            pass

        elif (self.tokenizer.retrun_list_ir_next_token() in
              {"true": ['constant', 0, 'neg'], "false": ['constant', 0],
                                                            "null": ['constant', 0],
                                                            "this": ['pointer', 0]}):
            cur_word = self.tokenizer.retrun_list_ir_next_token()
            if cur_word == "this":
                self.vmwriter1.write_push("pointer", 0)
            elif cur_word in {'false', 'null'}:
                self.vmwriter1.write_push("constant", 0)
            else:
                # self.vmwriter1.write_push("constant", 0)
                # self.vmwriter1.write_arithmetic('not')
                self.vmwriter1.write_push("constant", 1)
                self.vmwriter1.write_arithmetic('neg')

            self.tokenizer.advance()
        elif self.tokenizer.retrun_list_ir_next_token() in bin_of:
            cur = self.tokenizer.retrun_list_ir_next_token()
            self.tokenizer.advance()
            self.compile_term()
            if cur in bin_of:
                self.vmwriter1.write_arithmetic(bin_of[cur])

        di = {'^': "shiftleft", '#': "shiftright"}
        if self.tokenizer.return_token() in di:
            print("enter shift")
            self.tokenizer.advance()
            self.compile_term()
            self.vmwriter1.write_arithmetic(di[self.tokenizer.return_token()])


    def help_term_identifier(self):
        self.tokenizer.advance()  # varname
        if self.tokenizer.retrun_list_ir_next_token() not in ['[', '.', '(']:
            self.kind_of = self.symbol_tab.kind_of(self.name)
            return False
        self.kind_of = self.symbol_tab.kind_of(self.name)
        self.ty = self.symbol_tab.type_of(self.name)
        self.index = self.symbol_tab.index_of(self.name)
        if self.tokenizer.retrun_list_ir_next_token() == ".":
            return self.point_case()
        elif self.tokenizer.retrun_list_ir_next_token() == "[":
            return self.for_inside_array()
        elif self.tokenizer.retrun_list_ir_next_token() == "(":
            return self.for_inside_paretess()
        else:
            self.kind_of = self.symbol_tab.kind_of(self.name)
            return False

    def for_inside_paretess(self):
        self.tokenizer.advance()
        name = self.tokenizer.get_class_name() + '{}{}'.format('.', self.name)
        self.vmwriter1.write_push("pointer", 0)
        if self.tokenizer.retrun_list_ir_next_token() == ")":
            self.vmwriter1.write_call(name, 1)
        else:
            self.vmwriter1.write_call(name, 1 + self.compile_expression_list())
            # for ( and listexpresion and )
        self.tokenizer.advance()
        self.kind_of = self.symbol_tab.kind_of(name)
        return False

    def for_inside_array(self):
        name = self.name
        self.tokenizer.advance()
        backup_help = self.kind_of
        self.compile_expression()
        if backup_help == None:
            self.vmwriter1.write_arithmetic("add")
            self.tokenizer.advance()  # for [ and expresion and ]
            return True
        else:
            self.write_push_and_pop_to_help_other_func(self.symbol_tab.kind_of(name),
                                                       self.symbol_tab.index_of(name), "push")
            self.vmwriter1.write_arithmetic("add")
            self.tokenizer.advance()  # for [ and expresion and ]
            return True

    def point_case(self):
        self.tokenizer.advance()
        name_ = self.tokenizer.retrun_list_ir_next_token()
        self.tokenizer.advance()
        self.tokenizer.advance()
        if self.ty == None:
            name_ = self.name + '{}{}'.format(".", name_)
            self.vmwriter1.write_call(name_, self.compile_expression_list())
            self.tokenizer.advance()
            self.kind_of = self.symbol_tab.kind_of(name_)
            return False
        else:
            self.write_push_and_pop_to_help_other_func(self.kind_of, self.index, "push")
            name_ = self.ty + '{}{}'.format(".", name_)
            self.vmwriter1.write_call(name_, 1 + self.compile_expression_list())  # for ( and listexpresion and )
            self.tokenizer.advance()
            self.kind_of = self.symbol_tab.kind_of(name_)
            return False

    def compile_expression_list(self) -> int:
        """Compiles a (possibly empty) comma-separated list of expressions."""
        num_expressions = 0

        def compile_expression_list_helper():
            nonlocal num_expressions
            if self.tokenizer.retrun_list_ir_next_token() == ')':
                return
            if num_expressions:
                self.tokenizer.advance()
            self.compile_expression()
            num_expressions += 1
            compile_expression_list_helper()

        compile_expression_list_helper()
        return num_expressions

    def start_var(self):
        self.name = ''
        self.index = None
        self.ty = ''
        # put to zero all the var arg like ty,name ,index
