// This file is part of nand2tetris, as taught in The Hebrew University, and
// was written by Aviv Yaish. It is an extension to the specifications given
// [here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
// as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
// Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).

// This program illustrates low-level handling of the screen and keyboard
// devices, as follows.
//
// The program runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed.
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.
//
// Assumptions:
// Your program may blacken and clear the screen's pixels in any spatial/visual
// Order, as long as pressing a key continuously for long enough results in a
// fully blackened screen, and not pressing any key for long enough results in a
// fully cleared screen.
//
// Test Scripts:
// For completeness of testing, test the Fill program both interactively and
// automatically.
//
// The supplied FillAutomatic.tst script, along with the supplied compare file
// FillAutomatic.cmp, are designed to test the Fill program automatically, as
// described by the test script documentation.
//
// The supplied Fill.tst script, which comes with no compare file, is designed
// to do two things:
// - Load the Fill.hack program
// - Remind you to select 'no animation', and then test the program
//   interactively by pressing and releasing some keyboard keys

// Put your code here
@whitehelp
M=0                /// put new help value
@blackhelp
M=0
@START //jump because no need of the first if
0;JMP

(BEFORE_START) // if for black table
@8191
D=A
@whitehelp
M=D
@blackhelp
M=D


(START)

@KBD
D=M
@BLACK
D;JGT


(WHITE) //color the screen white
@KBD
D=M
@START
D;JNE
@whitehelp
D=M
M=M-1
@SCREEN
A=A+D
M=0
@GO_START
0;JMP

@START // no need this but only for double checking
0;JMP


(BLACK)
@blackhelp
D=M
@SCREEN
A=A+D
M=-1
D=D+1
@whitehelp
M=D
@blackhelp
M=D

@8191
D=A-D
@GO_START // goto start but first inizield the variable
D;JGT
@BEFORE_START
D;JLE

(GO_START)
@whitehelp
D=M
@blackhelp
M=D
@START //go back to start
0;JMP


(STOP)
@STOP
0;JMP