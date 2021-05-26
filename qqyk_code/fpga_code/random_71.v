/*+++++++++++++++++++++++++++++++++++
author:qqyk
++ 1+x**65+x**71
+++++++++++++++++++++++++++++++++++++*/
module random_71(
	input   clk,
	output  [70:0] random
);
reg [70:0] rand=71'd0;
always@(posedge clk)
begin
	rand[70:1] <= rand[69:0];
	rand[0] <= (rand[70]~^rand[64])^(rand[0]&rand[1]&rand[2]&rand[3]&rand[4]&rand[5]&rand[6]&rand[7]&rand[8]&rand[9]&rand[10]&rand[11]&rand[12]&rand[13]&rand[14]&rand[15]&rand[16]&rand[17]&rand[18]&rand[19]&rand[20]&rand[21]&rand[22]&rand[23]&rand[24]&rand[25]&rand[26]&rand[27]&rand[28]&rand[29]&rand[30]&rand[31]&rand[32]&rand[33]&rand[34]&rand[35]&rand[36]&rand[37]&rand[38]&rand[39]&rand[40]&rand[41]&rand[42]&rand[43]&rand[44]&rand[45]&rand[46]&rand[47]&rand[48]&rand[49]&rand[50]&rand[51]&rand[52]&rand[53]&rand[54]&rand[55]&rand[56]&rand[57]&rand[58]&rand[59]&rand[60]&rand[61]&rand[62]&rand[63]&rand[64]&rand[65]&rand[66]&rand[67]&rand[68]&rand[69]);
end
assign random = rand;
endmodule
