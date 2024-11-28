`timescale 1ns / 1ps

module Clock_Divider #(integer DIV = 1)(
    input wire clk,
    output reg clk_out
);

    logic [31:0] counter;

    always_ff @(posedge clk) begin
        if (counter == (DIV-1)) begin
            counter <= 0;
            clk_out <= ~clk_out;
        end else begin
            counter <= counter + 1;
        end
    end
endmodule
