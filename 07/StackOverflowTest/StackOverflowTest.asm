//start 

@0
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
@FINISH_LEVEL1_0
0;JMP
(CASE1_0)
@SP
AM=M-1
D=M
@CASE3_0
D;JGT
@R14
D=D-M
@R13
M=D
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
@Y_BIGGER_X0
D;JLT
@SP
A=M
M=0
@END0
0;JMP
(Y_BIGGER_X0)
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

@2
D=A
@SP
A=M
M=D
@SP
M=M+1

//new command

@0
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
@FINISH_LEVEL1_1
0;JMP
(CASE1_1)
@SP
AM=M-1
D=M
@CASE3_1
D;JGT
@R14
D=D-M
@R13
M=D
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

@0
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
@FINISH_LEVEL1_2
0;JMP
(CASE1_2)
@SP
AM=M-1
D=M
@CASE3_2
D;JGT
@R14
D=D-M
@R13
M=D
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

@2
D=A
@SP
A=M
M=D
@SP
M=M+1

//new command

@0
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
@FINISH_LEVEL1_3
0;JMP
(CASE1_3)
@SP
AM=M-1
D=M
@CASE3_3
D;JGT
@R14
D=D-M
@R13
M=D
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
@X_BIGGER_Y3
D;JGT
@SP
A=M
M=0
@END3
0;JMP
(X_BIGGER_Y3)
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

