from tkinter import*
import random as ran
import time
import copy

tk=Tk()
tk.title('テトリス')
can=Canvas(tk,width=600,height=690,bd=0,highlightthickness=0,bg='blue4')
can.pack()
fl=[]

class block:
    def __init__(self,can,pi,fl):
        self.can=can
        self.fl=fl
        color=['red','bisque','yellow2','cyan','green yellow','deeppink','magenta']
        self.cl=color[pi]
        self.id=[can.create_rectangle(0,0,30,30,fill=self.cl)]
        for i in range(0,3):
            self.id.append(can.create_rectangle(0,0,30,30,fill=self.cl))
        self.x=0
        self.spin=0
        self.pi=pi
        self.dontmove=False
        self.can.bind_all('<KeyPress-Left>',self.Left)
        self.can.bind_all('<KeyPress-Right>',self.Right)
        self.can.bind_all('<KeyPress-Down>',self.Down)
        self.can.bind_all('<KeyRelease-Left>',self.re)
        self.can.bind_all('<KeyRelease-Right>',self.re)
        self.can.bind_all('<space>',self.Spin)
        if pi==0:
            can.move(self.id[1],30,0)
            can.move(self.id[2],0,30)
            can.move(self.id[3],30,30)
        elif pi==1:
            can.move(self.id[1],0,30)
            can.move(self.id[2],30,30)
            can.move(self.id[3],60,30)
        elif pi==2:
            can.move(self.id[0],60,0)
            can.move(self.id[1],60,30)
            can.move(self.id[2],30,30)
            can.move(self.id[3],0,30)
        elif pi==3:
            can.move(self.id[1],-30,0)
            can.move(self.id[2],30,0)
            can.move(self.id[3],60,0)
        elif pi==4:
            can.move(self.id[0],30,0)
            can.move(self.id[2],0,30)
            can.move(self.id[3],-30,30)
            self.move(30,0)
        elif pi==5:
            can.move(self.id[1],30,0)
            can.move(self.id[2],30,30)
            can.move(self.id[3],60,30)
        elif pi==6:
            can.move(self.id[1],-30,30)
            can.move(self.id[2],0,30)
            can.move(self.id[3],30,30)
        self.move(25+30*4,10)
    def draw(self):
        if self.dontmove==False:
            for i in self.id:
                if self.can.coords(i)[2] >= 385 and self.x>=30:
                    self.x=0
                if self.can.coords(i)[0]<=25 and self.x<=-30:
                    self.x=0
            self.move(self.x,0)
    def down(self):
        self.candown()
        if self.dontmove==False:
            self.move(0,30)
    def move(self,x,y):
        for i in range(0,4):
            can.move(self.id[i],x,y)
    def Right(self,event):
            if not self.canmove(True):
                self.x=30
    def Left(self,event):
            if not self.canmove(False):
                self.x=-30
    def Down(self,event):
            self.down()
    def re(self,event):
        self.x=0
    def candown(self):
        for i in range(0,4):
            pos=self.can.coords(self.id[i])
            if fl.candown(pos[0], pos[1] + 30):
                self.dontmove=True
        if self.dontmove:
            for x in self.id:
                pos=self.can.coords(x)
                fl.put(pos[0],pos[1],self.cl)
            self.move(1000,1000)
            fl.check()
    def canmove(self,rig):
        x=True
        for i in range(0,4):
            pos=self.can.coords(self.id[i])
            if not fl.canmove(pos[0],pos[1],rig):
                x=False
        return x
    def Spin(self,event):
        if self.pi==1:
            if self.spin==0:
                can.move(self.id[0], 30,0)
                can.move(self.id[1], 0, -30)
                can.move(self.id[2], -30,0)
                can.move(self.id[3], -60,30)
                self.spin=1
            elif self.spin==1:
                can.move(self.id[0], 0, 30)
                can.move(self.id[1], 30, 0)
                can.move(self.id[2], 0, -30)
                can.move(self.id[3], -30, -60)
                self.spin=2
            elif self.spin==2:
                can.move(self.id[0], -30, 0)
                can.move(self.id[1], 0, 30)
                can.move(self.id[2], 30, 0)
                can.move(self.id[3], 60, -30)
                self.spin=3
            elif self.spin == 3:
                can.move(self.id[0], 0, -30)
                can.move(self.id[1], -30, 0)
                can.move(self.id[2], 0, 30)
                can.move(self.id[3], 30, 60)
                self.spin = 0
        if self.pi==2:
            if self.spin==0:
                can.move(self.id[0], 0,30)
                can.move(self.id[1], -30, 0)
                can.move(self.id[2], 0,-30)
                can.move(self.id[3], 30,-60)
                self.spin=1
            elif self.spin==1:
                can.move(self.id[0], -30, 0)
                can.move(self.id[1], 0, -30)
                can.move(self.id[2], 30, 0)
                can.move(self.id[3], 60, 30)
                self.spin=2
            elif self.spin==2:
                can.move(self.id[0], 0, -30)
                can.move(self.id[1], 30, 0)
                can.move(self.id[2], 0, 30)
                can.move(self.id[3], -30, 60)
                self.spin=3
            elif self.spin == 3:
                can.move(self.id[0], 30, 0)
                can.move(self.id[1], 0, 30)
                can.move(self.id[2], -30, 0)
                can.move(self.id[3], -60, -30)
                self.spin = 0
        elif self.pi==3:
            if self.spin==0:
                can.move(self.id[0], 0, 30)
                can.move(self.id[1], 30, 0)
                can.move(self.id[2], -30, 60)
                can.move(self.id[3], -60, 90)
                self.spin = 1
            elif self.spin==1:
                can.move(self.id[0], 0, -30)
                can.move(self.id[1], -30, 0)
                can.move(self.id[2], 30, -60)
                can.move(self.id[3], 60, -90)
                self.spin = 0
        elif self.pi==4:
            if self.spin==0:
                can.move(self.id[0], 0, 30)
                can.move(self.id[1], 30, 0)
                can.move(self.id[2], 0, -30)
                can.move(self.id[3], 30, -60)
                self.spin = 1
            elif self.spin==1:
                can.move(self.id[0], 0, -30)
                can.move(self.id[1], -30, 0)
                can.move(self.id[2], 0, 30)
                can.move(self.id[3], -30, 60)
                self.spin = 0
        elif self.pi==5:
            if self.spin==0:
                can.move(self.id[0], 60, 0)
                can.move(self.id[1], 30, 30)
                can.move(self.id[3], -30, 30)
                self.spin=1
            elif self.spin==1:
                can.move(self.id[0], -60, 0)
                can.move(self.id[1], -30, -30)
                can.move(self.id[3], 30, -30)
                self.spin=0
        elif self.pi==6:
            if self.spin==0:
                can.move(self.id[1],30,30)
                self.spin=1
            elif self.spin==1:
                can.move(self.id[1],-30,-60)
                can.move(self.id[3],0,-30)
                self.spin=2
            elif self.spin==2:
                can.move(self.id[0],30,30)
                can.move(self.id[1],60,60)
                self.spin=3
            elif self.spin==3:
                can.move(self.id[0], -30, -30)
                can.move(self.id[1], -60, -30)
                can.move(self.id[2], 0, 0)
                can.move(self.id[3], 0, 30)
                self.spin=0
        while True:
            check=False
            for i in self.id:
                if self.can.coords(i)[2]>385:
                    self.move(-30,0)
                    check=True
                if self.can.coords(i)[3]>700:
                    self.move(0,-30)
                    check=True
                if self.can.coords(i)[0]<25:
                    self.move(30,0)
                    check=True
            if check==False:
                break

