import pygame as pg
width,height=400,400
window=pg.display.set_mode((width,height))
pg.display.set_caption(__file__.split("/")[-1])
def update():
    pg.display.update()
    for event in pg.event.get():
        if event.type==pg.QUIT:quit()
while 1:
    update()

