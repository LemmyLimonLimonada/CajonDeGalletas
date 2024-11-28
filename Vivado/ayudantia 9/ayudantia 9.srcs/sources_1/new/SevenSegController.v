`timescale 1ns / 1ps

module SevenSegController(
    input wire clk,
    input wire [6:0] Y0,Y1,Y2,Y3, // Numeros (en segmentos) que se mostraran en cada display
    output reg [3:0] an,
    output reg [6:0] seg
    );

reg [2:0] contador; // Definimos estado siguiente y actual, respectivamente
  
always @(posedge clk) begin
    contador <= contador + 1;
    
    if (contador == 3'b0) begin
        an <= 4'b1110;
        seg <= Y0;
        end
        
    else if (contador == 3'b1) begin
        an <= 4'b1101;
        seg <= Y1;    
        end
        
    else if (contador == 3'b10) begin
        an <= 4'b1011;
        seg <= Y2;
        end
        
    else if (contador == 3'b11) begin
        contador <= 3'b0;
        an <= 4'b0111;
        seg <= Y3;
        end     
    
end
        
       
endmodule