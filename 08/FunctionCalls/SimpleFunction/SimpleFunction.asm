//start 

(SimpleFunction.test)
@R13
D=M
@SP
A=M
M=0
@R13
M=D
@SP
M=M+1
@SP
A=M
M=0
@R13
M=D
@SP
M=M+1
@R13
M=0
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
@1
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
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
@SP
AM=M-1
M=!M
@SP
M=M+1
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
@LCL
D=M
@R15
M=D
@5
D=A
@R15
D=M-D
A=D
D=M
@R14
M=D
@SP
D=A
@ARG
D=M+D
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
@ARG
D=M
D=D+1
@SP
M=D
@1
D=A
@R15
D=M-D
A=D
D=M
@THAT
M=D
@2
D=A
@R15
D=M-D
A=D
D=M
@THIS
M=D
@3
D=A
@R15
D=M-D
A=D
D=M
@ARG
M=D
@4
D=A
@R15
D=M-D
A=D
D=M
@LCL
M=D
@R14
A=M
0;JMP
