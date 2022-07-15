from PIL import Image as im
import pygame as pg
img = im.open("1.jpg").resize((500,300))
width,height=img.size

window=pg.display.set_mode((width*2,height))
pixel=pg.PixelArray(window)

img = img.__array__()
def show(img,off=False):
    for i in range(len(img[0])):
        for j in range(len(img)):
            if off==False:pixel[i][j]=tuple(img[j][i])
            else:pixel[i+width][j]=tuple(img[j][i])
def update():
    pg.display.update()
    for event in pg.event.get():
        if event.type==pg.QUIT:quit()
show(img)
update()
sb=1
sq=(2*sb)+1
off = [[3,1,3],
       [1,2,1],
       [3,1,3]]
# off = [[1 for j in range(sq)] for i in range(sq)]
for i in range(len(img[0])):
    for j in range(len(img)):
        for k in range(3):
            try:
                sumer=0
                for x,l in enumerate(off):
                    for y,m in enumerate(l):
                        if j+(x-sb)<0 or j+(x-sb)==len(img):sumer+=0
                        elif i+(y-sb)<0 or i+(y-sb)==len(img):sumer+=0
                        else:sumer+=img[j+(x-sb),i+(y-sb),k]*(m/(18))
                img[j,i,k]=int(sumer)
            except:img[j,i,k]=50*(k-2)
        # img[j,i,0]=0
        # img[j,i,1]=0
        # img[j,i,2]=0

show(img,True)
while 1:
    update()
