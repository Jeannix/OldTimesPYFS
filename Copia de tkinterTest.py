from Tkinter import *
import os
import random
root = Tk()
m=[]
x=0
y=0
direccion="right"
def upDatepos(dir):
    global m
    global x
    global y
    m[x][y]="_"
    if dir=="left":
        if x>0:
            x-=1
    elif dir=="right":
        if x<len(m)-1:
            x+=1
        else:
            x=0
    elif dir=="up":
        if y>0:
            y-=1
    elif dir=="down":
        if y<len(m[0])-1:
            y+=1
        else:
            y=0
    m[x][y]="o"
    
def leftKey(event):
    global direccion
    direccion="left"

def rightKey(event):
    global direccion
    direccion="right"

def upKey(event):
    global direccion
    direccion="up"
    
def downKey(event):
    global direccion
    direccion="down"

def printMat():
    global m
    for j in range(len(m[0])):
        c=""
        for i in range(len(m)):
            c+= str(m[i][j])
        print c


def task():
    global direccion
    clear = lambda: os.system('cls')
    clear()
    upDatepos(direccion)
    printMat()
    root.after(30, task)  


for i in range(20):
	c=[]
	for j in range(20):
		c.append("_")
	m.append(c)
m[0][0]="o"
	
frame = Frame(root, width=100, height=100)
root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)
root.bind('<Up>', upKey)
root.bind('<Down>', downKey)
frame.pack()

root.after(30, task)
root.mainloop()
