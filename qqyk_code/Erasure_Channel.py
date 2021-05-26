### 除删信道###
import random
class Erasure_Channel:
    '''
    精度是0.1
    '''
    def __init__(self,):
        self.rate=0
        self.range=list(range(10))

    def __matmul__(self,message):
        return self.message_delivery(message)
    def set_seed(self,seed):
        random.seed(seed)
    def message_delivery(self,message):
        now=random.choice(self.range)
        #print(now)
        if now<self.loss_rate:
            return None
        else:
            return message
    def set_loss_rate(self,loss_rate):
        self.loss_rate=loss_rate*10
        #print("self.rate=",self.rate)