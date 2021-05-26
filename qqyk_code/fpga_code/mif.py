class mif_quartus:
    def __init__(self,depth,width,file_name):
        self.depth=depth
        self.width=width
        self.file_name=file_name
        if self.file_name[-4:]==".mif":
            self.file_name=file_name
        else:
            self.file_name=file_name+".mif"
    def __write_head(self):
        fd=self.fd
        head=f'''DEPTH = {self.depth};
WIDTH = {self.width};
ADDRESS_RADIX = HEX;
DATA_RADIX = HEX;
CONTENT
BEGIN
'''
        fd.write(head)
    def generate(self,data_iter):
        ###
        ##data is a integer 迭代器
        ###
        with open(self.file_name,"w") as self.fd:
            self.__write_head()
            if len(data_iter)>self.depth:
                raise Exception("so many data we should change the dept")
            for number in range(len(data_iter)):
                data=data_iter[number]
                number_hex=hex(number)[2:]
                data_hex=hex(int(data))[2:]
                if len(data_hex)>self.width:
                    raise Exception("the data is large than rom width")
                self.fd.write(f"{number_hex}\t:\t{data_hex};\n")
            self.fd.write("END;")