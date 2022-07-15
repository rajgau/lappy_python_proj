from PIL import Image as im
import numpy as np
# 5/7
devby=3
img = np.array(im.open("3.png").resize((int(384/devby),int(384/devby))).__array__())

maper = lambda var,minI,maxI,minO,maxO:(((var-minI)/(maxI-minI))*(maxO-minO))+minO

imgbw=[[0 for j in range(len(img[0]))] for i in range(len(img))]
for i in range(len(img)):
    for j in range(len(img[0])):
        sumer=0
        for k in range(3):
            sumer+=img[i][j][k]/3
        imgbw[i][j]=[sumer/255,sumer/255,sumer/255]

ascci="#MWBHEA@0mabco<>^*;~_,.`         "

for i in range(len(imgbw)):
    for j in range(len(imgbw[0])):
        ind=int(maper(imgbw[i][j][0],0,1,len(ascci)-1,0))
        # ind=int(maper(imgbw[i][j][0],0,1,0,len(ascci)-1))
        print(ascci[ind],end='')
    print("\n")





























