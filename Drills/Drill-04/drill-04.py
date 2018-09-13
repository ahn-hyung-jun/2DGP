from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')


x=0
frame=0
direction=0
while(1):
    if(direction==0):
        while(x<800):
            clear_canvas()
            grass.draw(400,30)
            character.clip_draw(frame * 100, 100, 100, 100, x, 90) 
            x=x+5
            frame=(frame+1)%8
            update_canvas()
            delay(0.05)
            get_events()
        direction=1
    if(direction==1):
        while(0<x):
            clear_canvas()
            grass.draw(400,30)
            character.clip_draw(frame * 100, 0, 100, 100, x, 90) 
            x=x-5
            frame=(frame+1)%8
            update_canvas()
            delay(0.05)
            get_events()
        direction=0
    
close_canvas()

