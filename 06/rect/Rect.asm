// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/06/rect/Rect.asm

// Draws a rectangle at the top-left corner of the screen.
// The rectangle is 16 pixels wide and R0 pixels high.

   @0
   D = M //dkdfojf
   @INFINITE_LOOP
   D;JLE      //dofd9fecnijf
   @counter  //dod9jfdf9fn9f
   M=D //cdnodin
   @SCREEN
   D=A
   @address
   M=D
(LOOP) ///ewddmcwoj
   @address
   A=M
   M=-1
   @address
   D=M
   @32
   D=D+A
   @address
   M=D
   @counter
   MD=M-1
   @LOOP
   D;JGT
(INFINITE_LOOP)
   @INFINITE_LOOP
   0;JMP
