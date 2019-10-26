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
        self.width_frame_x, self.width_frame_y = 0, 0
        self.height_frame_x, self.height_frame_y = 0, 0
        self.image = load_image('unit_dao.png')

    def run_width(self):
        self.width_frame_y = 610

        self.image.clip_draw(self.width_frame_x, self.width_frame_y, 81, 81, self.x, self.y)

    def run_height(self):
        self.height_frame_x=0

        self.image.clip_draw(self.height_frame_x, self.height_frame_y, 120, 70, self.x, self.y)

# 초기화
global running
stage = Stage()
player = Player()
player.width_frame_x = 243
player.height_frame_y = 405
running = True

# 반복구간

while(running):
    clear_canvas()
    while(True):
        stage.background_draw()
        if(stage.y >= 600):
            stage.y = 25
            break

    player.run_width()
    player.width_frame_x += 74
    if(player.width_frame_x>= 486):
        player.width_frame_x = 243

    player.run_height()
    player.height_frame_y += 73
    if (player.height_frame_y >= 648):
        player.height_frame_y = 405

    update_canvas()

    delay(0.5)

close_canvas()
