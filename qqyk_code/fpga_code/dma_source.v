/*+++++++++++++++++++++++++++++++++++
author:qqyk
++ the number of ram is 16
++ this is the ram wr interface with the ram  a little bit like dma
+++++++++++++++++++++++++++++++++++++*/
module source_dma_16(
	input wire  clk,
	input wire  rst,
	input wire  data_load_en,
	input wire [7:0] data,
	input wire  control_en,
	output   ram_wr_en,
	output reg [9:0] ram_address,
	output reg [3:0] ram_selcet,
	output  [7:0] data_ram
);
always@(posedge clk)
begin
	if (rst)
	begin
		ram_selcet <= 4'd0;
		ram_address <= 10'd0;
	end
	if (ram_wr_en)
	begin
		if (ram_address<=10'd939)
		begin
			ram_selcet <= ram_selcet+1'b1;
			ram_address <= 10'd0;
		end
		else
		begin
			ram_address <= ram_address+1'b1;
		end
	end
end
assign ram_wr_en = data_load_en&&control_en;
assign ram_data = data;
endmodule
