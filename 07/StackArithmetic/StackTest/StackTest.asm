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

@17
D=A
@SP
A=M
M=D
@SP
M=M+1

//new command

@16
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
@EQUAL1
D;JEQ
@SP
A=M
M=0
@END1
0;JMP
(EQUAL1)
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

@16
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
@EQUAL2
D;JEQ
@SP
A=M
M=0
@END2
0;JMP
(EQUAL2)
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
@CASE1_3
D;JLT
@SP
D=M
@SP
AM=M-1
D=M
@R13
M=D
@CASE2_3
D;JLT
@R14
D=D-M
@R13
M=D
@SP
D=M
@FINISH_LEVEL1_3
0;JMP
(CASE1_3)
@SP
D=M
@SP
AM=M-1
D=M
@CASE3_3
D;JGT
@R14
D=D-M
@R13
M=D
@SP
D=M
@FINISH_LEVEL1_3
0;JMP
(CASE2_3)
@SP
D=M
@R13
M=-1
@FINISH_LEVEL1_3
0;JMP
(CASE3_3)
@SP
D=M
@R13
M=1
@FINISH_LEVEL1_3
0;JMP
(FINISH_LEVEL1_3)
@R13
D=M
@Y_BIGGER_X3
D;JLT
@SP
A=M
M=0
@END3
0;JMP
(Y_BIGGER_X3)
@SP
A=M
M=-1
(END3)
@SP
M=M+1
@R14
M=0
@R13
M=0

//new command

@891
D=A
@SP
A=M
M=D
@SP
M=M+1

//new command

@892
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
@CASE1_4
D;JLT
@SP
D=M
@SP
AM=M-1
D=M
@R13
M=D
@CASE2_4
D;JLT
@R14
D=D-M
@R13
M=D
@SP
D=M
@FINISH_LEVEL1_4
0;JMP
(CASE1_4)
@SP
D=M
@SP
AM=M-1
D=M
@CASE3_4
D;JGT
@R14
D=D-M
@R13
M=D
@SP
D=M
@FINISH_LEVEL1_4
0;JMP
(CASE2_4)
@SP
D=M
@R13
M=-1
@FINISH_LEVEL1_4
0;JMP
(CASE3_4)
@SP
D=M
@R13
M=1
@FINISH_LEVEL1_4
0;JMP
(FINISH_LEVEL1_4)
@R13
D=M
@Y_BIGGER_X4
D;JLT
@SP
A=M
M=0
@END4
0;JMP
(Y_BIGGER_X4)
@SP
A=M
M=-1
(END4)
@SP
M=M+1
@R14
M=0
@R13
M=0

//new command

@891
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
@CASE1_5
D;JLT
@SP
D=M
@SP
AM=M-1
D=M
@R13
M=D
@CASE2_5
D;JLT
@R14
D=D-M
@R13
M=D
@SP
D=M
@FINISH_LEVEL1_5
0;JMP
(CASE1_5)
@SP
D=M
@SP
AM=M-1
D=M
@CASE3_5
D;JGT
@R14
D=D-M
@R13
M=D
@SP
D=M
@FINISH_LEVEL1_5
0;JMP
(CASE2_5)
@SP
D=M
@R13
M=-1
@FINISH_LEVEL1_5
0;JMP
(CASE3_5)
@SP
D=M
@R13
M=1
@FINISH_LEVEL1_5
0;JMP
(FINISH_LEVEL1_5)
@R13
D=M
@Y_BIGGER_X5
D;JLT
@SP
A=M
M=0
@END5
0;JMP
(Y_BIGGER_X5)
@SP
A=M
M=-1
(END5)
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
@CASE1_6
D;JLT
@SP
D=M
@SP
AM=M-1
D=M
@R13
M=D
@CASE2_6
D;JLT
@R14
D=D-M
@R13
M=D
@SP
D=M
@FINISH_LEVEL1_6
0;JMP
(CASE1_6)
@SP
D=M
@SP
AM=M-1
D=M
@CASE3_6
D;JGT
@R14
D=D-M
@R13
M=D
@SP
D=M
@FINISH_LEVEL1_6
0;JMP
(CASE2_6)
@SP
D=M
@R13
M=-1
@FINISH_LEVEL1_6
0;JMP
(CASE3_6)
@SP
D=M
@R13
M=1
@FINISH_LEVEL1_6
0;JMP
(FINISH_LEVEL1_6)
@R13
D=M
@X_BIGGER_Y6
D;JGT
@SP
A=M
M=0
@END6
0;JMP
(X_BIGGER_Y6)
@SP
A=M
M=-1
(END6)
@SP
M=M+1
@R14
M=0
@R13
M=0

//new command

@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

//new command

@32767
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
@CASE1_7
D;JLT
@SP
D=M
@SP
AM=M-1
D=M
@R13
M=D
@CASE2_7
D;JLT
@R14
D=D-M
@R13
M=D
@SP
D=M
@FINISH_LEVEL1_7
0;JMP
(CASE1_7)
@SP
D=M
@SP
AM=M-1
D=M
@CASE3_7
D;JGT
@R14
D=D-M
@R13
M=D
@SP
D=M
@FINISH_LEVEL1_7
0;JMP
(CASE2_7)
@SP
D=M
@R13
M=-1
@FINISH_LEVEL1_7
0;JMP
(CASE3_7)
@SP
D=M
@R13
M=1
@FINISH_LEVEL1_7
0;JMP
(FINISH_LEVEL1_7)
@R13
D=M
@X_BIGGER_Y7
D;JGT
@SP
A=M
M=0
@END7
0;JMP
(X_BIGGER_Y7)
@SP
A=M
M=-1
(END7)
@SP
M=M+1
@R14
M=0
@R13
M=0

//new command

@32766
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
@CASE1_8
D;JLT
@SP
D=M
@SP
AM=M-1
D=M
@R13
M=D
@CASE2_8
D;JLT
@R14
D=D-M
@R13
M=D
@SP
D=M
@FINISH_LEVEL1_8
0;JMP
(CASE1_8)
@SP
D=M
@SP
AM=M-1
D=M
@CASE3_8
D;JGT
@R14
D=D-M
@R13
M=D
@SP
D=M
@FINISH_LEVEL1_8
0;JMP
(CASE2_8)
@SP
D=M
@R13
M=-1
@FINISH_LEVEL1_8
0;JMP
(CASE3_8)
@SP
D=M
@R13
M=1
@FINISH_LEVEL1_8
0;JMP
(FINISH_LEVEL1_8)
@R13
D=M
@X_BIGGER_Y8
D;JGT
@SP
A=M
M=0
@END8
0;JMP
(X_BIGGER_Y8)
@SP
A=M
M=-1
(END8)
@SP
M=M+1
@R14
M=0
@R13
M=0

//new command

@57
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

@SP
AM=M-1
M=!M
@SP
M=M+1

//new command

