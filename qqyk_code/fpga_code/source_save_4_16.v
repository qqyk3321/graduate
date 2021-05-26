module source_save_4_16(
	input wire  sys_clk,
	input wire [7:0] data,
	input wire  data_valid,
	input wire  rst_n,
	output wire [3:0] source_ram_wren,
	output wire [31:0] source_ram_address,
	output wire [511:0] source_ram_data
);
/*+++++++++++++++++++++++++++++++++++
author:qqyk
++ this is the modul for source _ram_save
++ the data_wide is 128
++ total 16  raw data packets packed into 4 ram 
++ input data is 8 bit wide
+++++++++++++++++++++++++++++++++++++*/
reg [1:0] frame;
reg [1:0] ram_number;
reg [7:0] address_reg;
reg [9:0] byte_counter;
reg  en;
reg [127:0] data_reg;
reg  frame_finished;
always@(posedge sys_clk)
begin
	if (!rst_n)
	begin
		frame <= 2'd0;
		ram_number <= 2'b0;
		address <= 15'b0;
		address <= 15'b0;
		address <= 15'b0;
		address <= 15'b0;
	end
end
always@(posedge sys_clk)
begin
	if (!rst_n)
	begin
		byte_counter <= 10'd0;
		en <= 1'b0;
		frame_finished <= 1'b0;
	end
	else if (data_valid)
	begin
		data_reg[7:0] <= data;
		data_reg[127:8] <= data_reg[119:0];
		if (byte_counter==10'd943)
		begin
			frame_finished <= 1'b1;
			en <= 1'b1;
			byte_counter <= 10'd0;
		end
		else if (byte_counter[3:0]==4'd15)
		begin
			frame_finished <= 1'b0;
			en <= 1'b1;
			byte_counter <= byte_counter+1'b1;
		end
		else
		begin
			frame_finished <= 1'b0;
			en <= 1'b0;
			byte_counter <= byte_counter+1'b1;
		end
	end
	else
	begin
		frame_finished <= 1'b0;
		en <= 1'b0;
	end
end
always@(posedge sys_clk)
begin
	if (!rst_n)
	begin
		address_reg <= 8'd0;
		ram_finished <= 1b0;
	end
	else if (en)
	begin
		if (frame_finished)
		begin
			address_reg[7:6] <= address_reg[7:6]+1'd1;
			address_reg[5:0] <= 6'd0;
		end
		else
		begin
			address_reg <= address_reg+1'b1;
		end
	end
end
always@(posedge sys_clk)
begin
	if (!rst_n)
	begin
		ram_number <= 2'd0;
	end
	else if ((frame_finished==1'b1)&&(address_reg[7:6]==2'd3))
	begin
		ram_number <= ram_number+1'b1;
	end
end
assign source_ram_data = {data_reg,data_reg,data_reg,data_reg};
assign source_ram_address = {address_reg,address_reg,address_reg,address_reg};
assign source_ram_wren[0] = (en&&(ram_number==2'd0));
assign source_ram_wren[1] = (en&&(ram_number==2'd1));
assign source_ram_wren[2] = (en&&(ram_number==2'd2));
assign source_ram_wren[3] = (en&&(ram_number==2'd3));
endmodule
