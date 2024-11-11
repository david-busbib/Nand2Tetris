//start 

@17
D=A
@SP
A=M
M=D
@SP
M=M+1

//new command

@17
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
@R14
M=D
@R13
M=D
@R13
D=M
@CASE1_0
D;JLT
@SP
D=M
@SP
AM=M-1
D=M
@R13
M=D
@CASE2_0
D;JLT
@R14
D=D-M
@R13
M=D
@SP
D=M
@FINISH_LEVEL1_0
0;JMP
(CASE1_0)
@SP
D=M
@SP
AM=M-1
D=M
@CASE3_0
D;JGT
@R14
D=D-M
@R13
M=D
@SP
D=M
@FINISH_LEVEL1_0
0;JMP
(CASE2_0)
@SP
D=M
@R13
M=-1
@FINISH_LEVEL1_0
0;JMP
(CASE3_0)
@SP
D=M
@R13
M=1
@FINISH_LEVEL1_0
0;JMP
(FINISH_LEVEL1_0)
@R13
D=M
@EQUAL0
D;JEQ
@SP
A=M
M=0
@END0
0;JMP
(EQUAL0)
@SP
A=M
M=-1
(END0)
@SP
M=M+1
@R14
M=0
@R13
M=0

//new command

@892
D=A
@SP
A=M
M=D
@SP
M=M+1

//new command

@891
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
@R14
M=D
@R13
M=D
@R13
D=M
@CASE1_1
D;JLT
@SP
D=M
@SP
AM=M-1
D=M
@R13
M=D
@CASE2_1
D;JLT
@R14
D=D-M
@R13
M=D
@SP
D=M
@FINISH_LEVEL1_1
0;JMP
(CASE1_1)
@SP
D=M
@SP
AM=M-1
D=M
@CASE3_1
D;JGT
@R14
D=D-M
@R13
M=D
@SP
D=M
@FINISH_LEVEL1_1
0;JMP
(CASE2_1)
@SP
D=M
@R13
M=-1
@FINISH_LEVEL1_1
0;JMP
(CASE3_1)
@SP
D=M
@R13
M=1
@FINISH_LEVEL1_1
0;JMP
(FINISH_LEVEL1_1)
@R13
D=M
@Y_BIGGER_X1
D;JLT
@SP
A=M
M=0
@END1
0;JMP
(Y_BIGGER_X1)
@SP
A=M
M=-1
(END1)
@SP
M=M+1
@R14
M=0
@R13
M=0

//new command

@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

//new command

@32766
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
@R14
M=D
@R13
M=D
@R13
D=M
@CASE1_2
D;JLT
@SP
D=M
@SP
AM=M-1
D=M
@R13
M=D
@CASE2_2
D;JLT
@R14
D=D-M
@R13
M=D
@SP
D=M
@FINISH_LEVEL1_2
0;JMP
(CASE1_2)
@SP
D=M
@SP
AM=M-1
D=M
@CASE3_2
D;JGT
@R14
D=D-M
@R13
M=D
@SP
D=M
@FINISH_LEVEL1_2
0;JMP
(CASE2_2)
@SP
D=M
@R13
M=-1
@FINISH_LEVEL1_2
0;JMP
(CASE3_2)
@SP
D=M
@R13
M=1
@FINISH_LEVEL1_2
0;JMP
(FINISH_LEVEL1_2)
@R13
D=M
@X_BIGGER_Y2
D;JGT
@SP
A=M
M=0
@END2
0;JMP
(X_BIGGER_Y2)
@SP
A=M
M=-1
(END2)
@SP
M=M+1
@R14
M=0
@R13
M=0

//new command

@56
D=A
@SP
A=M
M=D
@SP
M=M+1

//new command

@31
D=A
@SP
A=M
M=D
@SP
M=M+1

//new command

@53
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
D=M
@SP
AM=M-1
M=M+D
@SP
M=M+1

//new command

@112
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
D=M
@SP
AM=M-1
M=M-D
@SP
M=M+1

//new command

@SP
AM=M-1
M=-M
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
M=M&D
@SP
M=M+1

//new command

@82
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
D=M
@SP
AM=M-1
M=M|D
@SP
M=M+1

//new command

@100
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
@.8
M=D

//new command

@.8
D=M
@SP
A=M
M=D
@SP
M=M+1

//new command

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
@R14
M=D
@SP
AM=M-1
D=M
M=0
@R14
M=D
@R13
A=M
M=D
@R13
M=0
@R14
M=0

//new command

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
@R14
M=D
@SP
AM=M-1
D=M
M=0
@R14
M=D
@R13
A=M
M=D
@R13
M=0
@R14
M=0

//new command

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
@R14
M=D
@SP
AM=M-1
D=M
M=0
@R14
M=D
@R13
A=M
M=D
@R13
M=0
@R14
M=0

//new command

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
@R14
M=D
@SP
AM=M-1
D=M
M=0
@R14
M=D
@R13
A=M
M=D
@R13
M=0
@R14
M=0

//new command

@3
D=M
@SP
A=M
M=D
@SP
M=M+1

//new command

@4
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

@3038
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
@R14
M=D
@SP
AM=M-1
D=M
M=0
@R14
M=D
@R13
A=M
M=D
@R13
M=0
@R14
M=0

//new command

@15
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
@R14
M=D
@SP
AM=M-1
D=M
M=0
@R14
M=D
@R13
A=M
M=D
@R13
M=0
@R14
M=0

//new command

