from curses import window
import pygame as pg
from math import dist
width,height=600,600
window = pg.display.set_mode((width,height))

def update():
    pg.display.update()
    for event in pg.event.get():
        if event.type==pg.QUIT:quit()
class Main_Particle:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.charge=1
    def show(self):
        pg.draw.circle(window,(0,255,0),(self.x,self.y),5)

P=Main_Particle(width//2,height//2)
P.show()

def Vector_feld(P):
    for i in range(0,width,6):
        for j in range(0,height,6):
            intencity = (0.1*P.charge)/(dist((i,j),(P.x,P.y))**2)
            
while 1:
    update()
    Vector_feld(P)