`timescale 1ns / 1ps

module Clock_Divider #(integer DIV = 1)(
    input wire clk,
    output reg clk_out = 1'b0
    );

reg [31:0] contador;

always @(posedge clk) begin
    contador <= contador + 1;
     
    if (contador >= (DIV-1))
        contador <= 32'b0;
        
    clk_out <= (contador < DIV/2)?1'b1:1'b0; 
end

endmodule
