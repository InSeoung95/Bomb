from pico2d import *
import os

os.getcwd()
os.chdir('C:\\Users\\황인성\\Desktop\\2016184042_HIS\\크레이지 아케이드 리소스(크아,Crazy Arcade)\\크아이미지')

#클래스 정의

open_canvas()

class Stage:

    def __init__(self):
        self.image = load_image('map_flopy_tile2.png')
        self.x, self.y = 50, 25

    def update(self):
        self.x += 100
        if(self.x>=800):
            self.y += 50
            self.x = 50



    def draw(self):
        self.image.draw(self.x, self.y, 100, 50)
pass

# 초기화
global running
stage = Stage()


running = True

# 반복구간

while(running):
    stage.draw()
    update_canvas()
    stage.update()
    delay(0.01)

close_canvas()
