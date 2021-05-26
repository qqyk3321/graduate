from math import *
import random
import bisect
import struct
class RSD:
    def __init__(self,k,knpPrecision=20,file_name="A_lt"):
        '''里面使用到的参数，都是根据luby的一个专利文档来de 
        该文档仅仅只有一个参数，剩下的参数，基本上都是来源于经验。
        '''
        self.file_name=file_name
        ##load the parameter 
        

        self.k=k
        ## the precision bit 
        self.knpPrecision=knpPrecision
    def patent_rsd(self,):
        k=self.k
        self.__parameter_init()
        ##R1:start_ripple size 
        self.R1=int(self.kdSFactor*sqrt(self.k))
        ##R2:ripple target size
        self.R2=int(self.knRAdd+self.kdRFactor*k**0.25)
        ### 可能出现不了3中情况，因为R1和R2的选择。
        
        r_kinds=int(self.k/self.R2)-2
        if r_kinds<1:
            r_kinds=1
            raise Exception("not good")
        elif r_kinds>self.k:
            r_kinds=K
            raise Exception("not good")
        
        tail_kinds=1
        tail=self.R2
        while(tail>1):
            tail=tail//2
            tail_kinds+=1

        kinds=tail_kinds+r_kinds
        if kinds>k:
            tail_kinds=k-r_kinds
            kinds=k
        
        ##############
        kind_weight=[0]*kinds
        kind_density=[0]*kinds
        kind_frac=[0]*kinds
        ##weight 1
        kind_weight[0]=1
        kind_frac[0]=self.R1/self.k
        ##
        for i in range(1,r_kinds):
            kind_frac[i]=kind_frac[i-1]+1/(i*(i+1)*(1-(i+1)*self.R2/self.k))
            kind_weight[i]=i+1
        n_power=1
        for i in range(tail_kinds):
            n_power=n_power*2
        print(n_power>self.R2)
        j=2
        for i in range(r_kinds,kinds):
            kind_frac[i]=kind_frac[i-1]+self.fdTFactor*n_power/(j*k)
            kind_weight[i]=int(j*k/n_power)
            j=j*2

        ###精确度问题20位精确度
        modulus=1<<self.knpPrecision
        for i in range(kinds):
            kind_density[i]=int(kind_frac[i]/kind_frac[-1]*modulus)
        ######最大重量
        self.max_weight=max(kind_weight)
        #print(kind_weight)
        #### 计算平均
        sum=kind_weight[0]*kind_density[0]
        for i in range(1,kinds):
            sum=sum+(kind_weight[i]*(kind_density[i]-kind_density[i-1]))
        self.average_weight=sum/modulus
        
        self.kind_density=kind_density
        self.kind_weight=kind_weight
        self.file_name+="_patent"
    def __parameter_init(self):
        '''
        从那个文章里面作者提供的参数,
        '''
        self.knRAdd=2
        self.kdRFactor=2.0

        self.kdSFactor=1.4

        self.fdTFactor=1.6
        
    def lt_rsd(self,c=0.2,theta=0.05):
        
        '''
        在lt_isd的基础上叠加一个，修正版本，然后再归一化。
        先进性lt编码。
        @parameter c a constant >0
        @parameter theta fail probility

        '''
        k=self.k
        R=c*log(k/theta)*(k**0.5)
        mid=int(k/R)
        if (mid==1 or mid>k):
            raise Exception("sth is wrong")
        kinds=self.k
        kind_weight=[0]*kinds
        kind_frac=[0]*kinds
        kind_density=[0]*kinds
        modulus=1<<self.knpPrecision
        ### 定义概率
        for i in range(k):
            kind_weight[i]=i+1
            if i==0:
                kind_frac[i]=1/self.k+R/((i+1)*k)
            elif i<=mid-1:
                kind_frac[i]=kind_frac[i-1]+1/(i*(i+1))+R/((i+1)*k)
            elif i==mid:
                kind_frac[i]=kind_frac[i-1]+1/(i*(i+1))+R*log(R/theta)/k
            else:
                kind_frac[i]=kind_frac[i-1]+1/(i*(i+1))+0
            
        modulus=1<<self.knpPrecision
        for i in range(kinds):
            kind_density[i]=int(kind_frac[i]/kind_frac[-1]*modulus)
        ######最大重量
        self.max_weight=max(kind_weight)
        #print(kind_weight)
        #### 计算平均
        sum=kind_weight[0]*kind_density[0]
        for i in range(1,kinds):
            sum=sum+(kind_weight[i]*(kind_density[i]-kind_density[i-1]))
        self.average_weight=sum/modulus
        
        self.kind_density=kind_density
        self.kind_weight=kind_weight
        self.file_name+="_rsd"
        pass
    def lt_isd(self,):
        pass
        k=self.k
        kinds=self.k
        kind_weight=[0]*kinds
        kind_frac=[0]*kinds
        kind_density=[0]*kinds
        modulus=1<<self.knpPrecision
        ### 定义概率
        for i in range(k):
            kind_weight[i]=i+1
            if i==0:
                kind_frac[i]=1/self.k
            else:
                kind_frac[i]=kind_frac[i-1]+1/(i*(i+1))
            
        modulus=1<<self.knpPrecision
        for i in range(kinds):
            kind_density[i]=int(kind_frac[i]/kind_frac[-1]*modulus)
        ######最大重量
        self.max_weight=max(kind_weight)
        #print(kind_weight)
        #### 计算平均
        sum=kind_weight[0]*kind_density[0]
        for i in range(1,kinds):
            sum=sum+(kind_weight[i]*(kind_density[i]-kind_density[i-1]))
        self.average_weight=sum/modulus
        
        self.kind_density=kind_density
        self.kind_weight=kind_weight
        self.file_name+="_isd"

        
    def generate_random_v1(self,seed=10,n=None):
        '''
        generate verilog ,mif,还有编码矩阵A的二进制文件。
        '''                
        #step one generate  A the size of A is n,k
        #理论上来说n可以是任意的数值，为了仿真方便，
        #如果不说默认
        k=self.k
        if not n:
            n=floor(k+log(k))
        '''
        生成 随机数，然后看落在哪个范围内，使用相应的weight，然后再随机产生一系列的随机数，然后再把相应的
        位置1，把这个最后写进文件里面。 

        '''
        random.seed(seed)
        with open(self.file_name,"wb") as fd:
            ##p 是比k大的一个质数
            p=k
            while (1):
                for i in range (2,int(p**0.5+1)):
                    if p%i==0:
                        p=p+1
                        break
                break
            for _ in range(n):
                print("new_message")
                random_desity=random.randint(0,self.kind_density[-1])
                degree=self.kind_weight[bisect.bisect_left(self.kind_density,random_desity)]
                

                ###随机选择数字
                
                x=random.randint(1,p-1)
                y=random.randint(0,p-1)
                summ=y
                count=0
                new_line=[0]*k
                while (count<degree):

                    if summ>=k:
                        summ=(summ+x)%p
                        continue
                    print(f"summ={summ}")
                    new_line[summ]=1
                    summ=(summ+x)%p
                    count+=1
                print(f"count={count}")
                for i in range(floor(k/8)):
                    ##转换成二进制然后保存再文件再文件中。
                    val=0
                    for j in range(8):
                        
                        now=i*8+j
                        if now>=k or new_line[now]==0:
                            continue
                        else:
                            
                            
                            val=val|(1<<(7-j))
                    print(f"val={val}")
                    fd.write(struct.pack("B",val))
        
    def generate_mif_v1(self,):
        file_name=self.file_name+"v1"+"mif"
        pass
        '''
        方法1需要 较少的ram，因为连续相同的ram并没有存，利用地址映射，也就是一个硬件二分，实现的地址映射。
        需要一个precesion×floor（log2（kinds））的lut也是一个很大的开销。
        需要 floor（log2（kinds））×floor（log2（k））
        方法2 把得到的density作为寻址，也就是需要precesion×floor(log2(k))
        '''
        pass
