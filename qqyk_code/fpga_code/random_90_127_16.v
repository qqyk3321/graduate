/*+++++++++++++++++++++++++++++++++++
author:qqyk
++ random size is 2**16
++ the seed is 3
+++++++++++++++++++++++++++++++++++++*/
module random_90_127_16(
	input wire  clk,
	input wire  rst,
	output wire  valid
);
reg [15:0] rand;
localparam low=7d'90; 
localparam high=7d'127; 
always@(posedge clk)
begin
	if (rst==1'b1)
	begin
		rand<=3;
	end
	else
	begin
		rand[15:1]<=rand[14:0];
		rand[0]<=(rand[15]~^rand[14]~^rand[12]~^rand[3])^(rand[0]&rand[1]&rand[2]&rand[3]&rand[4]&rand[5]&rand[6]&rand[7]&rand[8]&rand[9]&rand[10]&rand[11]&rand[12]&rand[13]&rand[14]);
	end
end
assign wire_rand ={1'b1,rand[5:0]};
assign valid = (wire_rand>=low)&&(wire_rand<=high);
endmodule
