/*+++++++++++++++++++++++++++++++++++
author:qqyk
++ inst the 16 ram
++ k ram share the same data,q,rw with special control with ram_select_wr,ram_select_rd,
+++++++++++++++++++++++++++++++++++++*/
module ram_16_source_2port(
	input wire  clk,
	input wire  wr_en,
	input wire [9:0] address_wr,
	input wire [7:0] data,
	input wire  rd_en,
	output wire [7:0] q,
	input wire [9:0] address_rd,
	input wire [3:0] ram_select_wr,
	input wire [3:0] ram_select_rd
);
wire  rden_0;
wire  wren_0;
wire  rden_1;
wire  wren_1;
wire  rden_2;
wire  wren_2;
wire  rden_3;
wire  wren_3;
wire  rden_4;
wire  wren_4;
wire  rden_5;
wire  wren_5;
wire  rden_6;
wire  wren_6;
wire  rden_7;
wire  wren_7;
wire  rden_8;
wire  wren_8;
wire  rden_9;
wire  wren_9;
wire  rden_10;
wire  wren_10;
wire  rden_11;
wire  wren_11;
wire  rden_12;
wire  wren_12;
wire  rden_13;
wire  wren_13;
wire  rden_14;
wire  wren_14;
wire  rden_15;
wire  wren_15;
ram_source_2port ram_source_2port_0
	.rdaddress ( rdaddress ),
	.wraddress ( wraddress ),
	.clock ( clock ),
	.data ( data ),
	.rden ( rden_0 ),
	.wren ( wren_0 ),
	.wren ( wrenq ),
);
ram_source_2port ram_source_2port_1
	.rdaddress ( rdaddress ),
	.wraddress ( wraddress ),
	.clock ( clock ),
	.data ( data ),
	.rden ( rden_1 ),
	.wren ( wren_1 ),
	.wren ( wrenq ),
);
ram_source_2port ram_source_2port_2
	.rdaddress ( rdaddress ),
	.wraddress ( wraddress ),
	.clock ( clock ),
	.data ( data ),
	.rden ( rden_2 ),
	.wren ( wren_2 ),
	.wren ( wrenq ),
);
ram_source_2port ram_source_2port_3
	.rdaddress ( rdaddress ),
	.wraddress ( wraddress ),
	.clock ( clock ),
	.data ( data ),
	.rden ( rden_3 ),
	.wren ( wren_3 ),
	.wren ( wrenq ),
);
ram_source_2port ram_source_2port_4
	.rdaddress ( rdaddress ),
	.wraddress ( wraddress ),
	.clock ( clock ),
	.data ( data ),
	.rden ( rden_4 ),
	.wren ( wren_4 ),
	.wren ( wrenq ),
);
ram_source_2port ram_source_2port_5
	.rdaddress ( rdaddress ),
	.wraddress ( wraddress ),
	.clock ( clock ),
	.data ( data ),
	.rden ( rden_5 ),
	.wren ( wren_5 ),
	.wren ( wrenq ),
);
ram_source_2port ram_source_2port_6
	.rdaddress ( rdaddress ),
	.wraddress ( wraddress ),
	.clock ( clock ),
	.data ( data ),
	.rden ( rden_6 ),
	.wren ( wren_6 ),
	.wren ( wrenq ),
);
ram_source_2port ram_source_2port_7
	.rdaddress ( rdaddress ),
	.wraddress ( wraddress ),
	.clock ( clock ),
	.data ( data ),
	.rden ( rden_7 ),
	.wren ( wren_7 ),
	.wren ( wrenq ),
);
ram_source_2port ram_source_2port_8
	.rdaddress ( rdaddress ),
	.wraddress ( wraddress ),
	.clock ( clock ),
	.data ( data ),
	.rden ( rden_8 ),
	.wren ( wren_8 ),
	.wren ( wrenq ),
);
ram_source_2port ram_source_2port_9
	.rdaddress ( rdaddress ),
	.wraddress ( wraddress ),
	.clock ( clock ),
	.data ( data ),
	.rden ( rden_9 ),
	.wren ( wren_9 ),
	.wren ( wrenq ),
);
ram_source_2port ram_source_2port_10
	.rdaddress ( rdaddress ),
	.wraddress ( wraddress ),
	.clock ( clock ),
	.data ( data ),
	.rden ( rden_10 ),
	.wren ( wren_10 ),
	.wren ( wrenq ),
);
ram_source_2port ram_source_2port_11
	.rdaddress ( rdaddress ),
	.wraddress ( wraddress ),
	.clock ( clock ),
	.data ( data ),
	.rden ( rden_11 ),
	.wren ( wren_11 ),
	.wren ( wrenq ),
);
ram_source_2port ram_source_2port_12
	.rdaddress ( rdaddress ),
	.wraddress ( wraddress ),
	.clock ( clock ),
	.data ( data ),
	.rden ( rden_12 ),
	.wren ( wren_12 ),
	.wren ( wrenq ),
);
ram_source_2port ram_source_2port_13
	.rdaddress ( rdaddress ),
	.wraddress ( wraddress ),
	.clock ( clock ),
	.data ( data ),
	.rden ( rden_13 ),
	.wren ( wren_13 ),
	.wren ( wrenq ),
);
ram_source_2port ram_source_2port_14
	.rdaddress ( rdaddress ),
	.wraddress ( wraddress ),
	.clock ( clock ),
	.data ( data ),
	.rden ( rden_14 ),
	.wren ( wren_14 ),
	.wren ( wrenq ),
);
ram_source_2port ram_source_2port_15
	.rdaddress ( rdaddress ),
	.wraddress ( wraddress ),
	.clock ( clock ),
	.data ( data ),
	.rden ( rden_15 ),
	.wren ( wren_15 ),
	.wren ( wrenq ),
);
assign wren_0 = wr_en&&(ram_select_wr==4'd0);
assign rden_0 = rd_en&&(ram_select_rd==4'd0);
assign wren_1 = wr_en&&(ram_select_wr==4'd1);
assign rden_1 = rd_en&&(ram_select_rd==4'd1);
assign wren_2 = wr_en&&(ram_select_wr==4'd2);
assign rden_2 = rd_en&&(ram_select_rd==4'd2);
assign wren_3 = wr_en&&(ram_select_wr==4'd3);
assign rden_3 = rd_en&&(ram_select_rd==4'd3);
assign wren_4 = wr_en&&(ram_select_wr==4'd4);
assign rden_4 = rd_en&&(ram_select_rd==4'd4);
assign wren_5 = wr_en&&(ram_select_wr==4'd5);
assign rden_5 = rd_en&&(ram_select_rd==4'd5);
assign wren_6 = wr_en&&(ram_select_wr==4'd6);
assign rden_6 = rd_en&&(ram_select_rd==4'd6);
assign wren_7 = wr_en&&(ram_select_wr==4'd7);
assign rden_7 = rd_en&&(ram_select_rd==4'd7);
assign wren_8 = wr_en&&(ram_select_wr==4'd8);
assign rden_8 = rd_en&&(ram_select_rd==4'd8);
assign wren_9 = wr_en&&(ram_select_wr==4'd9);
assign rden_9 = rd_en&&(ram_select_rd==4'd9);
assign wren_10 = wr_en&&(ram_select_wr==4'd10);
assign rden_10 = rd_en&&(ram_select_rd==4'd10);
assign wren_11 = wr_en&&(ram_select_wr==4'd11);
assign rden_11 = rd_en&&(ram_select_rd==4'd11);
assign wren_12 = wr_en&&(ram_select_wr==4'd12);
assign rden_12 = rd_en&&(ram_select_rd==4'd12);
assign wren_13 = wr_en&&(ram_select_wr==4'd13);
assign rden_13 = rd_en&&(ram_select_rd==4'd13);
assign wren_14 = wr_en&&(ram_select_wr==4'd14);
assign rden_14 = rd_en&&(ram_select_rd==4'd14);
assign wren_15 = wr_en&&(ram_select_wr==4'd15);
assign rden_15 = rd_en&&(ram_select_rd==4'd15);
endmodule
