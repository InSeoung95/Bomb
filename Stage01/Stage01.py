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
        self.object_01 = load_image('map_flopy_object5.png')
        self.object_x = 100
        self.object_y = 100
        self.object_width = 120
        self.object_height = 40


    def background_draw(self):
        self.image.draw(self.x, self.y, 100, 50)
        self.x += 100
        if (self.x >= 800):
            self.y += 50
            self.x = 50
    def object_draw(self):
        self.object_x = 100
        self.object_y= 100
        self.object_width = 120
        self.object_height = 40
        self.object_01.draw(self.object_x,self.object_y,self.object_width, self.object_height)
    pass

class Player:
    def __init__(self):
        self.x, self.y = 400, 300
        self.frame_x, self.frame_y = 120, 405
        self.width, self.height = 80, 70
        self.vertical_dir, self.horizon_dir = 0, 0

        self.right_frame_x, self.right_frame_y = 243, 610
        self.up_frame_x, self.up_frame_y = 40, 405
        self.down_frame_x, self.down_frame_y = 120, 405

        self.image = load_image('unit_dao.png')
        #self.reverse_image = load_image('unit_dao01.png')

        self.velocity = 6

        '''
        왼, 오른쪽 이동. clip draw(243 +@, 610, 81, 81,x, y)
        앞으로 이동. clip draw(0, 405+@, 120, 70, x, y)
        뒤로 이동. clip draw(120 , 405+@, 80, 70, x, y)
        '''
    def go_update(self):
        self.image.clip_draw(self.frame_x, self.frame_y, self.width, self.height, self.x, self.y)

    def go_right(self):
        self.image.clip_draw(self.right_frame_x, self.right_frame_y, 81, 81, self.x, self.y)
        self.right_frame_x += 74
        if (self.right_frame_x >= 486):
            self.right_frame_x = 243

    def go_front(self):
        self.image.clip_draw(self.up_frame_x, self.up_frame_y, 120, 70, self.x-100, self.y)
        '''
        self.up_frame_y += 73
        if (self.up_frame_y >= 648):
            self.up_frame_y = 405
        '''
    def go_back(self):
        self.image.clip_draw(self.down_frame_x, self.down_frame_y, 80, 70, self.x, self.y)
        self.down_frame_y += 73
        if (self.down_frame_y >= 648):
            self.down_frame_y = 405

    def handle_event(self):
        global running
        self.image = load_image('unit_dao.png')
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN:
                '''
                if((stage.object_x-stage.object_width/2 < self.x and stage.object_x+ stage.object_width/2 > self.x)
                        and(stage.object_y-stage.object_height/2<self.y and stage.object_y+stage.object_height/2>self.y)):
                    break
                    '''

                if event.key == SDLK_d:
                    self.horizon_dir += self.velocity
                    self.x += self.horizon_dir*5
                    if ((self.x > 40 and self.x < 160) and (self.y > 100 and self.y < 140)):
                        self.x = self.x -self.horizon_dir*5
                        break
                    self.right_frame_x += 74
                    if (self.right_frame_x >= 486):
                        self.right_frame_x = 243
                    self.frame_x = self.right_frame_x
                    self.frame_y = self.right_frame_y

                    self.width, self.height = 80, 80
                    #self.go_right()


                elif event.key == SDLK_a:
                    self.horizon_dir -= self.velocity
                    self.x += self.horizon_dir*5
                    if ((self.x > 40 and self.x < 160) and (self.y > 100 and self.y < 140)):
                        self.x = self.x -self.horizon_dir*5
                        break

                    self.right_frame_x += 74
                    if (self.right_frame_x >= 486):
                        self.right_frame_x = 243
                    self.frame_x = self.right_frame_x
                    self.frame_y = self.right_frame_y

                    self.width, self.height = 80, 80
                    #self.go_right()

                elif event.key == SDLK_w:
                   #self.image = load_image('unit_dao01')
                    self.vertical_dir += self.velocity
                    self.y += self.vertical_dir*5
                    if ((self.x > 40 and self.x < 160) and (self.y > 100 and self.y < 140)):
                        self.y = self.y - self.vertical_dir * 5
                        break

                    self.up_frame_y += 73
                    if (self.up_frame_y >= 648):
                        self.up_frame_y = 405
                    self.frame_x = self.up_frame_x
                    self.frame_y =self.up_frame_y

                    self.width, self.height = 80, 70
                    #self.go_front()


                elif event.key == SDLK_s:
                    self.vertical_dir -= self.velocity
                    self.y += self.vertical_dir*5
                    if ((self.x > 40 and self.x < 160) and (self.y > 100 and self.y < 140)):
                        self.y = self.y -self.vertical_dir*5
                        break

                    self.down_frame_y += 73
                    if (self.down_frame_y >= 648):
                        self.down_frame_y = 405
                    self.frame_x = self.down_frame_x
                    self.frame_y =self.down_frame_y

                    self.width, self.height = 80, 70

                    #self.go_back()

                elif event.key == SDLK_ESCAPE:
                    running = False
            elif event.type == SDL_KEYUP:
                if event.key == SDLK_d:
                    self.horizon_dir -= self.velocity
                    self.x += self.horizon_dir* 5
                    #self.go_right()

                elif event.key == SDLK_a:
                    self.horizon_dir += self.velocity
                    self.x += self.horizon_dir*5
                    #self.go_right()


                elif event.key == SDLK_w:
                    self.vertical_dir -= self.velocity
                    self.y += self.vertical_dir*5
                    #self.go_front()

                elif event.key == SDLK_s:
                    self.vertical_dir += self.velocity
                    self.y += self.vertical_dir*5
                    #self.go_back()










# 초기화
global running
stage = Stage()
player = Player()
player.handle_event()
dir = 0


running = True

# 반복구간

while(running):
    clear_canvas()
    while (True):
        stage.background_draw()
        if (stage.y >= 600):
            stage.y = 25
            break
    stage.object_draw()

    player.go_update()
    update_canvas()
    player.handle_event()
    if(player.x<10):
        player.x = 10
    elif(player.x>790):
        player.x = 790

    if(player.y<20):
        player.y = 20
    elif(player.y>580):
        player.y = 580

    delay(0.01)

close_canvas()
