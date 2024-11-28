`timescale 1ns / 1ps

module SevenSegController(
    input wire clk,
    input wire [6:0] Y0,Y1,
    output reg [3:0] an,
    output reg [6:0] seg
    );

reg [2:0] contador; 
  
always @(posedge clk) begin
    contador <= contador + 1;
    
    if (contador == 3'b0) begin
        an <= 4'b1110;
        seg <= Y0;
        end
        
    else if (contador == 3'b1) begin
        an <= 4'b1011;
        seg <= Y1;    
        end
             
    
end
        
       
endmodule
