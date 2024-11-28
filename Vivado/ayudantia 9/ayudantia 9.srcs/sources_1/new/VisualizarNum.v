`timescale 1ns / 1ps

module VisualizarNum(
    input wire clk, // CLK DIVIDIDO
    input wire [15:0] num, // Numero a desplegar en el display
    output wire [6:0] seg,
    output wire [3:0] an
    );

wire [6:0] seg_aux_1, seg_aux_2, seg_aux_3, seg_aux_4;

// Instanciamos los modulos que llevan un numero BCD a los valores corresponidentes en el display
BCDToSevenSeg numero_1 (num[3:0], seg_aux_1);
BCDToSevenSeg numero_2 (num[7:4], seg_aux_2);
BCDToSevenSeg numero_3 (num[11:8], seg_aux_3);
BCDToSevenSeg numero_4 (num[15:12], seg_aux_4);

// Instanciamos el modulo que permite controlar los segmentos y anodos.
SevenSegController salida (clk, 
                            seg_aux_1,
                            seg_aux_2,
                            seg_aux_3, 
                            seg_aux_4,
                            an, 
                            seg
                            );



endmodule