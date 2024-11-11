// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/01/And.tst

load And.hdl,
output-file And.out,
compare-to And.cmp,
output-list a%B3.1.3 b%B3.1.3 out%B3.1.3;

set a 00,
set b 00,
eval,
output;

set a 00,
set b 01,
eval,
output;

set a 11,
set b 00,
eval,
output;

set a 01,
set b 01,
eval,
output;


set a 10,
set b 01,
eval,
output;