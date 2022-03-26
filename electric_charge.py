from random import uniform as uni
from random import choice 
import pygame as pg
import numpy as np
width,height=400,400
window=pg.display.set_mode((width,height))
pg.display.set_caption(__file__.split("/")[-1])
class Particle:
    def __init__(self):
        self.vel=np.array([uni(-1,1),uni(-1,1)])
        self.pos=np.array([uni(-width/2,width/2),uni(-height/2,height/2)])
        self.q=choice([-1,1])
    def show(self):
        pg.draw.circle(window,(0,255,0),(self.pos[0]+width/2,self.pos[1]+height/2),3,0)
    def force_move(self,particles):
        ind=particles.index(self)
        for i in range(len(particles)):
            if i==ind:continue
            dx,dy=move(self,particles[i])
            self.vel[0]+=dx
            self.vel[1]+=dy
        # print(self.vel_)
        self.pos[0]+=self.vel[0]
        self.pos[1]+=self.vel[1]
def move(p1,p2):
    k=9*(10**5)
    dsqr=(p2.pos[0]-p1.pos[0])**2+(p2.pos[1]-p1.pos[1])**2
    dv=((k*p1.q*p2.q)/dsqr)
    dv_x=dv*p2.vel[0]-p1.vel[0]
    dv_y=dv*p2.vel[1]-p1.vel[1]
    return (dv_x,dv_y)
def update():
    pg.display.update()
    window.fill((0,0,0))
    for event in pg.event.get():
        if event.type==pg.QUIT:quit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_ESCAPE:quit()
particles=[Particle() for i in range(10)]
while 1:
    update()
    for particle in particles:
        particle.show()
        particle.force_move(particles)
