import pygame as pg
from math import *
width=600
window=pg.display.set_mode((width,width))
class Particle:
    def __init__(self,x,y):
        self.pos=[x,y]
        self.vel=[0,0]
        self.size=1
    def move(self):
        if self.pos[0]<0:self.pos[0]=width
        elif self.pos[0]>width:self.pos[0]=0
        elif self.pos[1]<0:self.pos[1]=width
        elif self.pos[1]>width:self.pos[1]=0
        self.pos[0]+=self.vel[0]
        self.pos[1]+=self.vel[1]
    def show(self):pg.draw.circle(window,(3,150,255),self.pos,self.size)
class Env:
    def __init__(self,part=100): # 1 ---> 100
        self.particles=[Particle(i,j) for i in range(0,width,part) for j in range(0,width,part)]
    def move(self):
        for particle in self.particles:
            particle.vel=list(offset(f(particle.pos)))
            particle.move()
            particle.show()
def offset(pos,cordinate=True):
    x,y=pos
    if cordinate:return x-(width/2),y-(width/2)
    else:return x+(width/2),y+(width/2)
def f(pos,normalize=True):
    speed=4
    x,y=offset(pos)
    x1=-y
    y1=-x
    # x1=cos(y/50)
    # y1=sin(x/50)
    if normalize:
        dis=((x1)**2+(y1)**2)**0.5
        if dis==0:dis=1
        x1,y1=x1/dis,y1/dis
    return offset((x1*speed,y1*speed),False)
def show_vec():
    gap=10
    for i in range(0,width,gap):
        for j in range(0,width,gap):
            x,y=i+(gap/2),j+(gap/2)
            x,y=offset((x,y))
            x1,y1=offset(f((x,y)))
            x1=x+x1
            y1=y+y1
            pg.draw.line(window,(255,255,0),offset((x,y),False),offset((x1,y1),False))
clock=pg.time.Clock()
def update():
    pg.display.update()
    clock.tick(10080)
    window.fill((0,0,0))
    for event in pg.event.get():
        if event.type==pg.QUIT:quit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_ESCAPE:quit()
env=Env(10)
while 1:
    update()
    env.move()
    # show_vec()