class masu:
    def __init__(self,can,color):
        self.can=can
        self.color=color
        self.bl=False
        self.id=can.create_rectangle(25,10,55,40,fill=color)
    def colorchange(self,co,a,b):
        x=30*a+25
        y=30*b+10
        self.id=self.can.create_rectangle(x,y,x+30,y+30,fill=co)
        self.color=co
        self.bl=True
    def candown(self):
        return self.bl

class Field:
    def __init__(self,can,tk):
        self.can=can
        self.tk=tk
        self.score=0
        self.id=[[masu(can,'gray11') for i in range(22)] for j in range(12)]
        for i in range(0,22):
            for j in range(0,12):
                can.move(self.id[j][i].id,30*j,30*i)
    def put(self,a,b,color):
        x=int((a-25)/30)
        y=int((b-10)/30)
        if x<12 and y<22:
            self.id[x][y].colorchange(color,x,y)
    def check(self):
        for k in range(0,22):
            i=21-k
            check=True
            for j in range(0,12):
                if not self.id[j][i].bl:
                    check=False
                    break
            if check:
                self.score+=10
                time.sleep(0.5)
                for b in range(0, 12):
                    for a in range(0,i-1):
                        self.id[b][i-a].colorchange(self.id[b][i-a-1].color,b,i-a)
                        self.id[b][i - a].bl=self.id[b][i-a-1].bl
                    self.id[b][0].colorchange('gray11',b,0)
                    self.id[b][0].bl=False
                time.sleep(0.1)
                tk.update()
    def candown(self,a,b):
        x=int((a-25)/30)
        y=int((b-10)/30)
        if y>=22:
            return True
        return self.id[x][y].candown()
    def canmove(self,a,b,rig):
        x=int((a-25)/30)
        y=int((b-10)/30)

        if rig and x<11:
            x=x+1
        elif rig==False and 0<x:
            x=x-1
        return self.id[x][y].candown()

