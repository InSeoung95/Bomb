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


    def background_draw(self):
        self.image.draw(self.x, self.y, 100, 50)
        self.x += 100
        if (self.x >= 800):
            self.y += 50
            self.x = 50
    pass

class Player:
    def __init__(self):
        self.x, self.y = 400,300
        self.frame = 0
        self.image = load_image('unit_dao.png')

# 초기화
global running
stage = Stage()


running = True

# 반복구간

while(running):
    clear_canvas()
    while(True):
        stage.background_draw()
        if(stage.y >= 600):
            stage.y = 25
            break

    update_canvas()

    delay(0.01)

close_canvas()
