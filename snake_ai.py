import random
import pygame as pg
frac_x,frac_y=600,600
window=pg.display.set_mode((frac_x,frac_y))
pg.display.set_caption(__file__.split("/")[-1])
def update(show_env=True):
    if show_env:
        pg.display.update()
        window.fill((0,0,0))
        Env.clock.tick(20)
        x=y=0
        for event in pg.event.get():
            if event.type==pg.QUIT:quit()
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_UP:y=-1
                elif event.key==pg.K_DOWN:y=1
                if event.key==pg.K_RIGHT:x=1
                elif event.key==pg.K_LEFT:x=-1
                if event.key==pg.K_ESCAPE:quit()
        return (x,y)
    else:return random.choice([-1,0,1]),random.choice([-1,0,1])
class Env:
    clock=pg.time.Clock()
    def __init__(self,width,height,show_env=False):
        self.show_env=show_env
        if not show_env:pg.quit()
        self.width,self.height=width,height
        self.size_x=frac_x/width
        self.size_y=frac_y/height
        self.body=[[width//2,height//2]]
        self.food=self.create_food()
        self.vel_x=0
        self.vel_y=-1
        self.colide=False
    def create_food(self):
        seq=[[i,j] for i in range(self.width) for j in range(self.height)]
        for i in self.body:
            seq.remove(i)
        return tuple(random.choice(seq))
    def show_envm(self):
        for i in range(self.width):
            for j in range(self.height):
                try:
                    pg.draw.rect(window,(100,100,100),(self.size_x*i,self.size_y*j,self.size_x,self.size_y))
                    pg.draw.rect(window,(40,40,40),(self.size_x*i,self.size_y*j,self.size_x-1,self.size_y-1))
                except:print("~\_(-_-)_/~")
        pg.draw.rect(window,(255,0,0),(self.food[0]*self.size_x,self.food[1]*self.size_y,self.size_x,self.size_y))
        pg.draw.rect(window,(70,70,70),(self.food[0]*self.size_x+3,self.food[1]*self.size_y+3,self.size_x-6,self.size_y-6))
        for part in self.body:
            pg.draw.rect(window,(255,105,180),(self.size_x*part[0],self.size_y*part[1],self.size_x,self.size_y))
            pg.draw.rect(window,(70,70,70),(self.size_x*part[0]+3,self.size_y*part[1]+3,self.size_x-6,self.size_y-6))
    def step(self,move=None):
        if move==None:
            movement=update(self.show_env)
            move=human_to_machine(movement)
        """takes number from 0 to 4 to move the snake"""
        x,y=0,0
        if move==0:x,y=0,0 # no input
        if move==1:x,y=0,-1 # up
        if move==2:x,y=1,0 # left
        if move==3:x,y=0,1 # down
        if move==4:x,y=-1,0 # right
        if self.vel_y!=0:
            if x!=0:
                self.vel_x=x
                self.vel_y=0
        elif self.vel_x!=0:
            if y!=0:
                self.vel_y=y
                self.vel_x=0
        if len(self.body)==1:
            self.body[-1][0]+=self.vel_x
            self.body[-1][1]+=self.vel_y
            if self.body[-1][0]+self.vel_x<-1:self.body[-1][0]=self.width-1
            elif self.body[-1][0]+self.vel_x>self.width:self.body[-1][0]=0
            elif self.body[-1][1]+self.vel_y<-1:self.body[-1][1]=self.height-1
            elif self.body[-1][1]+self.vel_y>self.height:self.body[-1][1]=0
        else:
            self.body.pop()
            if self.body[0][0]+self.vel_x<0:self.body.insert(0,[self.width+self.vel_x,self.body[0][1]+self.vel_y])
            elif self.body[0][0]+self.vel_x>=self.width:self.body.insert(0,[0,self.body[0][1]+self.vel_y])
            elif self.body[0][1]+self.vel_y<0:self.body.insert(0,[self.body[0][0]+self.vel_x,self.height+self.vel_y])
            elif self.body[0][1]+self.vel_y>=self.height:self.body.insert(0,[self.body[0][0]+self.vel_x,0])
            else:self.body.insert(0,[self.body[0][0]+self.vel_x,self.body[0][1]+self.vel_y])
        food_rew=self.eat_food()
        return (0,food_rew,self.colide,{})
    def eat_food(self):
        if tuple(self.body[0])==self.food:
            self.food=self.create_food()
            self.body.append([self.body[0][0]-self.vel_x,self.body[0][1]-self.vel_y])
            return 10
        return 0
    def close(self):
        pg.quit()
def human_to_machine(*move):
    x,y=move[0]
    if x==0 and y==0:return 0 #none
    elif x==0 and y==-1:return 1 #up
    elif x==1 and y==0:return 2 #left
    elif x==0 and y==1:return 3 #down
    elif x==-1 and y==0:return 4 #right
env=Env(10,10)
while 1:
    n_state,reward,done,info=env.step()
    # print(env.step()
    env.show_envm()

