`timescale 1ns / 1ps

module FullAdder(
    input a, b, c,
    output y, z
    );
    wire [2:0] carry;
    assign carry =  HalfAdder(a,b);
    assign y =  HalfAdder(a,b);
    assign z =  AND2(a,b);
endmodule
