###定义一个专门用来写verilog的python 类
##需要定义一个变量来表示当前行逻辑
class verilog:
    def __init__(self,fd):
        self.fd=fd
        self.write_v=write_verilog(fd)
        self.module_announcement_inst=module_announcement(self.write_v)
        self.module_inst_inst=module_inst(self.write_v)
        self.if_begin_inst=if_begin(self.write_v)
        self.else_begin_inst=else_begin(self.write_v)
        self.else_if_begin_inst=else_if_begin(self.write_v)

        self.always_begin_inst=always_begin(self.write_v)
    def always_begin(self,line):
        self.always_begin_inst.load(line)
        return self.always_begin_inst
    def if_begin(self,line):
        self.if_begin_inst.load(line)
        return self.if_begin_inst

    def else_begin(self):
        
        return self.else_begin_inst
    def else_if_begin(self,line):
        self.else_if_begin_inst.load(line)
        return self.else_if_begin_inst
    def module_announcement(self,name,para_list):
        self.module_announcement_inst.load(name,para_list)
        return self.module_announcement_inst
    def module_inst(self,name,name_append,para_list):
        self.module_inst_inst.load(name,name_append,para_list)
        return self.module_inst_inst
class write_verilog:
    def __init__(self,fd):
        self.logic_level=0
        self.fd=fd
    def write_l(self,content):
        self.fd.write("\t"*self.logic_level+content)
        self.fd.write("\n")
    def write_parameter(self,para_list):
        '''
        para_list 内容如下
        ["input"，"reg" ,"[72:0]","sys_clk"]
        
        ("reg","","sys_clk")
        
        '''
        para_number=len(para_list)
        para_type=len(para_list[0])
        for number in range(para_number):
            para=para_list[number]
            
            if para_type==4:
                if number==para_number-1:
                    self.write_l(" ".join(para))
                else:
                    self.write_l(" ".join(para)+",")
            elif para_type==3:
                self.write_l(" ".join(para)+";")
            elif para_type==2:
                if number==para_number-1:
                    self.write_l("."+para[0]+" ( "+para[1]+" )")
                else:
                    self.write_l("."+para[0]+" ( "+para[1]+" ),")

    def write_noblock(self,connect_list):
        for wire_out,wire_in in connect_list:
            self.write_l(wire_out+" <= "+wire_in+";")
    def write_block(self,connect_list):
        for wire_out,wire_in in connect_list:
            self.write_l(wire_out+" = "+wire_in+";")
    def write_wire_connect(self,connect_list):
        for wire_out,wire_in in connect_list:

            self.write_l("assign "+wire_out+" = "+wire_in+";")
    
    def write_comment(self,comment_list):
        '''
        /*+++++++++++++++++++++++++++++++++++
        author_qqyk
        +comment_list_[0]
        +comment_list_[1]
        +comment_list_[2]
        +++++++++++++++++++++++++++++++++++++*/

        '''
        start="/*+++++++++++++++++++++++++++++++++++\nauthor:qqyk"
        end="+++++++++++++++++++++++++++++++++++++*/"
        start_line='++ '
        length=len(comment_list)+2
        fd=self.fd
        for i in range(length):
            if i==0:
                fd.write(start)
            elif (i==length-1):
                fd.write(end)
            else :
                fd.write(start_line)
                fd.write(comment_list[i-1])
            fd.write("\n") 
        
class module_inst:
    def __init__(self,verilog):
        self.verilog=verilog
    def load(self,name,name_append,para_list):
        self.name=name
        self.name_append=name_append
        self.para_list=para_list
        
    def __enter__(self,):
        self.verilog.write_l(self.name+' '+self.name+'_'+self.name_append+"(")
        self.verilog.logic_level+=1
        self.verilog.write_parameter(self.para_list)
        self.verilog.logic_level-=1
        self.verilog.write_l(");")
        
    def __exit__(self,Type, value, traceback):
        pass
class module_announcement:
    def __init__(self,verilog):
        self.verilog=verilog
    def load(self,name,para_list):
        self.name=name
        self.para_list=para_list
        
    def __enter__(self,):
        self.verilog.write_l("module"+" "+self.name+"(")
        self.verilog.logic_level+=1
        self.verilog.write_parameter(self.para_list)
        self.verilog.logic_level-=1
        self.verilog.write_l(");")
        
    def __exit__(self,Type, value, traceback):
        self.verilog.write_l("endmodule")


class if_begin:
    def __init__(self,verilog):
        self.verilog=verilog
    def load(self,line):
        self.line=line
        
    def __enter__(self,):
        self.verilog.write_l(f"if ({self.line})")
        self.verilog.write_l("begin")
        self.verilog.logic_level+=1
        pass
    def __exit__(self,Type, value, traceback):
        self.verilog.logic_level-=1
        self.verilog.write_l("end")
        pass
class always_begin:
    def __init__(self,verilog):
        self.verilog=verilog
    def load(self,line):
        self.line=line
        
    def __enter__(self,):
        self.verilog.write_l(f"always@({self.line})")
        self.verilog.write_l("begin")
        self.verilog.logic_level+=1
        pass
    def __exit__(self,Type, value, traceback):
        self.verilog.logic_level-=1
        self.verilog.write_l("end")
        pass
class else_begin:
    def __init__(self,verilog):
        self.verilog=verilog

        
    def __enter__(self,):
        self.verilog.write_l("else")
        self.verilog.write_l("begin")
        self.verilog.logic_level+=1
        pass
    def __exit__(self,Type, value, traceback):
        self.verilog.logic_level-=1
        self.verilog.write_l("end")
        pass
class else_if_begin:
    def __init__(self,verilog):
        self.verilog=verilog
    def load(self,line):
        self.line=line
        
    def __enter__(self,):
        self.verilog.write_l(f"else if ({self.line})")
        self.verilog.write_l("begin")
        self.verilog.logic_level+=1
        pass
    def __exit__(self,Type, value, traceback):
        self.verilog.logic_level-=1
        self.verilog.write_l("end")
        pass