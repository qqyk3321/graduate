/*+++++++++++++++++++++++++++++++++++
author:qqyk
++ 1+x**1+x**3+x**5+x**14
+++++++++++++++++++++++++++++++++++++*/
module random_14(
	input   clk,
	output  [13:0] degree_random
);
reg [13:0] degree_random_reg=14'd0;
always@(posedge clk)
begin
	rand[13:1] <= rand[12:0];
	rand[0] <= (rand[13]~^rand[4]~^rand[2]~^rand[0])^(rand[0]&rand[1]&rand[2]&rand[3]&rand[4]&rand[5]&rand[6]&rand[7]&rand[8]&rand[9]&rand[10]&rand[11]&rand[12];
end
assign degree_random = degree_random_reg;
endmodule
