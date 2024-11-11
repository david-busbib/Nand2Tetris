"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing

CLASS_S = {"static", "field"}
SUB_S = {"arg", "var"}

class SymbolTable:
    """A symbol table that associates names with information needed for Jack
    compilation: type, kind and running index. The symbol table has two nested
    scopes (class/subroutine).
    """

    def __init__(self) -> None:
        """Creates a new empty symbol table."""
        # Your code goes here!
        self.symbol_tab_1=[]
        self.symbol_tab_2=[]
        self.count_1=[0,0] #first for static second for field
        self.count_2=[0,0]#first for arg second for var
        self.cur_name=''
        self.cur_type=''
        self.cur_kind=''
        pass

    def start_subroutine(self) -> None:
        """Starts a new subroutine scope (i.e., resets the subroutine's
        symbol table).
        """
        # Your code goes here!
        # Your code goes here!
        # self.symbol_tab_1 = []
        self.symbol_tab_2 = []
        # self.count_1 = [0, 0]  # first for static second for field
        self.count_2 = [0, 0]
        pass

    def define(self, name: str, type: str, kind: str) -> None:
        """Defines a new identifier of a given name, type and kind and assigns
        it a running index. "STATIC" and "FIELD" identifiers have a class scope,
        while "ARG" and "VAR" identifiers have a subroutine scope.

        Args:
            name (str): the name of the new identifier.
            type (str): the type of the new identifier.
            kind (str): the kind of the new identifier, can be:
            "STATIC", "FIELD", "ARG", "VAR".
        """

        # Your code goes here!
        self.cur_name = name
        self.cur_type = type
        self.cur_kind = kind
        if self.cur_kind =='field':
            self.symbol_tab_1.append([self.cur_name,self.cur_type,self.cur_kind,self.count_1[0]])
            self.count_1[0] += 1
        if self.cur_kind =='static':
            self.symbol_tab_1.append([self.cur_name,self.cur_type,self.cur_kind,self.count_1[1]])
            self.count_1[1]+=1
        if self.cur_kind =='argument':
            self.symbol_tab_2.append([self.cur_name,self.cur_type,self.cur_kind,self.count_2[0]])
            self.count_2[0]+=1
        if self.cur_kind =='var':
            self.symbol_tab_2.append([self.cur_name,self.cur_type,self.cur_kind,self.count_2[1]])
            self.count_2[1]+=1



        pass

    def var_count(self, kind: str) -> int:
        """
        Args:
            kind (str): can be "STATIC", "FIELD", "ARG", "VAR".

        Returns:
            int: the number of variables of the given kind already defined in
            the current scope.
        """
        # Your code goes here!
        if kind in CLASS_S:
            if kind == 'field':
                return self.count_1[0]
            if kind== 'static':
                return self.count_1[1]
        if kind in SUB_S:
            if kind == 'arg':
                return self.count_2[0]
            if kind == 'var':
                return self.count_2[1]



        pass

    def kind_of(self, name: str) -> str:
        """
        Args:
            name (str): name of an identifier.

        Returns:
            str: the kind of the named identifier in the current scope, or None
            if the identifier is unknown in the current scope.
        """
        # Your code goes here!
        for i in self.symbol_tab_2:
            if i[0] ==name :
                return i[2]
        for i in self.symbol_tab_1:
            if i[0] == name:
                return i[2]

        return

    def type_of(self, name: str) -> str:
        """
        Args:
            name (str):  name of an identifier.

        Returns:
            str: the type of the named identifier in the current scope.
        """
        # Your code goes here!
        for i in self.symbol_tab_2:
            if i[0] == name:
                return i[1]
        for i in self.symbol_tab_1:
            if i[0] == name:
                return i[1]

        return

    def index_of(self, name: str) -> int:
        """
        Args:
            name (str):  name of an identifier.

        Returns:
            int: the index assigned to the named identifier.
        """
        try:
            for i in self.symbol_tab_2:
                if i[0] == name:
                    return i[3]
            for i in self.symbol_tab_1:
                if i[0] == name:
                    return i[3]
        except:
            return 0
        return 0
        # Your code goes here!

