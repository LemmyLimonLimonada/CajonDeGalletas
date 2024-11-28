`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 05/29/2024 01:20:07 PM
// Design Name: 
// Module Name: Main
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module Main(
    input clk,
    input [15:0] sw,
    output wire [6:0] seg,  
    output wire [3:0] an
    );
    
parameter DIV = 100_000;
wire slw_clk;
    
    
// Instanciamos un dividor de clock de frecuencia 1kHz  
Clock_Divider #(DIV) Clock_Divider_inst (clk, slw_clk);

// Instanciamos el modulo que permite visualizar los numeros en el display
VisualizarNum VisualizarNum_inst (slw_clk, sw, seg, an);




 
endmodule