/*+++++++++++++++++++++++++++++++++++
author:qqyk
++ random size is 2**18
++ the seed is 3
+++++++++++++++++++++++++++++++++++++*/
module random_90_128_18(
	input wire  clk,
	input wire  rst,
	output wire [7:0] wire_rand,
	output wire  valid
);
reg [17:0] rand;
localparam low=8d'90; 
localparam high=8d'128; 
always@(posedge clk)
begin
	if (rst==1'b1)
	begin
		rand<=3;
	end
	else
	begin
		rand[17:1]<=rand[16:0];
		rand[0]<=(rand[17]~^rand[10])^(rand[0]&rand[1]&rand[2]&rand[3]&rand[4]&rand[5]&rand[6]&rand[7]&rand[8]&rand[9]&rand[10]&rand[11]&rand[12]&rand[13]&rand[14]&rand[15]&rand[16]);
	end
end
assign wire_rand = rand[7:0];
assign valid = (wire_rand>=low)&&(wire_rand<=high);
endmodule
