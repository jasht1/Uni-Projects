`timescale 1ns / 1ps

module L1Q1a_2_in_AND_tb(
    );
    
    // Decalre variables
    reg A, B;
    wire Y;
    
    // call test unit
    L1Q1a_2_in_AND UUT (
        .a(A),
        .b(B), 
        .y(Y)
    );
    
    initial begin
        A = 0;
        B = 0;
        #5;
        
        A = 1;
        #5;
        
        B = 1;
        #5;
        
        A = 0;
        #5;
        
        $finish;
    end
endmodule
