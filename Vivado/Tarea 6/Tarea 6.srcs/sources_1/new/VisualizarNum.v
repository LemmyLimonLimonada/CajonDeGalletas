`timescale 1ns / 1ps

module VisualizarNum(
    input logic clk, 
    input logic [1:0] p_state,
    input logic [1:0] g_state,
    output logic [6:0] seg,
    output logic [3:0] an
);

    logic [6:0] seg_aux_1, seg_aux_2, seg_aux_3, seg_aux_4;

    JuegoExe numero_1 (p_state, seg_aux_1);
    NumJugador numero_2 (p_state, g_state, seg_aux_2);
    DineroPozo numero_3 (p_state, g_state, seg_aux_3);
    Ganador numero_4 (p_state, g_state, seg_aux_4);

    SevenSegController salida (clk, 
                               seg_aux_1,
                               seg_aux_2,
                               seg_aux_3, 
                               seg_aux_4,
                               an, 
                               seg
                               );

endmodule
