import random
from time import time
import pygame as pg
frac_x,frac_y=600,600
width,height=(15,15)
window=pg.display.set_mode((frac_x,frac_y))
pg.display.set_caption(__file__.split("/")[-1])
def update():
    pg.display.update()
    window.fill((0,0,0))
    x=y=0
    for event in pg.event.get():
        if event.type==pg.QUIT:quit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_UP:x=1
            elif event.key==pg.K_DOWN:x=-1
            if event.key==pg.K_RIGHT:y=1
            elif event.key==pg.K_LEFT:y=-1
    return (x,y)
class Env:
    def __init__(self,width,height):
        self.size_x=frac_x/width
        self.size_y=frac_y/height
        self.food=self.create_food()
        self.vel_x=0
        self.vel_y=1
        self.body=[(width//2,height//2)]
        self.frame_time=0
    def create_food(self):return (random.randint(0,width-1),random.randint(0,height-1))
    def show_env(self):
        for i in range(width):
            for j in range(height):
                pg.draw.rect(window,(100,100,100),(self.size_x*i,self.size_y*j,self.size_x,self.size_y))
                pg.draw.rect(window,(40,40,40),(self.size_x*i,self.size_y*j,self.size_x-1,self.size_y-1))
        pg.draw.rect(window,(255,0,0),(self.food[0]*self.size_x,self.food[1]*self.size_y,self.size_x,self.size_y))
        pg.draw.rect(window,(70,70,70),(self.food[0]*self.size_x+3,self.food[1]*self.size_y+3,self.size_x-6,self.size_y-6))
        for part in self.body:
            pg.draw.rect(window,(255,105,180),(self.size_x*part[0],self.size_y*part[1],self.size_x,self.size_y))
    def move_snake(self,x,y):
        if self.vel_y!=0:
            if x!=0:self.vel_x=x
        elif self.vel_x!=0:
            if y!=0:self.vel_y=y
        
    
env=Env(width,height)
env.create_food()
while 1:
    t1=time()
    movement=update()
    env.show_env()
    t2=time()
    dt=1//(t2-t1)
    print(dt)
    env.move_snake(movement,dt)

