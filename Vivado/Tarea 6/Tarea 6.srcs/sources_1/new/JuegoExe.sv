`timescale 1ns / 1ps

module JuegoExe(
    input logic [1:0] p_state,
    output logic [6:0] seg
);

    always_comb begin
        case (p_state)
            2'b00: seg = 7'b1000000; 
            2'b01: seg = 7'b1111001; 
            2'b10: seg = 7'b1111001; 
            2'b11: seg = 7'b1111111; 
            default: seg = 7'b1111111; 
        endcase
    end

endmodule
