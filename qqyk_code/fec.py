import numpy as np
from  Galois_field_v2 import  *
from Erasure_Channel import *
########时间装饰器
########自动打印时间
#######@func_time
import time
####################

####################
def func_time(func):
    def inner(*args,**kw):
        start_time = time.time()
        r=func(*args,**kw)
        end_time = time.time()
        print('函数运行时间为：',end_time-start_time,'s')
        return r
    return inner

##############################
class FEC:##最大fec父类，包含初始化数据，读入数据，固定大小的数据
    def __init__(self,original_data_number,original_data_length,gf,seed=1):
        ##数据分成original_data_number个数据包，并且产生original_data_length长度的char（8）位的数据
        ##数据是横着放到，是一条一条[1*original_data_length]的数据
        self.original_data_length=original_data_length
        self.original_data_number=original_data_number
        self.original_data_matrix=None
        self.set_seed(seed)
        print("thsi is gf",gf)
        self.gf=gf
        self.decoding_data_matrix=np.zeros((original_data_number,original_data_length),dtype=int)
        self.ec=None
        self.receive_data_matrix=None
    def random_generate_original_data(self):
        
        self.original_data_matrix=np.random.randint(self.gf.total,size=[self.original_data_number,self.original_data_length])  
    def set_seed(self,seed=1):
        np.random.seed(seed)
    def load_original_data_matrix(self,original_data_matrix):
        self.original_data_matrix=original_data_matrix
    def check_decoding(self,decoding_data_matrix):
        
        print("decoding process is ",(self.original_data_matrix==self.decoding_data_matrix).all())
    def set_ec_loss_rate(self,loss_rate):
        self.ec=Erasure_Channel()
        self.ec.set_loss_rate(loss_rate)
    def deliver_encoding_message_on_ec(self):
        self.receive_data_matrix=None
        if (self.ec==None):
            raise Exception("please set the ec first")
        ####
        count=0
        for message in self.encoding_data_matrix[self.original_data_number:]:
            receive_message=self.ec@message
            if receive_message is None:

                continue
            else:
                count+=1
                if self.receive_data_matrix is None:
                    self.receive_data_matrix=receive_message
                else:
                    self.receive_data_matrix=np.vstack((self.receive_data_matrix,receive_message))
        if count<self.original_data_number:
            return False
    def deliver_all_message_on_ec(self):
        ####需要先设置ec
        self.receive_data_matrix=None
        count=0
        if (self.ec==None):
            raise Exception("please set the ec first")
        ####
        for message in self.encoding_data_matrix:
            receive_message=self.ec@message
            if receive_message is None:

                continue
            else:
                count+=1
                if self.receive_data_matrix is None:
                    self.receive_data_matrix=receive_message
                else:
                    self.receive_data_matrix=np.vstack((self.receive_data_matrix,receive_message))
        if count<self.original_data_number:
            return False
        else:
            return True
class ZIGZAG(FEC):
    def __init__(self,original_data_number,original_data_length,encoding_data_number,gf,seed=1):
        self.encoding_data_number=encoding_data_number
        FEC.__init__(self,original_data_number,original_data_length,gf,seed=1)
        self.max_length=self.original_data_length
        self.zigmax=8
    @func_time
    def encoding_time(self):
        self.encoding()
    def encoding(self):
        #####
        ###需要encoding_matrix 需要original_data_matrix  需要
        #####
        self.generate_shiftmatrix()
        self.encoding_data_length=self.original_data_length+self.zigmax
        #self.encoding_data=np.zeros((self.shift_matrix.shape[0],self.original_data_length+self.zigmax),dtype="int")
        if self.encoding_matrix is None:
            raise Exception("do not have encoding_matrix")
        if self.original_data_matrix is None:
            raise Exception("do not have original_data_matrix")
        
        encoding_data_matrix=np.zeros((self.shift_matrix.shape[0],self.encoding_data_length),dtype="int")
        for original_data_number in range(self.original_data_matrix.shape[0]):
            ###每一行都要移位，然后移位的时候是这样的。如果是float("-inf")不操作。如果是一个数字，就移位给相应的代码。

            for encoding_data_number in range(self.shift_matrix.shape[0]):

                #print(encoding_data_number,original_data_number)
                shift_pos=self.shift_matrix[encoding_data_number][original_data_number]
                if shift_pos==-1:
                    continue
                #print("shift_pos",shift_pos)
                #print(self.encoding_data_matrix[encoding_data_number][shift_pos:shift_pos+self.original_data_length])
                #print(self.original_data_matrix[original_data_number][:])
                encoding_data_matrix[encoding_data_number][shift_pos:shift_pos+self.original_data_length]^=self.original_data_matrix[original_data_number][:]
        self.encoding_data_matrix=np.concatenate((encoding_data_matrix,self.shift_matrix),axis=1)
