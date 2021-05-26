from random_dic import *
from write_verilog import *
class generate_random:
    def __init__(self,w=3,seed=0):
        '''
        parameter @w : 2**w random or w_bit random
        parameeter @seed: init value
        '''
        self.w=w
        self.lst=[]
        self.seed=seed
        pass
        
    
    def generate_verilog(self,):
        '''
        generate random_{self.w}.v 
        '''
        file_name=f"random_{self.w}.v"
        seed=self.seed
        w=self.w
        with open(file_name,"w") as fd:
            gv=verilog(fd)
           
            comment_list=[]
            comment_list+=[f"random size is 2**{self.w}"]
            comment_list+=[f"the seed is {self.seed}"]
            comment_list=['+'.join(["1","+".join([f"x**{i+1}" for i in random_dic[self.w]][::-1])])]
            gv.write_v.write_comment(comment_list)
            module_name=f"random_{self.w}"
            para_list=[]
            para_list+=[("input","","","clk")]
            para_list+=[("output","",f"[{self.w-1}:0]","random")]
            

            with gv.module_announcement(module_name,para_list):
                para_list=[]
                para_list+=[("reg",f"[{self.w-1}:0]",f"rand={self.w}'d{seed}")]
                gv.write_v.write_parameter(para_list)
                with gv.always_begin("posedge clk"):
                    eq_list=[]
                    eq_list+=[(f"rand[{self.w-1}:1]",f"rand[{self.w-2}:0]")]
                    eq_list+=[("rand[0]","("+"~^".join(["rand["+str(i)+"]" for i in random_dic[self.w]])+")"+"^"+"("+"&".join(["rand["+str(i) +"]" for i in range(self.w-1)])+')')]
                    gv.write_v.write_noblock(eq_list)
                eq_list=[]
                eq_list+=[("random","rand")]
                gv.write_v.write_wire_connect(eq_list)
