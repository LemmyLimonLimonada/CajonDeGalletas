`timescale 1ns / 1ps

module Ganador(
    input logic [1:0] p_state, g_state,
    output logic [6:0] seg
);

    always_comb begin
        if (g_state == 2'b00) begin
            case (p_state)
                2'b00: seg = 7'b1111111; 
                2'b01: seg = 7'b0100100;
                2'b10: seg = 7'b1111001; 
                2'b11: seg = 7'b1111111;  
                default: seg = 7'b1111111; 
            endcase
        end else begin
            seg = 7'b1111111; 
        end
    end

endmodule
