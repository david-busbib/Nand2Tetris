// This file is part of nand2tetris, as taught in The Hebrew University, and
// was written by Aviv Yaish. It is an extension to the specifications given
// [here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
// as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
// Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).

// Multiplies R0 and R1 and stores the result in R2.
//
// Assumptions:
// - R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.
// - You can assume that you will only receive arguments that satisfy:
//   R0 >= 0, R1 >= 0, and R0*R1 < 32768.
// - Your program does not need to test these conditions.
//
// Requirements:
// - Your program should not change the values stored in R0 and R1.
// - You can implement any multiplication algorithm you want.

// Put your code here.
@2 //the R2
M=0 //check that no value is in their
@sum
M=0


@R1
D=M
@i //the equal to remove each loop one
M=D


@1
D=M
@END // check if really is bigger from zero
D;JEQ

@0
D=M
@END // // check if really is bigger from zero
D;JEQ

(LOOP)
@i //while i is bigger from zero add to sum the r1 value
D=M
@END
D;JLE


@R0
D=M
@sum
M=D+M

@i
M=M-1

@LOOP
0;JMP


(END) //apdate the R2 to be the * between R1 and R2
@sum
D=M
@R2
M=D
(END1)
@END1
0;JMP





