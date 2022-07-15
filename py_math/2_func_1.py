import pygame as pg
from math import *
width=400
window=pg.display.set_mode((width,width))
def offset(pos,cordinate=True):
    x,y=pos
    if cordinate:return x-(width/2),y-(width/2)
    else:return x+(width/2),y+(width/2)
def f(pos,a):
    x,y=offset(pos)
    vec=int(((cos(((y)/20)+a)+sin(x/20)+2)/4)*255)
    return vec
def update():
    pg.display.update()
    clock.tick(10000)
    # window.fill((0,0,0))
    for event in pg.event.get():
        if event.type==pg.QUIT:quit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_ESCAPE:quit()
clock=pg.time.Clock()
pixel=pg.PixelArray(window)
a=0
while 1:
    update()
    for i in range(width):
        for j in range(width):
            col=f((i,j),a)
            pixel[i,j]=(col,col,col)
    a+=0.1