class next:
    def __init__(self,pi):
        color = ['red', 'bisque', 'yellow2', 'cyan', 'green yellow', 'deeppink', 'magenta']
        self.cl = color[pi]
        self.id = [can.create_rectangle(0, 0, 30, 30, fill=self.cl)]
        for i in range(0, 3):
            self.id.append(can.create_rectangle(0, 0, 30, 30, fill=self.cl))
        if pi==0:
            can.move(self.id[1],30,0)
            can.move(self.id[2],0,30)
            can.move(self.id[3],30,30)
            self.move(20,0)
        elif pi==1:
            can.move(self.id[1],0,30)
            can.move(self.id[2],30,30)
            can.move(self.id[3],60,30)
        elif pi==2:
            can.move(self.id[0],60,0)
            can.move(self.id[1],60,30)
            can.move(self.id[2],30,30)
            can.move(self.id[3],0,30)
        elif pi==3:
            can.move(self.id[1],-30,0)
            can.move(self.id[2],30,0)
            can.move(self.id[3],60,0)
            self.move(20,15)
        elif pi==4:
            can.move(self.id[0],30,0)
            can.move(self.id[2],0,30)
            can.move(self.id[3],-30,30)
            self.move(30,0)
        elif pi==5:
            can.move(self.id[1],30,0)
            can.move(self.id[2],30,30)
            can.move(self.id[3],60,30)
        elif pi==6:
            can.move(self.id[1],-30,30)
            can.move(self.id[2],0,30)
            can.move(self.id[3],30,30)
            self.move(30,0)
        self.move(950,50)
    def move(self,x,y):
        for i in range(0,4):
            can.move(self.id[i],x,y)

tk.update()
fl=Field(can,tk)
box=can.create_rectangle(410,410,590,530,fill='gray11')
box2=can.create_rectangle(410,30,590,130,fill='gray11')
blo=[block(can,1,fl)]
count=0
num=0
nextnum=ran.randint(0,6)
beforscore=0
beforeeasy=1
noweasy=1
ne=[next(0),next(1),next(2),next(3),next(4),next(5),next(6)]
ne[nextnum].move(-500,0)
score=can.create_text(500,500,text='Score:%s'%fl.score,font=(30,30),fill='white')
easy=can.create_text(500,450,text='Level:%s'%beforeeasy,font=(30,30),fill='white')


while True:
    if blo[num].dontmove==True:
        blo.append(block(can,nextnum,fl))
        ne[nextnum].move(500,0)
        nextnum=int(ran.randint(0,6))
        ne[nextnum].move(-500,0)
        num += 1
    blo[num].draw()
    x=8
    if fl.score>=200:
        x=1
        noweasy=5
    elif fl.score >= 150 and fl.score < 200:
        x=2
        noweasy=4
    elif fl.score >= 100 and fl.score < 150:
        x=3
        noweasy=3
    elif fl.score>=50 and fl.score<100:
        x=5
        noweasy=2
    if count%x==0:
        blo[num].down()
    if fl.id[6][0].bl:
        break
    if beforscore<fl.score:
        beforscore=fl.score
        can.move(score,1000,1000)
        score = can.create_text(500, 500, text='Score:%s' % fl.score, font=(30, 30), fill='white')
        if noweasy>beforeeasy:
            beforeasy=noweasy
            can.move(easy,1000,1000)
            easy = can.create_text(500, 450, text='Level:%s' % noweasy, font=(30, 30), fill='white')

    time.sleep(0.06)
    count+=1
    tk.update()
tx=can.create_text(300,300,text='GAME OVER',font=(50,50),fill='red')
tk.mainloop()