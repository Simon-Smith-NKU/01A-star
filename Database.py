STEP = 50
x=[]
y=[]
OPEN=[]
CLOSE=[]
Block = []
begin,end#开始和结束

for i in range(16):
    x.append(-400 + STEP *i)
for i in range(12):
    y.append(300 - STEP*i)

class Node:
    def __init__(self,x,y,cost =0):
        self.x = x
        self.y = y
        self.g = cost


