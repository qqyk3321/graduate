/*+++++++++++++++++++++++++++++++++++
author:qqyk
++ this is 4 fifo inst 
++ fifo is 8bit-wide and 1024-deep with aclr sys with wrclk
+++++++++++++++++++++++++++++++++++++*/
module tx_fifo_4(
	input wire  wrclk,
	input wire [3:0] wrreq,
	input wire [31:0] data,
	output wire [3:0] wrempty,
	input wire [3:0] rdreq,
	input wire  rd_clk,
	output wire [31:0] q,
	output wire [39:0] rdusedw,
	input wire [3:0] aclr
);
tx_fifo tx_fifo__0(
	.aclr ( aclr[0] ),
	.data ( data[7:0] ),
	.rdclk ( rdclk ),
	.rdreq ( rdreq[0] ),
	.wrclk ( wrclk ),
	.wrreq ( wrreq[0] ),
	.q ( q[7:0] ),
	.rdusedw ( rdusedw[9:0] ),
	.wrempty ( wrempty[0] )
);
tx_fifo tx_fifo__1(
	.aclr ( aclr[1] ),
	.data ( data[15:8] ),
	.rdclk ( rdclk ),
	.rdreq ( rdreq[1] ),
	.wrclk ( wrclk ),
	.wrreq ( wrreq[1] ),
	.q ( q[15:8] ),
	.rdusedw ( rdusedw[19:10] ),
	.wrempty ( wrempty[1] )
);
tx_fifo tx_fifo__2(
	.aclr ( aclr[2] ),
	.data ( data[23:16] ),
	.rdclk ( rdclk ),
	.rdreq ( rdreq[2] ),
	.wrclk ( wrclk ),
	.wrreq ( wrreq[2] ),
	.q ( q[23:16] ),
	.rdusedw ( rdusedw[29:20] ),
	.wrempty ( wrempty[2] )
);
tx_fifo tx_fifo__3(
	.aclr ( aclr[3] ),
	.data ( data[31:24] ),
	.rdclk ( rdclk ),
	.rdreq ( rdreq[3] ),
	.wrclk ( wrclk ),
	.wrreq ( wrreq[3] ),
	.q ( q[31:24] ),
	.rdusedw ( rdusedw[39:30] ),
	.wrempty ( wrempty[3] )
);
endmodule
