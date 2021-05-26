module source_ram_4_12(
	input wire  ram_clk,
	input wire [383:0] data,
	input wire [2:0] wren,
	input wire [2:0] rden,
	input wire [23:0] address,
	output wire [383:0] q
);
/*+++++++++++++++++++++++++++++++++++
author:qqyk
++ this is the modul for source _ram
++ the data_wide is 128
++ total 12  raw data packets packed into 3 ram 
+++++++++++++++++++++++++++++++++++++*/
source_ram source_ram__0(
	.clock ( ram_clk ),
	.data ( data[127:0] ),
	.wren ( wren[0] ),
	.address ( address[8:0] ),
	.rden ( rden[0] ),
	.q ( q[127:0] )
);
source_ram source_ram__1(
	.clock ( ram_clk ),
	.data ( data[255:128] ),
	.wren ( wren[1] ),
	.address ( address[16:8] ),
	.rden ( rden[1] ),
	.q ( q[255:128] )
);
source_ram source_ram__2(
	.clock ( ram_clk ),
	.data ( data[383:256] ),
	.wren ( wren[2] ),
	.address ( address[24:16] ),
	.rden ( rden[2] ),
	.q ( q[383:256] )
);
endmodule
