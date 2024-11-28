`timescale 1ns / 1ps

module BCDToSevenSeg(
    input wire [3:0] sw, // Numero BCD
    output reg [6:0] seg
    );


always @(*) begin

    case (sw)
        4'b0000: seg = 7'b1000000; // revisamos cuando la entrada es 0
        4'b0001: seg = 7'b1111001; // revisamos cuando la entrada es 1
        4'b0010: seg = 7'b0100100; // revisamos cuando la entrada es 2
        4'b0011: seg = 7'b0110000; // revisamos cuando la entrada es 3
        4'b0100: seg = 7'b0011001; // revisamos cuando la entrada es 4
        4'b0101: seg = 7'b0010010; // revisamos cuando la entrada es 5
        4'b0110: seg = 7'b0000010; // revisamos cuando la entrada es 6
        4'b0111: seg = 7'b1111000; // revisamos cuando la entrada es 7
        4'b1000: seg = 7'b0000000; // revisamos cuando la entrada es 8
        4'b1001: seg = 7'b0010000; // revisamos cuando la entrada es 9
        default: seg = 7'b1000000; // revisamos cuando la entrada es otra
    endcase
        
end
   

endmodule
