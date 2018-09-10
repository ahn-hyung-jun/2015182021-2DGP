from pico2d import *
import turtle
import math

open_canvas()

grass=load_image('grass.png')
character=load_image('character.png')

grass.draw_now(400, 30)
character.draw_now(400, 90)

x = 0
y = 0
i=0
j=0
loop=0
degree=360

while (loop==0):
    while(x<700):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x=x+4
        delay(0.01)
    while(y<550):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(750,y)
        y=y+4
        delay(0.01)
    while(50<x):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,550)
        x=x-4
        delay(0.01)
    while(90<y):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(50,y)
        y=y-4
        delay(0.01)
    while(x<400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x=x+4
        delay(0.01)
        t=270   
    while(t<630):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(210*math.cos(math.radians(t))+400, 210*math.sin(math.radians(t))+300)
        t=t+2
        delay(0.01)
    
        

      

close_canvas()
