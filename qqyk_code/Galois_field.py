## 有限域计算的类
import numpy as np
'''
伽罗华域运算
'''
primitive_polynomial_dict = {
                            3: 0b1011,
                            4: 0b10011,  # x**4  + x  + 1
                             8: (1 << 8) + 0b11101,  # x**8  + x**4  + x**3 + x**2 + 1
                             5:(1<<5)+0b101,
                             16: (1 << 16) + (1 << 12) + 0b1011,  # x**16 + x**12 + x**3 + x + 1
                             32: (1 << 32) + (1 << 22) + 0b111,  # x**32 + x**22 + x**2 + x + 1
                             64: (1 << 64) + 0b11011  # x**64 + x**4 + x**3 + x + 1
                             }
class GF:
    def __init__(self, w):
        ## gfilog  里面对应[2^0,2^1,2^2,2^3,...,...,...,none]然后对应本源多项式的码字
        ## 
        self.w = w
        self.total = (1 << self.w) 
        self.gflog = []
        self.gfilog = [1] # g(0) = 1
        
        self.make_gf_dict(self.w, self.gflog, self.gfilog)

    def make_gf_dict(self, w, gflog, gfilog):
        gf_element_total_number = 1<<w
        primitive_polynomial = primitive_polynomial_dict[w]#用数字表示的多项式
        for i in range(1, gf_element_total_number -1):
            temp = gfilog[i - 1] << 1  # g(i) = g(i-1) * 2
            if temp & gf_element_total_number:  # 判断溢出
                temp ^= primitive_polynomial  # 异或本原多项式
            #print(i,temp)
            gfilog.append(temp)#
        #这个assert 能校验什么呀，然后为什么要加个none，代表0吗
        
        #gfilog.append(float("-inf"))
        gfilog.append(-1)
        for i in range(gf_element_total_number):
    
            #gflog.append(float("-inf"))
            gflog.append(-1)


        for i in range(0, gf_element_total_number - 1):
            gflog[gfilog[i]] = i
        #print(gflog)
        #print(gfilog)
            
    
    def add(self, a, b):
        #(print(a))
        a=self.check(a)
        b=self.check(b)
        return GF_data((a ^ b))

    def sub(self, a, b):
        a=self.check(a)
        b=self.check(b)
        return GF_data((a ^ b) )

    def mul(self, a, b):##这个就是先看ab对应是2^x,2^y 所以a/b=2^(x-y),a*b=2^(x+y)
        a=self.check(a)
        b=self.check(b)
        return GF_data(self.gfilog[(self.gflog[a] + self.gflog[b]) % (self.total-1)])

    def div(self, a, b):
        a=self.check(a)
        b=self.check(b)
        return GF_data(self.gfilog[(self.gflog[a] - self.gflog[b]) % (self.total-1)])
    def ex(self,a,x):
        a=self.check(a)
        return GF_data(self.gfilog[(self.gflog[a]*x)%(self.total-1)])
    def check(self,a):
        #print("isinstance(a,GF_data)",isinstance(a,GF_data))
        if not isinstance(a,GF_data):
            raise Exception(f"{a} not a GF_data")   
        else :
            return a.num 
class GF_data:
    def __init__(self,num,gf):
        '''
        @parameter num 实际的数值
        、、@parameter self.gf 对应的伽罗华域
        '''
        self.num=num
        self.gf=gf
        
    def __add__(self,b):
        return self.gf.add(self,b)
    def __eq__(self,b):
        return self.num==b.num    
    

    def __sub__(self,b):
        return self.__add__(b)
    
    def __mul__(self,b):
        return self.gf.mul(self,b)
    def __truediv__(self,b):
        return self.gf.div(self,b)
    def __str__(self):
        return f"the value in self.gf({2**self.gf.w}) is {self.num}"
    def __repr__(self):
        subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        return f"{self.num}"+f"{2**self.gf.w}".translate(subscript)
    def chang_prime(self):
        return self.gf.gflog[self.num]
##gf=GF(8)