#    def generate_receive_degree_matrix(self, ):
#        ##构建degree matrix和接受矩阵一样大
#        ##degree=1 直接可以还原，degree=2.. 不能直接还原，并且 degree=0没意义跳过
#        ## 我需要知道原始数据包的长度，个数。用于提取位置信息。
#        ##step1 找到receive_encoding_matrix
#        ###再去构造
#        self.receive_encoding_matrix=self.receive_data_matrix[:,-self.original_data_number:]
#        print(self.receive_encoding_matrix.shape)
#        self.receive_degree_matrix=np.zeros((self.receive_data_matrix.shape[0],self.encoding_data_length),dtype="int")
#        #######################################
#        for receive_message in range(self.receive_data_matrix.shape[0]):
#            for original_message in range(self.original_data_number):
#                pos_start=self.receive_encoding_matrix[receive_message][original_message]
#                self.receive_degree_matrix[receive_message][pos_start:pos_start+self.original_data_length]+=1
    def generate_receive_degree_matrix(self, ):
        ##构建degree matrix和接受矩阵一样大
        ##degree=1 直接可以还原，degree=2.. 不能直接还原，并且 degree=0没意义跳过
        ## 我需要知道原始数据包的长度，个数。用于提取位置信息。
        ##step1 找到receive_encoding_matrix
        ###再去构造
        
        self.receive_encoding_matrix=self.receive_data_matrix[:,-self.original_data_number:]
        #print(self.receive_encoding_matrix.shape)
        self.receive_degree_matrix=np.array([[set() for i in range(self.encoding_data_length)] for i in range(self.receive_encoding_matrix.shape[0])])
        #######################################
        for receive_message in range(self.receive_data_matrix.shape[0]):
            for original_message in range(self.original_data_number):
                pos_start=self.receive_encoding_matrix[receive_message][original_message]
                if pos_start<0:
                    continue
                for pos in range(pos_start,pos_start+self.original_data_length):

                    self.receive_degree_matrix[receive_message][pos].add(original_message)
    def set_fd(self,file_name):
        self.fd=open(file_name,"w")
    @func_time
    def decoding_vv1_time(self,fd):
        self.decoding_vv1(fd)
    def decoding_vv1(self,fd):
        ########最普通的做法就是贪心做法，不停的取出有意义的数据，更新，直到全部取完，或者实在没有办法更新。
        ###不停的去操作degreematrix，
        ###
        self.generate_receive_degree_matrix()
        
        ############通过workflag查询有无进一步更新
        workflag=1
        decoding_row_pos=[0]*self.receive_data_matrix.shape[0]
        decoding_ori_pos=[0]*self.original_data_number
        ###########################初始化解码矩阵##########################
        self.decoding_data_matrix=np.zeros((self.original_data_number,self.original_data_length),dtype="int")
        while(workflag):
            ###############每一个循环刚开始都把workflag变成0################
            workflag=0
            ############开始对于decoding_row_pos里面对应的行的pos开始不停的看有没有是1的情况，如果变成0则把pos加1，直到到了self.encoding_data_length
            for row in range(self.receive_data_matrix.shape[0]):
                pos=decoding_row_pos[row]
                if pos==-1:
                    continue

                if len(self.receive_degree_matrix[row][pos])==0:
                    pass
                elif len(self.receive_degree_matrix[row][pos])>1:
                    continue
                elif len(self.receive_degree_matrix[row][pos])==1:
                    ####这里面提供了有效信息，这次提取，下次就用row对应的下一个位置
                    #test.append((row,pos))
                    ori_data_index=self.receive_degree_matrix[row][pos].pop()
                    ori_data_pos=decoding_ori_pos[ori_data_index]
                    ori_data=self.receive_data_matrix[row][pos]
                    self.decoding_data_matrix[ori_data_index][ori_data_pos]=ori_data
                    decoding_ori_pos[ori_data_index]+=1
                    
                    ######更新self.receive_data_matrix,更新self.receive_degree_matrix
                    for rec_index in range(self.receive_data_matrix.shape[0]):
                        if rec_index==row:
                            continue
                        ################找到对应位置
                        rec_data_pos=ori_data_pos+self.receive_encoding_matrix[rec_index][ori_data_index]
                        ################更新self.receive_data_matrix,更新self.receive_degree_matrix
                        if self.receive_encoding_matrix[rec_index][ori_data_index]==-1:
                            continue
                        self.receive_data_matrix[rec_index][rec_data_pos]^=ori_data

                        self.receive_degree_matrix[rec_index][rec_data_pos].remove(ori_data_index)
                        

                ##########更新decoding_row_pos[row]信息
                pos=pos+1
                if pos==self.encoding_data_length:
                    pos=-1
                decoding_row_pos[row]=pos
                workflag=1
            
        ####################
        #####打印一下解码状态
        ####################
        data_check=(self.original_data_matrix==self.decoding_data_matrix)
        success=(data_check).all()
        #print (f"decoding success is {success}")
        success_number=sum(np.array(decoding_ori_pos)==self.original_data_length)
        #print(f"original data number is {self.original_data_number}")
        #print(f"totaol send data number is {self.encoding_data_number+self.original_data_number}")
        #print(f"receive data number is {self.receive_data_matrix.shape[0]}")
        #print(f"encoding rate is {success_number/self.original_data_number}")
        #fd=self.fd
        


        if success==True:
            return True
        else:
            fd.write("##############################\n\n")
            ##fd.write(f"success_number={success_number}\n")
            fd.write(f'self.x_set={self.x_set}\n')
            fd.write(f'self.y_set={self.y_set}\n')
            
            fd.write(f'receive data number={self.receive_data_matrix.shape[0]}\n')
            
            fd.write(f'receive_encoding_matrix=\n{self.receive_encoding_matrix}\n')
            fd.write(f'encoding matrix=\n{self.encoding_matrix}\n')
            fd.write(f'shift matrix=\n{self.shift_matrix}\n')
            return False


    
    def decoding_v2(self):

        pass
    def generate_shiftmatrix(self):
        #######把enconding matrix 转换成shiftmatrix ，并看一下最长的长度。####
        self.shift_matrix=np.zeros((self.encoding_matrix.shape),dtype="int")
        maxx=float("-inf")
        for row in range(self.encoding_matrix.shape[0]):
            minn=float("inf")
            for col in range(self.encoding_matrix.shape[1]):
                self.shift_matrix[row][col]=GF_data(self.encoding_matrix[row][col],self.gf).chang_prime()

                if self.shift_matrix[row][col]!=-1 :
                    minn=min(self.shift_matrix[row][col],minn)
                    maxx=max(self.shift_matrix[row][col],maxx)
            self.shift_matrix[row]=self.shift_matrix[row]-minn
        self.max_length=maxx+self.original_data_length
                


    
    def add_system_matrix(self):
    ### 添加k*k单位矩阵矩阵。
    ### 
        
        system_matrix=np.eye(self.original_data_number,dtype="int")
        #print(system_matrix.shape)
        #print(self.encoding_matrix.shape)
        self.encoding_matrix=np.vstack((system_matrix,self.encoding_matrix))

    
    

