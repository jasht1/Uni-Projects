`timescale 1ns / 1ps

module Q2a_full_expresion(
    input a, b, c,
    output f
    );
    
    assign f = (~a & b & ~c) + (a & ~b & ~c) + (a & b & ~c);
    
endmodule
