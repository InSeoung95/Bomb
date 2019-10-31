from pico2d import *

import Stage01

player = Stage01.Player()

class Bomb:
    def __init__(self):
        self.idle0 = load_image('Idle (0).png')
        self.idle1 = load_image('Idle (1).png')
        self.idle2 = load_image('Idle (2).png')

        self.idle = [self.idle0,self.idle1, self.idle2]
        self.time =0
    def boming(self):
        for i in self.idle:
            i.draw(player.x, player.y)
            delay(0.2)
    pass