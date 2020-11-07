from math import sqrt

STEP = 50
x=[]
y=[]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [-1, -1, -1, 0, 1, 1, 1, 0]
OPEN = []
CLOSE = []
Block = []
global begin,end#开始和结束

for i in range(16):
    x.append(-400 + STEP *i)
for i in range(12):
    y.append(300 - STEP*i)

class Node:
    def __init__(self,x,y,cost =0):
        self.x = x
        self.y = y
        self.g = cost

    def cost(self,end):
        self.h = round(10 * sqrt((self.x-end.x)**2+(self.y-end.y)**2))
        self.f = self.g + self.h

    def father(self,x):
        self.father = x

def insertOPEN(x):
    global  OPEN
    i=0
    # insert queue
    for node in OPEN:
        if node.f < x.f:
            i += 1
        else:
            break
    OPEN.insert(i, x)

