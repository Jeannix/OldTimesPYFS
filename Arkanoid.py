from Tkinter import *
import os
bol=[[10,16,-1,1]]#[[x,y,velcidadx,velocidad de y]]#PARA ACTIVAR EL POWER UP(APPEND), SI SE CAE LA BOLA. POP
root = Tk()
ob=["X","-","u"]
m=[]
x=10
y=17
def mov():
    global bol,m,o,p
    for z in range(len(bol)):
        ejex=bol[z][0]#bol[z][0]=10#
        ejey=bol[z][1]#bol[z][1]=16
        m[ejex][ejey]=" "

        if m[ejex-1][ejey]in ob or m[ejex+1][ejey]in ob:#PARA QUE REBOTE X
            if bol[z][2]==-1:#
                bol[z][2]=1#
            else:
                bol[z][2]=-1#
        if m[ejex][ejey-1]in ob or m[ejex][ejey+1]in ob:#PARA QUE REBOTE Y
            if bol[z][3]==-1:#
                bol[z][3]=1#
            else:#
                bol[z][3]=-1#
        m[ejex][ejey]="O"
        bol[z][0]+=bol[z][2]
        bol[z][1]+=bol[z][3]
def upDatepos(dir):
    global m,x,y
    for t in range(-1,2):
        m[x+t][y]=" "
    if dir=="left":
        if x>2:#barrera para que no traspase pared#
            x-=1
    elif dir=="right":
        if x<len(m)-3:
            x+=1
    m[x][y]="-"
    m[x+1][y]="-"
    m[x-1][y]="-"    
def leftKey(event):
    upDatepos("left")
def rightKey(event):
    upDatepos("right")
    
def printMat():
    global m
    for j in range(len(m[0])):
        c=""
        for i in range(len(m)):
            c+= str(m[i][j])
        print c
def task():
    os.system('cls')
    mov()
    printMat()
    root.after(30,task)
    
for i in range(20):
	c=[]
	for j in range(20):
		c.append(" ")
	m.append(c)
for t in range(20):
    m[0][t]="X"
    m[19][t]="X"
    m[t][0]="X"
    m[t][19]="X"
for t in range(-1,2):
    m[x+t][y]="-"
frame = Frame(root, width=10, height=10)
root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)
frame.pack()

root.after(30,task)
root.mainloop()
