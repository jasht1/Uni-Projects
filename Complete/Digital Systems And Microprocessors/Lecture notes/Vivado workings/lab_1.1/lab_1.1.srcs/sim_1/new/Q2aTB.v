`timescale 1ns / 1ps

module Q2aTB(

    );
    
    // Decalre variables
    reg A, B, C;
    wire F;
    
    // call test unit
    Q2a_full_expresion UUT (
        .a(A),
        .b(B), 
        .c(C),
        .f(F)
    );
    
    // test all inputs
    integer i = 0;
    initial begin
        for(i = 0; i<8; i=i+1) begin
            {A,B,C} = i[2:0];
            #5;
        end
    end
endmodule
