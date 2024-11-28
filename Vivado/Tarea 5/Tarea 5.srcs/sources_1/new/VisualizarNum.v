`timescale 1ns / 1ps

module VisualizarNum(
    input wire clk,
    input wire [6:0] sw, 
    output wire [6:0] seg,
    output wire [3:0] an
    );

wire [6:0] seg_aux_1, seg_aux_2;
wire [0:0] r1, r2, r3;
wire [3:0] m_bits;
wire [2:0] p_bits;
    assign m_bits = {sw[4], sw[2], sw[1], sw[0]};
    assign r1 = (~(sw[4] ^ (sw[2] ^ sw[0])) ^ sw[6]);
    assign r2 = (~(sw[4] ^ (sw[1] ^ sw[0])) ^ sw[5]);
    assign r3 = (~(sw[2] ^ (sw[1] ^ sw[0])) ^ sw[3]);
    assign p_bits = {r1, r2, r3};

BCDToSevenSeg numero_1 (m_bits[3:0], seg_aux_1);
ThreeToSevenSeg numero_2 (p_bits[2:0], seg_aux_1, seg_aux_2);

SevenSegController salida (clk, 
                            seg_aux_1,
                            seg_aux_2,
                            an, 
                            seg
                            );



endmodule