###########################################编解码的方法都是固定的#######################
############只是编码矩阵产生的方法不同#############################
class ZIGZAG_Corsi(ZIGZAG):
    def __init__(self,original_data_number,original_data_length,encoding_data_number,gf,seed=1):
        ZIGZAG.__init__(self,original_data_number,original_data_length,encoding_data_number,gf,seed=1)
        
        if (self.original_data_number+self.encoding_data_number)>gf.total:
            raise Exception("the size of the Corsi is small")
        ###因为柯西矩阵是一个固定大小的矩阵，所以有上限。
    def generate_encoding_matrix(self,):
        ###要产生两个矩阵，一个是shiftmatrix（本源元的指数）就是实际代码的操作，一个是encodingmatrix。对应的编码矩阵。
        ###因为最开始产生的是encodingmatrix 然后需要换到shift matrix
        self.encoding_matrix=np.zeros((self.encoding_data_number,self.original_data_number),dtype="int")
        ################

        ###先要产生两个不重叠的在gf域内的集合。然后再产生柯西矩阵。
        ll=np.array(range(self.gf.total))

        np.random.shuffle(ll)
        self.x_set=(ll[0:self.original_data_number])
        self.y_set=(ll[self.original_data_number:self.original_data_number+self.encoding_data_number])
        for row in range(self.encoding_data_number):
            for col in range(self.original_data_number):
                
                a=GF_data(1,self.gf)
                b=GF_data(self.x_set[col],self.gf)
                c=GF_data(self.y_set[row],self.gf)
                d=a/(b+c)
                self.encoding_matrix[row][col]=d.num






        pass
    ######添加系统码，并且
        self.add_system_matrix()
        self.generate_shiftmatrix()
        pass
        
