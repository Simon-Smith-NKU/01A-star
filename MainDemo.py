import turtle
from tkinter import messagebox
import win32api, win32con
from Database import *
from time import sleep

redfinished, greenfinished, bluefinished = False, False, False
global src , printer

def main():
    global src,printer
    length = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)  # 获得屏幕分辨率X轴
    width = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)  # 获得屏幕分辨率Y轴
    print(width)
    print(length)

    # 0<=x<=15,0<=y<=11
    turtle.setup(800, 600)
    turtle.screensize(bg='black')
    turtle.tracer(0)

    for i in range(16):
        for j in range(12):
            squreempty(x[i], y[j], "yellow")
    turtle.update()
    turtle.ht()
    printer = turtle.Turtle()  # 写字
    printer.ht()

    src = turtle.getscreen()  # 事件
    src.update()
    src.onclick(fillgreen)  # left
    src.onclick(fillred, btn=3)
    src.onclick(fillblue, btn=2)  # mid

    turtle.listen()
    turtle.onkey(lambda: SearchBegin(), "space")
    turtle.mainloop()

def squreempty(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    for i in range(4):
        turtle.forward(STEP)
        turtle.right(90)


def squarefill(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(STEP)
        turtle.right(90)
    turtle.end_fill()


def fillred(x0, y0):
    global x, y, redfinished, end
    if not redfinished:
        tempx = int((x0 + 400) // STEP)
        tempy = int((300 - y0) // STEP)
        end = Node(tempx, tempy)
        print(end.x, "\t", end.y)
        squarefill(x[tempx], y[tempy], "red")
        redfinished = True
        turtle.update()


def fillgreen(x0, y0):
    global x, y, greenfinished, begin
    if not greenfinished:
        tempx = int((x0 + 400) // STEP)
        tempy = int((300 - y0) // STEP)
        begin = Node(tempx, tempy)
        print(begin.x, "\t", begin.y)
        squarefill(x[tempx], y[tempy], "green")
        greenfinished = True
        turtle.update()


def fillblue(x0, y0):
    global x, y
    tempx = int((x0 + 400) // STEP)
    tempy = int((300 - y0) // STEP)
    Block.append(Node(tempx, tempy))
    # print(Block)
    squarefill(x[tempx], y[tempy], "blue")
    turtle.update()


def fillyellow(x0, y0):
    global x, y
    tempx = x0
    tempy = y0
    squarefill(x[tempx], y[tempy], "yellow")


def fillpink(x0, y0):
    global x, y, STEP
    tempx = x[x0] + STEP / 2
    tempy = y[y0] - STEP
    turtle.penup()
    turtle.goto(tempx, tempy)
    turtle.pendown()
    turtle.color("pink")
    turtle.begin_fill()
    turtle.circle(25, 360)
    turtle.end_fill()


def build_map():
    global begin, end, redfinished, greenfinished,Block
    turtle.clear()
    for i in range(16):
        for j in range(12):
            squreempty(x[i], y[j], "yellow")

    for node in Block:
        fillblue(node.x, node.y)

    for node in CLOSE:
        fillyellow(node.x, node.y)

    if redfinished:
        fillred(end.x, end.y)
    if greenfinished:
        fillgreen(begin.x, begin.y)

def SearchBegin():
    global bluefinished, begin
    bluefinished = True
    begin.cost(end)
    find(begin)

def SearchEnd_notfind():
    messagebox.showinfo(title="Result", message="Not found!")
    return

def SearchEnd_find():
    global end
    cost_write(end)
    return

def cost_write(input):
    global printer, begin, end
    while  input != begin:
        fillpink(input.x,input.y)
        printer.penup()
        printer.goto(x[input.x] + STEP, y[input.y] - STEP)
        printer.pendown()
        printer.write("g=" + str(input.g) + "\nh=" + str(input.h) + "\nf=" + str(input.f), \
                      align="right", font=("times new roman", 8, "normal"))
        cost_write(input.father)
    return

def inBlock(x,y):
    # global Block
    result = False
    for node in Block:
        if x == node.x and y == node.y:
            result = True
    return result

def find(source):
    #build_map()
    # 生成OPEN
    for i in range(8):
        # 0<=x<=15,0<=y<=11
        tempx = source.x + dx[i]
        tempy = source.y + dy[i]
        # 判断不得斜穿
        legal = True
        if i in [0,2,4,6]:
            if 0 == i :
                legal = (not inBlock(tempx,tempy)) and \
                        (not inBlock(source.x + dx[7],source.y + dy[7]) or \
                          not inBlock(source.x + dx[1],source.y + dy[1]))
            if 2 == i:
                legal = (not inBlock(tempx, tempy)) and \
                        (not inBlock(source.x + dx[3], source.y + dy[3]) or \
                         not inBlock(source.x + dx[1], source.y + dy[1]))
            if 4 == i:
                legal = (not inBlock(tempx, tempy)) and \
                        (not inBlock(source.x + dx[3], source.y + dy[3]) or \
                         not inBlock(source.x + dx[5], source.y + dy[5]))
            if 6 == i:
                legal = (not inBlock(tempx, tempy)) and 、
                        (not inBlock(source.x + dx[7], source.y + dy[7]) or \
                         not inBlock(source.x + dx[5], source.y + dy[5]))
        else:
            legal = inBlock(tempx,tempy)
        if legal:
            if tempx == end.x and tempy == end.y:
                end.father(source)
                if 0 == i % 2:
                    end.g = source.g + 14
                else:
                    end.g = source.g + 10
                end.cost(end)
                SearchEnd_find()
            elif tempx < 16 and tempx >= 0 and tempy < 12 and tempy >= 0:
                if 0 == i % 2:
                    tempnode = Node(tempx, tempy, source.g + 14)
                else:
                    tempnode = Node(tempx, tempy, source.g + 10)
                tempnode.cost(end)
                tempnode.father(source)
                # 更新open估价
                found = False
                OPENnum = 0
                for node in OPEN:
                    if node.x == tempnode.x \
                            and node.y == tempnode.y:
                        found = True
                        if node.f > tempnode.f:
                            OPEN.pop(OPENnum)
                            insertOPEN(tempnode)
                            fillyellow(tempx, tempy)
                            turtle.update()
                            break
                        else:
                            break
                    OPENnum += 1
                # 更新close估价
                CLOSEnum = 0
                for node in CLOSE:
                    if node.x == tempnode.x \
                            and node.y == tempnode.y:
                        found = True
                        if node.f > tempnode.f:
                            CLOSE.pop(CLOSEnum)
                            CLOSE.append(tempnode)
                            insertOPEN(tempnode)
                            fillyellow(tempx, tempy)
                            turtle.update()
                            break
                        else:
                            break
                    CLOSEnum += 1
                if not found:
                    insertOPEN(tempnode)
                    fillyellow(tempx, tempy)
                    turtle.update()
        # 利用CLOSE(f升序)
        CLOSE.append(source)


    if OPEN:
        nextnode = OPEN.pop(0)
        sleep(0.1)
        find(nextnode)
    else:
        SearchEnd_notfind()


if __name__ == "__main__":
    main()
