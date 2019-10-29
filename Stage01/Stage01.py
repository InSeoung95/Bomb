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
        self.x, self.y = 400, 300
        self.frame_x, self.frame_y = 0, 0
        self.width, self.height = 0, 0
        self.vertical_dir, self.horizon_dir = 0, 0
        '''
        self.width_frame_x, self.width_frame_y = 243, 610
        self.height_frame_x, self.height_frame_y = 0, 405
        self.image = load_image('unit_dao.png')
        '''
        '''
        왼, 오른쪽 이동. clip draw(243 +@, 610, 81, 81,x, y)
        앞으로 이동. clip draw(0, 405+@, 120, 70, x, y)
        뒤로 이동. clip draw(120 , 405+@, 80, 70, x, y)
        '''
    def go_update(self):
        self.image.clip_draw(self.frame_x, self.frame_y, self.width, self.height, self.x, self.y)

    def go_right(self):

        self.image.clip_draw(self.frame_x, self.width_frame_y, 81, 81, self.x, self.y)


    def go_front(self):

        self.image.clip_draw(self.height_frame_x, self.height_frame_y, 120, 70, self.x, self.y)

    def go_back(self):
        self.height_frame_x = 120
        self.image.clip_draw(self.height_frame_x, self.height_frame_y, 80, 70, self.x, self.y)

    def handle_event(self):
        global running

        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_d:
                    self.horizon_dir += 1
                    self.x += self.horizon_dir* 5

                    self.frame_x + 243
                    self.frame_y = 610
                    self.width, self.height = 81, 81
                    self.go_update()

                    self.frame_x += 74
                    if (self.frame_x >= 486):
                        self.frame_x = 243

                elif event.key == SDLK_a:
                    self.horizon_dir -= 1
                    self.x -= self.horizon_dir*5

                    self.frame_x + 243
                    self.frame_y = 610
                    self.width, self.height = 81, 81
                    self.go_update()

                    self.frame_x += 74
                    if (self.frame_x >= 486):
                        self.frame_x = 243

                elif event.key == SDLK_w:
                    self.y += 10
                    self.go_front()
                    self.height_frame_y += 73
                    if (self.height_frame_y >= 648):
                        self.height_frame_y = 405


                elif event.key == SDLK_s:
                    self.y -= 10
                    self.go_back()
                    self.height_frame_y += 73
                    if (self.height_frame_y >= 648):
                        self.height_frame_y = 405
                elif event.key == SDLK_ESCAPE:
                    running = False







# 초기화
global running
stage = Stage()
player = Player()
dir = 0

running = True

# 반복구간

while(running):
    clear_canvas()

    while(True):
        stage.background_draw()
        if(stage.y >= 600):
            stage.y = 25
            break
    player.handle_event()
    update_canvas()


    delay(0.01)

close_canvas()
