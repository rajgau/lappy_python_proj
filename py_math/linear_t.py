import pygame as pg
import numpy as np
from math import *
width=400
window=pg.display.set_mode((width,width))
pg.display.set_caption(__file__.split("/")[-1])
def update():
    pg.display.update()
    window.fill((0,0,0))
    for event in pg.event.get():
        if event.type==pg.QUIT:quit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                return True
    return False
def grid():
    gap=width//10
    for x in range(0,width,gap):
        pg.draw.line(window,(0,200,50),(x,0),(x,width))
        pg.draw.line(window,(200,50,0),(0,x),(width,x))
matrix=[[1,3],
        [5,1]]
def transform(vec):
    x,y=vec
    x-=width/2
    y-=width/2
    x,y=np.dot((x,y),matrix)
    return (x+(width/2),((width/2)+y))
# grid()
# span=[]
# for i in range(0,width,10):
#     for j in range(0,width,10):
        
# print(len(span))
# for i in span:
#     pg.draw.circle(window,(80,80,255),i,3)
t=0
a=0
while 1:
    q,w=pg.mouse.get_pos()
    q,w=((2*q)/width)-1,((2*w)/width)-1
    tog = update()
    if tog:t+=1
    if tog%2==0:
        matrix[0][0]=q
        matrix[1][0]=w
    else:
        matrix[0][1]=q
        matrix[1][1]=w
    # matrix[0][1]=sin(a)*0.5
    # matrix[1][1]=cos(a)*0.5
    # matrix[0][0]=sin(-a+q)*0.5
    # matrix[1][0]=cos(a+w)*0.5
    a+=0.01
    grid()
    span=[transform((i,j)) for i in range(0,width,10) for j in range(0,width,10)]
    for i in span:
        pg.draw.circle(window,(80,80,255),i,3)



