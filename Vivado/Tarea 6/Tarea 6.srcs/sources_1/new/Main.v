`timescale 1ns / 1ps

module Main(
    input logic clk,
    input logic [1:0] sw,
    input logic btnR, btnL, btnU, // btnR -> Confirmación, btnL -> Empezar, btnU -> Reset
    output logic [6:0] seg,  
    output logic [3:0] an
);

    typedef enum logic [1:0] {M0, M1, M2} p_states;
    typedef enum logic [1:0] {S0, S1, S2, S3} g_states;
    p_states p_state, p_nextstate;
    g_states g_state, g_nextstate;

    parameter DIV = 100_000;
    wire slw_clk;
    logic fin;
    logic [1:0] j_exe, n_jug, d_poz, g_jug;

    Clock_Divider #(DIV) Clock_Divider_inst (clk, slw_clk);

    // Sincronizacion de btnR
    logic btnR_sync, btnR_sync2;

    always_ff @(posedge clk) begin
        btnR_sync <= btnR;
        btnR_sync2 <= btnR_sync;
    end

    // Estados de jugador
    always_ff @(posedge btnR_sync2 or posedge btnU or posedge btnL)
        if (btnU) p_state <= M0;
        else if (btnL) p_state <= M1;
        else p_state <= p_nextstate;

    always_comb begin
        case (p_state)
            M0: p_nextstate = M0;
            M1: if (fin) p_nextstate = M0;
                else if (btnR_sync2) p_nextstate = M2;
            M2: if (fin) p_nextstate = M0;
                else if (btnR_sync2) p_nextstate = M1;
            default: p_nextstate = M0;
        endcase
    end

    // Estados de partida
    always_ff @(posedge btnR_sync2 or posedge btnU or posedge btnL)
        if (btnU) g_state <= S0;
        else if (btnL) g_state <= S2;
        else if (sw[1] & sw[0] & btnR_sync2) g_state <= S0;
        else g_state <= g_nextstate;

    always_comb begin
        case (g_state)
            S0: if (btnL) g_nextstate = S2;
                else g_nextstate = S0;
            S1: if (sw[1] & btnR) g_nextstate = S0;
                else if (~sw[1] & sw[0] & btnR) g_nextstate = S2;
                else g_nextstate = S1;
            S2: if (sw[1] & ~sw[0] & btnR) g_nextstate = S1;
                else if (~sw[1] & sw[0] & btnR) g_nextstate = S3;
                else g_nextstate = S2;
            S3: if (sw[1] & ~sw[0] & btnR) g_nextstate = S2;
                else if (~sw[1] & sw[0] & btnR) g_nextstate = S0;
                else g_nextstate = S3;
            default: g_nextstate = S0;
        endcase
    end

    assign fin = (g_state == S0);
    VisualizarNum VisualizarNum_inst (slw_clk, p_state, g_state, seg, an);

endmodule
