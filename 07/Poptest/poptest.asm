//start 

@65
D=A
@SP
A=M
M=D
@SP
M=M+1

//new command

@0
D=A
@LCL
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

@65
D=A
@SP
A=M
M=D
@SP
M=M+1

//new command

@SP
AM=M-1
D=M
M=0
@R5
M=D

//new command

@0
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

//new command

@R5
D=M
@SP
A=M
M=D
@SP
M=M+1

//new command

@SP
AM=M-1
D=M
@SP
AM=M-1
M=M+D
@SP
M=M+1

//new command

