import pygame
from set_sprite import set_sprite
import config as cg 
class Hero(pygame.sprite.Sprite):
 
    frames_l = dict() # khung hình nhân vật chuyển động sang trái
    
    frames_r = dict() # khung hình nhân vật chuyển động sang phải
    
    
    
    bullet = list()
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        
        # nạp hình ảnh nhân vật di chuyển sang phải
        set_sheet= set_sprite('cat',cg.State,"Left")

        set_sheet.get_image()

        self.frames_l = cg.frame_state_l
        
        set_sheet= set_sprite('cat',cg.State,"Right")
        
        set_sheet.get_image()

        self.frames_r = cg.frame_state_r

   
        # nạp hình ảnh nhân vật di chuyển sang trái
        self.change_x = 0
        self.change_y = 0
        self.vi_tri = [0, 0] 
        self.vi_tri_bd = self.vi_tri
        self.direction = "Left"
        self.state = "Run"
        self.va_cham =""
        # 
        # đặt khung hình nhân vật mới bắt đầu là khung 4
        # 
        self.image = self.frames_l[self.state][0]
        
        #
        #lấy diện tích của khung ảnh nhân vật
        self.rect = self.image.get_rect()

        
        self.feet = pygame.Rect(0, 0,60, 90)

        
        
   

    def update(self, dt): 

        """ cập nhật lại nhân vật """

        self.vi_tri_bd = self.vi_tri[:]

        self.vi_tri[0] += self.change_x  # chiều ngang
        
        self.vi_tri[1] += self.change_y # chiều cao 
        
        self.rect.topleft= self.vi_tri
        self.feet.midbottom = self.rect.midbottom
        

        # update hình ảnh nhân vật
        
        if self.direction == "Left" :
           time_step = (pygame.time.get_ticks()/70)% (len(self.frames_l[self.state])-1)  
           print(f"Left {self.state} : {int(time_step)}")
           self.image = self.frames_l[self.state][int(time_step)]
        elif self.direction == "Right" :
           time_step = (pygame.time.get_ticks()/70)% (len(self.frames_r[self.state])-1)  
           print(f"Rigth {self.state} : {int(time_step)}")
           self.image = self.frames_r[self.state][int(time_step)] 

    def move_back(self, dt):
        self.vi_tri[1] = self.vi_tri_bd[1]
        self.rect.topleft = self.vi_tri
        self.feet.midbottom = self.rect.midbottom

    def go_left (self,dt):
        self.change_x = -4
        self.direction = "Left"
        self.state ="Run"

    def go_right(self,dt) : 
        self.change_x = 4
        self.direction = "Right"
        self.state ="Run"

    def jump (self,dt) : 
        
        self.change_y = -12
        self.state ="Jump"
    def stop(self,dt):
        self.change_y = 0 
        self.change_x = 0 
        self.state = "Idle"
        print("stop")

        