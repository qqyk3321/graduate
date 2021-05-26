module source_save_n_k(
	output wire [2047:0] source_ram_data
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
reg [7:0] address;
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
endmodule
