`timescale 1ns / 1ps

module JuegoExe(
    input logic [1:0] sw,
    output logic [6:0] seg
    );

always_comb begin
        case (sw)
            4'b0000: seg = 7'b1000000; 
            4'b0001: seg = 7'b1111001; 
            4'b0010: seg = 7'b0100100; 
            4'b0011: seg = 7'b0110000; 
            4'b0100: seg = 7'b0011001; 
            4'b0101: seg = 7'b0010010; 
            4'b0110: seg = 7'b0000010; 
            4'b0111: seg = 7'b1111000; 
            4'b1000: seg = 7'b0000000; 
            4'b1001: seg = 7'b0010000; 
            default: seg = 7'b1000000; 
        endcase
    end

endmodule
