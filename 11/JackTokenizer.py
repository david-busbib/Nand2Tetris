"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing

KEYWORD = "KEYWORD"
SYMBOL = "SYMBOL"
IDENTIFIER = "IDENTIFIER"
INT_CONST = "INT_CONST"
STRING_CONST = "STRING_CONST"


class JackTokenizer:
    """Removes all comments from the input stream and breaks it
    into Jack language tokens, as specified by the Jack grammar.

    # Jack Language Grammar

    A Jack file is a stream of characters. If the file represents a
    valid program, it can be tokenized into a stream of valid tokens. The
    tokens may be separated by an arbitrary number of whitespace characters,
    and comments, which are ignored. There are three possible comment formats:
    /* comment until closing */ , /** API comment until closing */ , and
    // comment until the lines end.

    - xxx: regular typeface is used for names of language constructs
    - x | y: indicates that either x or y can appear.
    - x?: indicates that x appears 0 or 1 times.
    - x*: indicates that x appears 0 or more times.

    ## Lexical Elements

    The Jack language includes five types of terminal elements (tokens).

    - keyword: 'class' | 'constructor' | 'function' | 'method' | 'field' |
               'static' | 'var' | 'int' | 'char' | 'boolean' | 'void' | 'true' |
               'false' | 'null' | 'this' | 'let' | 'do' | 'if' | 'else' |
               'while' | 'return'
    - symbol: '{' | '}' | '(' | ')' | '[' | ']' | '.' | ',' | ';' | '+' |
              '-' | '*' | '/' | '&' | '|' | '<' | '>' | '=' | '~' | '^' | '#'
    - integerConstant: A decimal number in the range 0-32767.
    - StringConstant: '"' A sequence of Unicode characters not including
                      double quote or newline '"'
    - identifier: A sequence of letters, digits, and underscore ('_') not
                  starting with a digit. You can assume keywords cannot be
                  identifiers, so 'self' cannot be an identifier, etc'.

    ## Program Structure

    A Jack program is a collection of classes, each appearing in a separate
    file. A compilation unit is a single class. A class is a sequence of tokens
    structured according to the following context free syntax:

    - class: 'class' className '{' classVarDec* subroutineDec* '}'
    - classVarDec: ('static' | 'field') type varName (',' varName)* ';'
    - type: 'int' | 'char' | 'boolean' | className
    - subroutineDec: ('constructor' | 'function' | 'method') ('void' | type)
    - subroutineName '(' parameterList ')' subroutineBody
    - parameterList: ((type varName) (',' type varName)*)?
    - subroutineBody: '{' varDec* statements '}'
    - varDec: 'var' type varName (',' varName)* ';'
    - className: identifier
    - subroutineName: identifier
    - varName: identifier

    ## Statements

    - statements: statement*
    - statement: letStatement | ifStatement | whileStatement | doStatement |
                 returnStatement
    - letStatement: 'let' varName ('[' expression ']')? '=' expression ';'
    - ifStatement: 'if' '(' expression ')' '{' statements '}' ('else' '{'
                   statements '}')?
    - whileStatement: 'while' '(' 'expression' ')' '{' statements '}'
    - doStatement: 'do' subroutineCall ';'
    - returnStatement: 'return' expression? ';'

    ## Expressions

    - expression: term (op term)*
    - term: integerConstant | stringConstant | keywordConstant | varName |
            varName '['expression']' | subroutineCall | '(' expression ')' |
            unaryOp term
    - subroutineCall: subroutineName '(' expressionList ')' | (className |
                      varName) '.' subroutineName '(' expressionList ')'
    - expressionList: (expression (',' expression)* )?
    - op: '+' | '-' | '*' | '/' | '&' | '|' | '<' | '>' | '='
    - unaryOp: '-' | '~' | '^' | '#'
    - keywordConstant: 'true' | 'false' | 'null' | 'this'

    Note that ^, # correspond to shiftleft and shiftright, respectively.
    """

    def __init__(self, input_stream: typing.TextIO) -> None:
        """Opens the input stream and gets ready to tokenize it.

        Args:
            input_stream (typing.TextIO): input stream.
        """
        # Your code goes here!
        # A good place to start is to read all the lines of the input:
        # input_lines = input_stream.read().splitlines()
        self.input_line = input_stream.read().splitlines()
        self.left = 0
        self.cur_line_num = 0
        self.list_line = []
        self.cur_token = ''
        self.end_line = True
        self.cur_line = ''
        self.first_line = True
        self.next_token = ''
        self.comment_one_star = 0
        self.comment_one_two = 0
        self.class_name = ''

    def get_class_name(self):
            return self.class_name
    def define_class_name(self,name):
        self.class_name=name

    def has_more_tokens(self) -> bool:
        """Do we have more tokens in the input?

        Returns:
            bool: True if there are more tokens, False otherwise.
        """
        # Your code goes here!
        if self.left == len(self.list_line):
            return False

        return True

        pass
    def return_list_line(self):
        return self.list_line

    def del_com(self):
        """
        return the cur line command without any space or explication
        """

        cur_words = " ".join(self.cur_line.split())
        try:
            cur_words = cur_words[:cur_words.index('//')]
        except:
            pass
        try:
            cur_words.index('/*')
            try:
                if cur_words.index('*/'):
                    return cur_words[:cur_words.index('/*')] + cur_words[cur_words.index('*/') + 2:]
            except:
                self.comment_one_star = 1

            return cur_words[:cur_words.index('/*')]
        except:
            pass
        try:
            cur_words.index('/**')
            try:
                if cur_words.index('*/'):
                    return cur_words[:cur_words.index('/*') - 1] + cur_words[cur_words.index('*/'):]
            except:
                self.comment_one_two = 1
            # self.comment_one_two=1
            return cur_words[:cur_words.index('/**')]
        except:
            pass
        return cur_words

    def arrange_line(self, cur):
        modified_string = ''.join(char if char
                                          not in
                                          ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|',
                                           '<', '>', '=', '~']
                                  else f' {char} ' for char in cur)
        result =[]
        for i in modified_string.split(' ') :
            if i and i.startswith("#") or i.startswith("^"):
                result.append(i[0])
                result.append(i[1:])
            else :
                if i:
                    result.append(i)
        return result

    def help_advance(self, first_lne):
        in_1 = self.input_line[first_lne].index('"')
        in_2 = self.input_line[first_lne].index('"', in_1 + 1)
        self.cur_line = self.input_line[first_lne][:in_1]
        cur = self.del_com()
        self.list_line.extend(self.arrange_line(cur))

        cur2 = self.input_line[first_lne][in_1:in_2 + 1]
        self.list_line.append('{}'.format(cur2))

        self.cur_line = self.input_line[first_lne][in_2 + 1:]
        cur3 = self.del_com()
        self.list_line.extend(self.arrange_line(cur3))

    def advance(self) -> None:
        """Gets the next token from the input and makes it the current token.
        This method should be called if has_more_tokens() is true.
        Initially there is no current token.
        """
        # Your code goes here!
        if self.first_line:
            first_lne = 0
            self.help_of_help_advance(first_lne)

        if not self.first_line:
            if self.has_more_tokens():
                self.cur_token = self.list_line[self.left]
                self.left += 1
                try:
                    self.next_token = self.list_line[self.left]
                except:
                    pass

    def help_of_help_advance(self, first_lne):
        while first_lne != len(self.input_line) and self.first_line:
            if self.end_line:
                try1 = self.input_line[first_lne].split()
                if (not try1 or try1[0].startswith('//') or (try1[0].startswith('/**'))
                        or (try1[0].startswith('/*') or self.comment_one_star or self.comment_one_two)
                ):
                    try:
                        if try1[0].startswith('/**') or self.comment_one_two:
                            while try1 == [] or not try1[-1].endswith('*/'):
                                first_lne += 1
                                try1 = self.input_line[first_lne].split()
                            self.comment_one_two = 0
                    except:
                        pass
                    try:
                        if try1[0].startswith('/*') or self.comment_one_star:
                            while not try1[-1].endswith('*/'):
                                first_lne += 1
                                try1 = self.input_line[first_lne].split()
                            self.comment_one_star = 0
                    except:
                        pass

                    pass
                else:
                    indexof_ = 0
                    index_of_2 = 0
                    try:
                        indexof_ = self.input_line[first_lne].index('//')
                        index_of_2 = self.input_line[first_lne].index('"', 0)


                    except:
                        pass
                    if '"' in self.input_line[first_lne] and (
                            (indexof_ and index_of_2 < indexof_) or (not indexof_ and not index_of_2)):
                        self.help_advance(first_lne)
                    else:
                        self.cur_line = self.input_line[first_lne]
                        cur = self.del_com()
                        self.list_line.extend(self.arrange_line(cur))
                first_lne += 1
        self.first_line = False

    def retrun_list_ir_next_token(self, boo=None):
        if (boo):
            return self.cur_line
        try:
            return self.next_token
        except:
            return self.token



    def return_token(self):
        return self.cur_token

    def token_type(self) -> str:
        """
        Returns:
            str: the type of the current token, can be
            "KEYWORD", "SYMBOL", "IDENTIFIER", "INT_CONST", "STRING_CONST"
        """
        # Your code goes here!
        if self.cur_token in ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=',
                              '~']:
            return SYMBOL
        if (self.cur_token in
                ['class', 'constructor', 'function', 'method', 'field',
                              'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 'false',
                              'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return']):
            return KEYWORD
        try:
            tr = int(self.cur_token)
            if tr >= 0 and tr <= 32767:
                return INT_CONST
        except:
            pass
        try:
            if self.cur_token.startswith('"') and self.cur_token.endswith('"'):
                return STRING_CONST
        except:
            pass

        try:
            if int(self.cur_token[0]):
                pass
        except:
            return IDENTIFIER



    def keyword(self) -> str:
        """
        Returns:
            str: the keyword which is the current token.
            Should be called only when token_type() is "KEYWORD".
            Can return "CLASS", "METHOD", "FUNCTION", "CONSTRUCTOR", "INT",
            "BOOLEAN", "CHAR", "VOID", "VAR", "STATIC", "FIELD", "LET", "DO",
            "IF", "ELSE", "WHILE", "RETURN", "TRUE", "FALSE", "NULL", "THIS"
        """
        # Your code goes here!
        if self.token_type() == KEYWORD:
            return self.cur_token
        pass
    def keyword_next(self) -> str:

        return self.next_token
        pass

    def symbol(self) -> str:
        """
        Returns:
            str: the character which is the current token.
            Should be called only when token_type() is "SYMBOL".
            Recall that symbol was defined in the grammar like so:
            symbol: '{' | '}' | '(' | ')' | '[' | ']' | '.' | ',' | ';' | '+' |
              '-' | '*' | '/' | '&' | '|' | '<' | '>' | '=' | '~' | '^' | '#'
        """
        # Your code goes here!
        if self.token_type() == SYMBOL:
            if self.cur_token == '<':
                return '&lt;'
            if self.cur_token == '&':
                return '&amp;'
            if self.cur_token == '>':
                return '&gt;'
            return self.cur_token

        pass
    def symbol_next(self) -> str:
        if self.next_token == '<':
            return '&lt;'
        if self.next_token == '&':
            return '&amp;'
        if self.next_token == '>':
            return '&gt;'
        return self.next_token

        pass

    def identifier(self) -> str:
        """
        Returns:
            str: the identifier which is the current token.
            Should be called only when token_type() is "IDENTIFIER".
            Recall that identifiers were defined in the grammar like so:
            identifier: A sequence of letters, digits, and underscore ('_') not
                  starting with a digit. You can assume keywords cannot be
                  identifiers, so 'self' cannot be an identifier, etc'.
        """
        # Your code goes here!
        if self.token_type() == IDENTIFIER:
            return self.cur_token
        pass
    def identifier_next(self) -> str:
        return self.next_token
        pass

    def int_val(self) -> int:
        """
        Returns:
            str: the integer value of the current token.
            Should be called only when token_type() is "INT_CONST".
            Recall that integerConstant was defined in the grammar like so:
            integerConstant: A decimal number in the range 0-32767.
        """
        # Your code goes here!
        if self.token_type() == INT_CONST:
            return int(self.cur_token)
    def int_val_next(self) -> int:
        return int(self.next_token)

    def string_val(self) -> str:
        """
        Returns:
            str: the string value of the current token, without the double
            quotes. Should be called only when token_type() is "STRING_CONST".
            Recall that StringConstant was defined in the grammar like so:
            StringConstant: '"' A sequence of Unicode characters not including
                      double quote or newline '"'
        """
        # Your code goes here!
        if self.token_type() == STRING_CONST:
            return str(self.cur_token[1:-1])
    def string_val_next(self) -> str:
        return str(self.next_token[1:-1])
