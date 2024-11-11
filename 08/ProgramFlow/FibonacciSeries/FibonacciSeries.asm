//start 

//new command 
//new command 
//new command 
//new command 
//new command 
//new command 
//new command 
//new command 
//new command 
//new command 
//new command 
@1
D=A
@ARG
A=M+D
D=M
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
//new command 
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//new command 
@0
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
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//new command 
@1
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
//new command 
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//new command 
@2
D=A
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
@SP
AM=M-1
M=M-D
@SP
M=M+1
//new command 
@0
D=A
@ARG
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
//new command 
(MAIN_LOOP_START)
//new command 
//new command 
@0
D=A
@ARG
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
D=M
@COMPUTE_ELEMENT
D;JNE
//new command 
@END_PROGRAM
0;JMP
//new command 
//new command 
(COMPUTE_ELEMENT)
//new command 
//new command 
@0
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
@1
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
@SP
AM=M-1
M=M+D
@SP
M=M+1
//new command 
@2
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
//new command 
@4
D=M
@SP
A=M
M=D
@SP
M=M+1
//new command 
@1
D=A
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
@SP
AM=M-1
M=M+D
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
//new command 
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//new command 
@1
D=A
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
@SP
AM=M-1
M=M-D
@SP
M=M+1
//new command 
@0
D=A
@ARG
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
//new command 
@MAIN_LOOP_START
0;JMP
//new command 
//new command 
(END_PROGRAM)
