import random
import pygame as pg
clock=pg.time.Clock()
width,height=(400,400)
window=pg.display.set_mode((width,height))
def update():
    pg.display.update()
    window.fill((0,0,0))
    clock.tick(25)
    for event in pg.event.get():
        if event.type==pg.QUIT:quit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_ESCAPE:quit()
class Particle:
    k=10
    def  __init__(self,x,y,col=(100,255,100)):
        self.pos=[x,y]
        self.vel=[0,0]
        self.q=random.choice([-1,1])
        self.col=col
    def move(self,p):
        # a=k*q1*q2/r2
        val=(Particle.k*self.q*p.q)
        den_x=((p.pos[1]-self.pos[1])+0.0001)
        den_y=((self.pos[0]-p.pos[0])+0.0001)
        if not den_x<4:
            self.vel[0]+=val/den_x
            self.pos[0]+=self.vel[0]
        if not den_y<4:
            self.vel[1]+=val/den_y
            self.pos[1]+=self.vel[1]

        # ////////////////////////////////// bounds
        if self.pos[0]>width:
            self.pos[0]=width
            self.vel[0]=0
        elif self.pos[0]<0:
            self.pos[0]=0
            self.vel[0]=0
        if self.pos[1]>height:
            self.pos[1]=height
            self.vel[1]=0
        elif self.pos[1]<0:
            self.pos[1]=0
            self.vel[1]=0
    def show(self):
        pg.draw.circle(window,self.col,self.pos,7)
a=Particle(133,201,col=(255,100,100))
b=Particle(133*2,200)
while 1:
    update()
    a.move(b)
    b.move(a)
    a.show()
    b.show()