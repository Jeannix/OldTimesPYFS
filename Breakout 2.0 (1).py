from Tkinter import *
from random import *
import os
bol=[[10,15,1,1]]#[[x,y,velcidadx,velocidad de y]]#PARA ACTIVAR EL POWER UP(APPEND), SI SE CAE LA BOLA. POP
powerups=[]
root = Tk()
blon=[]
m=[]
x,y,xb,yb=10,16,0,4
tim=70
triplica=0
lvup=0
bolens=0
bar=1# con dos es el poder grande, cambialo a 1 y entenderas, para que sea pequenio cambia a bar por -1

def triplicar():
    global m,bol
    asd=randrange(1,18)
    dx=randrange(8,15)
    a=1
    while a==0:
        bol.append([asd,dx,-1,1])
        bol.append([asd,dx,-1,1])
        a-=1
    
def barra():
    global bar
    b=randrange(0,2)
    if b==0:
        bar=2
    if b==1:
        bar=-1
def disparar():
    print "Disparando"
def poderes():
    a=randrange(0,3)
    if a==0:
        barra()
    elif a==1:
        disparar()
    elif a==2:
        triplicar()
def probpoderes():
    b=random()
    if b<=0.3:
        poderes()     
def gameover():
    global tim,bol
    tim+=1000000
    print "PERDISTE"
def lv1():
    global m,blon
    for t in range(20):
        m[0][t]="X"
        m[19][t]="X"
        m[t][0]="X"
        m[t][19]="X"
    for w in range(1,19):
        blon.append([w,1])
        blon.append([w,2])
    for w in range(len(blon)):
        ejesx=blon[w][0]
        ejesy=blon[w][1]
        m[ejesx][ejesy]="u"
    if bol[i][e][y][x]==blon:
        blon.pop([w,1])
    

def lv2():
    global m,ob
    for bloc in range(5,16):
        m[bloc][3]="N"
def lv3():
    global m
    for asd in range(6,17):
        m[asd][4]="I"
def mov():
    global bol,m
    for z in range(len(bol)):
        ejex=bol[z][0]#bol[z][0]=10#
        ejey=bol[z][1]#bol[z][1]=16
        mine=bol[z][0]-bol[z][2]
        miney=bol[z][1]-bol[z][3]
        m[mine][miney]=" "
        if m[ejex-1][ejey]!=" " or m[ejex+1][ejey]!=" ":#PARA QUE REBOTE X
            if bol[z][2]==-1:#
                bol[z][2]=1#
            else:
                bol[z][2]=-1#
        if m[ejex][ejey+1]!=" " or m[ejex][ejey-1]!=" ":#PARA QUE REBOTE Y
            if bol[z][3]==-1:#
                bol[z][3]=1#
            else:
                bol[z][3]=-1#
        if m[ejex+1][ejey+1]=="=" or m[ejex-1][ejey+1]=="=":
            if bol[z][3]==1:
                bol[z][3]=-1
            else:
                bol[z][3]=-1
        bol[z][0]+=bol[z][2]
        bol[z][1]+=bol[z][3]
        m[ejex][ejey]="O"
def upDatepos(dir):
    global m,x,y,bar
    m[x][y]=" "
    for we in range(-bar,bar+1):#para entender esto mira arriba la variable bar esto hace que no deje rastro
        m[x+we][y]=" " 
    if dir=="left":
        if x>3:
            x-=1
    elif dir=="right":
        if x<len(m)-4:
            x+=1
    m[x][y]="="
    for we in range(-bar,bar+1):
        m[x+we][y]="="
def leftKey(event):
    upDatepos("left")
def rightKey(event):
    upDatepos("right") 
def printMat():
    global m,bol,ejex,ejey
    for j in range(len(m[0])):
        c=""
        for i in range(len(m)):
            c+= str(m[i][j])
        print c
def task():
    global tim,bol
    os.system('cls')
    upDatepos(dir)
    lv1()
    mov()
    if bol[0][1]==18:
        gameover()
    probpoderes()
    printMat()
    root.after(tim,task)    
for i in range(20):
	c=[]
	for j in range(20):
		c.append(" ")
	m.append(c)

frame = Frame(root, width=10, height=10)
root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)
frame.pack()

root.after(30,task)
root.mainloop()
