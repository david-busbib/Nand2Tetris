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
(LOOP_START)
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
@LOOP_START
D;JNE
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
