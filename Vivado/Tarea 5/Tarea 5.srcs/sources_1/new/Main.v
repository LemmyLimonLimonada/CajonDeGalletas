`timescale 1ns / 1ps


module Main(
    input clk,
    input [6:0] sw,
    output wire [6:0] seg,  
    output wire [3:0] an
    );
    
parameter DIV = 100_000;
wire slw_clk;
    
   
Clock_Divider #(DIV) Clock_Divider_inst (clk, slw_clk);

VisualizarNum VisualizarNum_inst (slw_clk, sw, seg, an);


endmodule