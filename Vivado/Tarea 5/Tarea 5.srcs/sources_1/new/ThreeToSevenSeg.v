`timescale 1ns / 1ps

module ThreeToSevenSeg(
    input wire [2:0] sw, 
    input wire [6:0] seg_aux_1,
    output reg [6:0] seg
    );


always @(*) begin
    if (seg_aux_1 != 3'b0000110) begin
        case (sw)
            3'b000: seg = 7'b1000000; 
            3'b001: seg = 7'b0011001; 
            3'b010: seg = 7'b0000010; 
            3'b011: seg = 7'b0100100; 
            3'b100: seg = 7'b1111000; 
            3'b101: seg = 7'b0110000; 
            3'b110: seg = 7'b0010010; 
            3'b111: seg = 7'b1111001; 
            default: seg = 7'b1000000;
        endcase
        end
     else if (seg_aux_1 == 3'b0000110) begin
        seg = 7'b0000110;  
        end

end
   

endmodule
