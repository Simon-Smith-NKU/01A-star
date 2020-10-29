import turtle
import win32api, win32con
from Database import *

redfinished,greenfinished,bluefinished = False,False,False

def squreempty(x,y,color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    for i in range(4):
        turtle.forward(STEP)
        turtle.right(90)

def squarefill(x,y,color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(STEP)
        turtle.right(90)
    turtle.end_fill()

def fillred(x0,y0):
    global x,y,redfinished,end
    if not redfinished:
        tempx = int((x0 + 400)// STEP)
        tempy = int((300-y0)//STEP )
        end = Node(tempx,tempy)
        print(end.x, "\t", end.y)
        squarefill(x[tempx],y[tempy],"red")
        redfinished = True

def fillgreen(x0,y0):
    global x,y,greenfinished,begin
    if not greenfinished:
        tempx = int((x0 + 400)// STEP)
        tempy = int((300-y0)//STEP )
        begin = Node(tempx , tempy)
        print(begin.x,"\t",begin.y,greenfinished)
        squarefill(x[tempx],y[tempy],"green")
        greenfinished = True

def fillblue(x0,y0):
    global x,y
    tempx = int((x0 + 400)// STEP)
    tempy = int((300-y0)//STEP )
    Block.append(Node(tempx,tempy))
    print(Block)
    squarefill(x[tempx],y[tempy],"blue")

def fillyellow(x0,y0):
    global x,y
    tempx = x0
    tempy = y0
    squarefill(x[tempx],y[tempy],"yellow")

def find():
    global begin,end
    for i in range(16):
        for j in range(12):
            squreempty(x[i], y[j], "yellow")

    fillred(end.x , end.y)
    fillgreen(begin.x , begin.y)

    for node in Block:
        fillblue(node.x,node.y)

    for node in CLOSE:
        fillyellow(node.x,node.y)


length = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)  #获得屏幕分辨率X轴
width = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)   #获得屏幕分辨率Y轴
print (width)
print (length)

turtle.setup(800, 600)
turtle.screensize(bg='black')
turtle.tracer(0)

for i in range(16):
    for j in range (12):
        squreempty(x[i],y[j],"yellow")


src = turtle.getscreen()
turtle.ht()
src.update()
src.onclick(fillgreen)#left
src.onclick(fillred,btn = 3)
src.onclick(fillblue ,btn = 2)#mid

#find()
# printer = turtle.Turtle()
# printer.write("from 小宇", align="left", font=("times new roman", 8, "normal"))

turtle.done()