/*+++++++++++++++++++++++++++++++++++
author:qqyk
++ simple_degree generate，包含random71bit，这个位数是我随意定义的，
++ 初始化，利用定义reg的时候自带的
++ 包含a single 10bit rom or ram,9-bit wid
+++++++++++++++++++++++++++++++++++++*/
module simple_degree_16(
	input   clk,
	output  [8:0] degree_random,
	output   degree_valid
);
wire [70:0] random;
wire [9:0] address_rom;
wire [8:0] q_rom;
random_71 random_71_inst(
	.clk ( clk ),
	.degree_random ( random )
);
simple_degree_rom simple_degree_rom_inst(
	.address ( address_rom ),
	.clock ( clk ),
	.q ( q_rom )
);
assign address_rom = random[9:0];
assign degree_valid = 1'b1;
assign degree_random = q_rom;
endmodule
