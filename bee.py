import pgzrun
from random import randint

WIDTH=600
HEIGHT=500

score=0

game_over=False

bee=Actor("bee")
flr=Actor("flower")

bee.pos=100,100
flr.pos=200,200

def draw():
    screen.blit("bg",(0,0))
    flr.draw()
    bee.draw()
    screen.draw.text("score "+str(score),color="black",topleft=(10,10))

pgzrun.go()
