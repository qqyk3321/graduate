module source_ram_4_16(
	input wire  ram_clk,
	input wire [511:0] data,
	input wire [3:0] wren,
	input wire [3:0] rden,
	input wire [31:0] address,
	output wire [511:0] q
);
/*+++++++++++++++++++++++++++++++++++
author:qqyk
++ this is the modul for source _ram
++ the data_wide is 128
++ total 16  raw data packets packed into 4 ram 
+++++++++++++++++++++++++++++++++++++*/
source_ram source_ram__0(
	.clock ( ram_clk ),
	.data ( data[127:0] ),
	.wren ( wren[0] ),
	.address ( address[7:0] ),
	.rden ( rden[0] ),
	.q ( q[127:0] )
);
source_ram source_ram__1(
	.clock ( ram_clk ),
	.data ( data[255:128] ),
	.wren ( wren[1] ),
	.address ( address[15:8] ),
	.rden ( rden[1] ),
	.q ( q[255:128] )
);
source_ram source_ram__2(
	.clock ( ram_clk ),
	.data ( data[383:256] ),
	.wren ( wren[2] ),
	.address ( address[23:16] ),
	.rden ( rden[2] ),
	.q ( q[383:256] )
);
source_ram source_ram__3(
	.clock ( ram_clk ),
	.data ( data[511:384] ),
	.wren ( wren[3] ),
	.address ( address[31:24] ),
	.rden ( rden[3] ),
	.q ( q[511:384] )
);
endmodule