###########################################编解码的方法都是固定的#######################
############只是编码矩阵产生的方法不同#############################
class ZIGZAG_RS(ZIGZAG):
    def __init__(self,original_data_number,original_data_length):
        ZIGZAG.__init__(self, original_data_number, original_data_length)
    def generate_encoding_matrix(self,):
        pass
        self.add_system_matrix()
        self.generate_shiftmatrix()
        pass

#########################################################
#######user_test

#########参数设置和初始化
#gf_w=3##伽罗华域2**gf_w
#k=3#分组中原始数据包数量
#length=1000#数据长度
#r=5#冗余数据包数量
#loss_rate=0.1###丢包率
#gf=GF(gf_w)##初始化伽罗华域
#
#zigzag_corsi=ZIGZAG_Corsi(k,length,r,gf)###初始化   
#zigzag_corsi.set_ec_loss_rate(loss_rate)
############生成编码矩阵
#zigzag_corsi.generate_encoding_matrix()
###############产生初始随机数据，
#zigzag_corsi.random_generate_original_data()
###################把encoding_matrix转换成shiftmatrix
#zigzag_corsi.generate_shiftmatrix()
#zigzag_corsi.random_generate_original_data()
##print(zigzag_corsi.shift_matrix)
##print(aa.original_data_matrix)
###########产生编码数据。
#zigzag_corsi.encoding()
##print(aa.encoding_data_matrix)
#
#
#zigzag_corsi.deliver_all_message_on_ec()
#zigzag_corsi.decoding_vv1()


##########参数设置和初始化
#gf_w=3##伽罗华域2**gf_w
#k=3#分组中原始数据包数量
#length=100#数据长度
#r=5#冗余数据包数量
#loss_rate=0.3###丢包率
#gf=GF(gf_w)##初始化伽罗华域
#file_name="log_decode"
#zigzag_corsi=ZIGZAG_Corsi(k,length,r,gf)###初始化   
#zigzag_corsi.set_ec_loss_rate(loss_rate)
############生成编码矩阵
##zigzag_corsi.generate_encoding_matrix()
###############产生初始随机数据，
#zigzag_corsi.random_generate_original_data()
#zigzag_corsi.set_fd(file_name)
###################把encoding_matrix转换成shiftmatrix
##zigzag_corsi.generate_shiftmatrix()
##zigzag_corsi.random_generate_original_data()
##print(zigzag_corsi.shift_matrix)
##print(aa.original_data_matrix)
###########产生编码数据。
#success=0
#for times in range(10000):
#    
#    zigzag_corsi.generate_encoding_matrix()
#    zigzag_corsi.encoding()
#    #print(aa.encoding_data_matrix)
#
#
##    decodeable=zigzag_corsi.deliver_encoding_message_on_ec()
##    if not decodeable:
##        continue
##    r=zigzag_corsi.decoding_vv1()
##    #print(r)
##    success+=r
###print(success)   
##
#
#    
##########参数设置和初始化
#gf_w=3##伽罗华域2**gf_w
#k=3#分组中原始数据包数量
#length=100#数据长度
#r=4#冗余数据包数量
#loss_rate=0.6###丢包率
#gf=GF(gf_w)##初始化伽罗华域
#file_name="log_decode"
#zigzag_corsi=ZIGZAG_Corsi(k,length,r,gf)###初始化   
#zigzag_corsi.set_ec_loss_rate(loss_rate)
############生成编码矩阵
##zigzag_corsi.generate_encoding_matrix()
###############产生初始随机数据，
#zigzag_corsi.random_generate_original_data()
#zigzag_corsi.set_fd(file_name)
###################把encoding_matrix转换成shiftmatrix
##zigzag_corsi.generate_shiftmatrix()
##zigzag_corsi.random_generate_original_data()
##print(zigzag_corsi.shift_matrix)
##print(aa.original_data_matrix)
###########产生编码数据。
#
#success=0
#with open(file_name,"w") as fd:
#    for times in range(10000):
#        
#        zigzag_corsi.generate_encoding_matrix()
#        zigzag_corsi.encoding()
#        #print(aa.encoding_data_matrix)
#
#
#        decodeable=zigzag_corsi.deliver_all_message_on_ec()
#        if not decodeable:
#            continue
#        r=zigzag_corsi.decoding_vv1(fd)
#        #print(r)
#        success+=r
#print(success)   