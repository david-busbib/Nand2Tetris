//start 

@3030
D=A
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1

//new command

@3
D=A
@R13
M=D
@SP
AM=M-1
D=M
M=0
@R13
A=M
M=D
@R13
M=0

//new command

@3040
D=A
@3040
D=A
@SP
A=M
M=D
@SP
M=M+1

//new command

@4
D=A
@R13
M=D
@SP
AM=M-1
D=M
M=0
@R13
A=M
M=D
@R13
M=0

//new command

@32
D=A
@32
D=A
@SP
A=M
M=D
@SP
M=M+1

//new command

@2
D=A
@THIS
D=M+D
@R13
M=D
@SP
AM=M-1
D=M
M=0
@R13
A=M
M=D
@R13
M=0

//new command

@46
D=A
@46
D=A
@SP
A=M
M=D
@SP
M=M+1

//new command

@6
D=A
@THAT
D=M+D
@R13
M=D
@SP
AM=M-1
D=M
M=0
@R13
A=M
M=D
@R13
M=0

//new command

@3
D=M
@3
D=M
@THIS
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1

//new command

@4
D=M
@4
D=M
@THAT
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1

//new command

@SP
AM=M-1
@SP
A=M
D=M
D=M
@SP
AM=M-1
M=M+D
@SP
M=M+1

//new command

@2
D=A
@2
D=A
@THIS
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

//new command

@SP
AM=M-1
@SP
A=M
D=M
D=M
@SP
AM=M-1
M=M-D
@SP
M=M+1

//new command

@6
D=A
@6
D=A
@THAT
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

//new command

@SP
AM=M-1
@SP
A=M
D=M
D=M
@SP
AM=M-1
M=M+D
@SP
M=M+1

//new command

