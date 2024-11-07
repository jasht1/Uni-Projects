`timescale 1ns / 1ps

module Q1b_3_in_OR(
    input a, b, c,
    output y
    );
    
    assign y = a | b | c;
    
endmodule
