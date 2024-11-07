`timescale 1ns / 1ps

module XOR2(
    input a, b,
    output reg y
    );
    always @(a or b) begin
        if (a == 1 & b == 0) begin
            y=1;
        end
        if (a == 0 & b == 1) begin
            y=1;
        end
        else 
            y=0;
end

endmodule
