from pico2d import *
import os

os.getcwd()
os.chdir('C:\\Users\\황인성\\Desktop\\2016184042_HIS\\크레이지 아케이드 리소스(크아,Crazy Arcade)\\크아이미지')


#클래스 정의

open_canvas()
class Item:
    def __init__(self):
        self.item01 = load_image('item_64.png')
        self.height, self.width = 60, 60
        self.state = True
    def draw(self):
        self.item01.draw(100,400,self.height,self.height)
    def eat(self):
        self.state = False
        player.velocity += 10
    pass

class Bomb:
    def __init__(self):
        self.idle_image = load_image('custom_bubble_95.png')
        self.spread_image = load_image('unit_bombwater.png')
        self.state = False
        self.time =0
        self.bomb_x, self.bomb_y =0, 0
        self.dir=0
    def draw(self):
        self.idle_image.clip_draw(10+self.dir*73,10,50, 50, self.bomb_x, self.bomb_y)
        self.dir += 1
        if(self.dir >2):
            self.dir = 0
        self.time += 1
        if(self.time > 30):
            self.state = False
            self.time = 0
        if(self.state==False):
            for i in range(0,4):
                self.spread_image.clip_draw(260+65*i,252,60,70,self.bomb_x+25,self.bomb_y )#오른쪽 터질 때
                self.spread_image.clip_draw(260+65*i,180,60,70,self.bomb_x-25,self.bomb_y )#왼쪽 터질 때
                self.spread_image.clip_draw(10+65*i,180,60,70, self.bomb_x,self.bomb_y+25)#위쪽 터질 때
                self.spread_image.clip_draw(10+65*i,252,60,70, self.bomb_x,self.bomb_y-25)#아래 터질 때
    pass


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
        for i in range(0, 5):
            self.object_01.draw(self.object_x+self.object_width*i,self.object_y,self.object_width, self.object_height)
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

        self.right_state = False
        self.up_state = False
        self.down_state = False

        self.image = load_image('unit_dao.png')
        #self.reverse_image = load_image('unit_dao01.png')

        self.velocity = 3
        self.velocity_a =0

        '''
        왼, 오른쪽 이동. clip draw(243 +@, 610, 81, 81,x, y)
        앞으로 이동. clip draw(0, 405+@, 120, 70, x, y)
        뒤로 이동. clip draw(120 , 405+@, 80, 70, x, y)
        '''
    def go_update(self):
        self.image.clip_draw(self.frame_x, self.frame_y, self.width, self.height, self.x, self.y)


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
                    self.right_state = True
                    self.horizon_dir += self.velocity

                elif event.key == SDLK_a:
                    self.right_state = True
                    #self.image = load_image('unit_dao_reverse.png')
                    self.horizon_dir -= self.velocity

                elif event.key == SDLK_w:
                    self.up_state = True
                   #self.image = load_image('unit_dao01')
                    self.vertical_dir += self.velocity

                elif event.key == SDLK_s:
                    self.down_state = True
                    self.vertical_dir -= self.velocity

                    #self.go_back()
                elif event.key == SDLK_SPACE:
                    bomb.state =True
                    bomb.bomb_x = player.x
                    bomb.bomb_y = player.y


                elif event.key == SDLK_ESCAPE:
                    running = False
            elif event.type == SDL_KEYUP:
                if event.key == SDLK_d:
                    self.right_state = False
                    self.horizon_dir -= self.velocity

                    self.frame_x = 465
                    self.frame_y = 680
                    self.width, self.height = 80, 70
                    #self.go_right()

                elif event.key == SDLK_a:
                    self.right_state = False
                    self.horizon_dir += self.velocity
                    self.frame_x = 455
                    self.frame_y = 680
                    self.width, self.height = 80, 70
                    #self.go_right()


                elif event.key == SDLK_w:
                    self.up_state = False
                    self.vertical_dir -= self.velocity
                    self.frame_x = 290
                    self.frame_y = 697
                    self.width, self.height = 80, 70
                    #self.go_front()

                elif event.key == SDLK_s:
                    self.down_state = False
                    self.vertical_dir += self.velocity
                    self.frame_x =370
                    self.frame_y = 697
                    self.width, self.height = 80, 70

                    #self.go_back()


# 초기화
global running
stage = Stage()
player = Player()
item = Item()

dir = 0
bomb = Bomb()

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
    if(bomb.state==True):
        bomb.draw()
    if(item.state==True):
        item.draw()

    player.go_update()
    update_canvas()
    player.handle_event()

    if(player.right_state == True):
        player.right_frame_x += 74
        if (player.right_frame_x >= 486):
            player.right_frame_x = 243
        player.frame_x = player.right_frame_x
        player.frame_y = player.right_frame_y
    elif(player.up_state == True):
        player.up_frame_y += 73
        if (player.up_frame_y >= 648):
            player.up_frame_y = 405
        player.frame_x = player.up_frame_x
        player.frame_y = player.up_frame_y
    elif(player.down_state == True):
        player.down_frame_y += 73
        if (player.down_frame_y >= 648):
            player.down_frame_y = 405
        player.frame_x = player.down_frame_x
        player.frame_y = player.down_frame_y

    player.x += player.horizon_dir * 5
    player.y += player.vertical_dir * 5

    if ((player.x > 40 and player.x < 640) and (player.y > 100 and player.y < 140)):
        player.x = player.x - player.horizon_dir*5
        player.y = player.y - player.vertical_dir * 5
        continue
    if((player.x>70 and player.x<130) and (player.y> 370 and player.y < 430)):
        if(item.state==True):
            item.state = False

    if(player.x<10):
        player.x = 10
    elif(player.x>790):
        player.x = 790

    if(player.y<20):
        player.y = 20
    elif(player.y>580):
        player.y = 580

    delay(0.05)

close_canvas()
