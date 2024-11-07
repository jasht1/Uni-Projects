`timescale 1ns / 1ps

module Q1bTB_3_in_OR(

    );
    
    // Decalre variables
    reg A, B, C;
    wire Y;
    
    // call test unit
    Q1b_3_in_OR UUT (
        .a(A),
        .b(B), 
        .c(C),
        .y(Y)
    );
    
    // test all inputs
    integer i = 0;
    initial begin
        for(i = 0; i<8; i=i+1) begin
            {A,B,C} = i[2:0];
            #5;
        end
    end
    // overcomplicated
//    initial begin
//        {A,B,C} = 3'b000; // assign inputs to a bus
//    end
//    always begin
//        #5;
//        {A,B,C} = 3'b1; // add 1 to the bus
//        if (&{A,B,C}) begin // see if it overflows
//            #5;
//            $finish;
//        end
//    end
endmodule
