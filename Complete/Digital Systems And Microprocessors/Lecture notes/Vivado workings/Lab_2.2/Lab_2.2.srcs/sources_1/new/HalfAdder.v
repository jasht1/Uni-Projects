`timescale 1ns / 1ps

module HalfAdder(
    input a, b,
    output y, z
    );
    assign y =  XOR2(a,b);
    assign z =  AND2(a,b);
endmodule

