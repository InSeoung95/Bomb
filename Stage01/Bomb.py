from pico2d import *

class Bomb:
    def __init__(self):
        self.idle0 = load_image('Idle (0).png')
        self.idle1 = load_image('Idle (1).png')
        self.idle2 = load_image('Idle (2).png')

        self.idle = [self.idle0,self.idle1, self.idle2]
        self.time =0
    def boming(self):
        for i in self.idle:
            i.clip_draw(10,10,20,20)
            delay(0.2)
    pass
bomb = Bomb()

open_canvas()
bomb.boming()
update_canvas()
clear_canvas()