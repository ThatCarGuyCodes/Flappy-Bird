from turtle import *
from random import *

class point:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.yspeed = 1

s = Screen()
bgcolor("lightblue")
bird = point(0, 0)
pipes=[]

def jump(x,y):
    bird.y +=20

def draw_pipe(x,y):
    color("green")
    begin_fill()
    forward(40)
    if y>25:
        left(90)
        forward(200-y)
        left(90)
        fd(40)
        left(90)
        fd(200-y)
        left(90)
    if y<-25:
        right(90)
        fd(200+y)
        right(90)
        fd(40)
        right(90)
        fd(200+y)
        right(90)
    end_fill()

def draw_bird():
    clear()
    goto(bird.x, bird.y)
    dot(20, 'yellow')
    for pipe in pipes:
        goto(pipe.x, pipe.y)
        draw_pipe(pipe.x, pipe.y)
        if abs(bird.x - pipe.x) < 10 and abs(bird.y - pipe.y) < 10:
            color("black")
            write("Game Over")
            ontimer(s.bye(), 1000)

def move():
    bird.yspeed = 2 + abs(200-bird.y)/50
    bird.y -=bird.yspeed
    for pipe in pipes:
        pipe.x -=3
    if randrange(10)==0:
        ypos = randint(-200, 200)
        pt = point(200, ypos)
        pipes.append(pt)
    draw_bird()
    ontimer(move, 100)

ht()
penup()
tracer(0)
onscreenclick(jump)
move()
