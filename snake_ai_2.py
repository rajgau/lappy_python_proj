import random
import pygame as pg
class Env:
    clock=pg.time.Clock()
    width=600
    def __init__(self,side,show_env=True):
        self.show_env=show_env
        if show_env:
            self.window=pg.display.set_mode((Env.width,Env.width))
            pg.display.set_caption(__file__.split("/")[-1])
        self.size=Env.width//side
        self.body=[[side//2,side//2]]
        self.food=self.create_food()
        self.vel=0,-1
        self.colide=False
    def create_food(self):
        seq=[[i,j] for i in range(self.size) for j in range(self.size)]
        for i in self.body:
            seq.remove(i)
        return tuple(random.choice(seq))
    def show_envm(self):
        for i in range(self.side):
            for j in range(self.side):
                pg.draw.rect(self.window,(100,100,100),(self.size*i,self.size*j,self.size,self.size))
                pg.draw.rect(self.window,(40,40,40),(self.size*i,self.size*j,self.size-1,self.size-1))
        pg.draw.rect(self.window,(255,0,0),(self.food[0]*self.size,self.food[1]*self.size,self.size,self.size))
        pg.draw.rect(self.window,(70,70,70),(self.food[0]*self.size+3,self.food[1]*self.size+3,self.size-6,self.size-6))
        for part in self.body:
            pg.draw.rect(self.window,(255,105,180),(self.size*part[0],self.size*part[1],self.size,self.size))
            pg.draw.rect(self.window,(70,70,70),(self.size*part[0]+3,self.size*part[1]+3,self.size-6,self.size-6))
    def update(self):
        if self.show_env:
            pg.display.update()
            self.window.fill((0,0,0))
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
    def step(self,move=None):
        if move==None:
            movement=self.update()
            move=self.human_to_machine(movement)
        """takes number from 0 to 4 to move the snake"""
        x,y=0,0
        if move==0:x,y=0,0 # no input
        if move==1:x,y=0,-1 # up
        if move==2:x,y=1,0 # left
        if move==3:x,y=0,1 # down
        if move==4:x,y=-1,0 # right
        if self.vel[1]!=0:
            if x!=0:
                self.vel[0]=x
                self.vel[1]=0
        elif self.vel[0]!=0:
            if y!=0:
                self.vel[1]=y
                self.vel[0]=0
        if len(self.body)==1:
            self.body[-1][0]+=self.vel[0]
            self.body[-1][1]+=self.vel[1]
            if self.body[-1][0]+self.vel[0]<-1:self.body[-1][0]=self.width-1
            elif self.body[-1][0]+self.vel[0]>self.width:self.body[-1][0]=0
            elif self.body[-1][1]+self.vel[1]<-1:self.body[-1][1]=self.height-1
            elif self.body[-1][1]+self.vel[1]>self.height:self.body[-1][1]=0
        else:
            self.body.pop()
            if self.body[0][0]+self.vel[0]<0:self.body.insert(0,[self.width+self.vel[0],self.body[0][1]+self.vel[1]])
            elif self.body[0][0]+self.vel[0]>=self.width:self.body.insert(0,[0,self.body[0][1]+self.vel[1]])
            elif self.body[0][1]+self.vel[1]<0:self.body.insert(0,[self.body[0][0]+self.vel[0],self.height+self.vel[1]])
            elif self.body[0][1]+self.vel[1]>=self.height:self.body.insert(0,[self.body[0][0]+self.vel[0],0])
            else:self.body.insert(0,[self.body[0][0]+self.vel[0],self.body[0][1]+self.vel[1]])
        food_rew=self.eat_food()
        return (0,food_rew,self.colide,{})
    def eat_food(self):
        if tuple(self.body[0])==self.food:
            self.food=self.create_food()
            self.body.append([self.body[0][0]-self.vel[0],self.body[0][1]-self.vel[1]])
            return 10
        return 0
    def close(self):pg.quit()
    def human_to_machine(*move):
        # print(move[0])
        x,y=move[0]
        if x==0 and y==0:return 0 #none
        elif x==0 and y==-1:return 1 #up
        elif x==1 and y==0:return 2 #left
        elif x==0 and y==1:return 3 #down
        elif x==-1 and y==0:return 4 #right
