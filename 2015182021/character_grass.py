from pico2d import *

os.chdir('C:\\2DGP\\2018-2DGP\\Labs\\Lecture03')

open_canvas()

grass=load_image('grass.png')
character=load_image('character.png')

grass.draw_now(400,30)
character.draw_now(400,90)

delay(5)
                

close_canvas()
