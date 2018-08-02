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
        set_sheet= set_sprite('cat',cg.State)
        set_sheet.get_image()
        self.frames_l = cg.frame_state
        print(self.frames_l)
        # nạp hình ảnh nhân vật di chuyển sang trái
        self.velocity = [0, 0] 
        self._position = [0, 0]
        self._old_position = self.position
        self.direction = "Right"
        self.state = "Run"

        # 
        # đặt khung hình nhân vật mới bắt đầu là khung 4
        # 
        self.image = self.frames_l[self.state][0]
        
        #
        #lấy diện tích của khung ảnh nhân vật
        self.rect = self.image.get_rect()

        
        self.feet = pygame.Rect(0, 0,60, 90)


        
    @property
    def position(self):
        return list(self._position)

    @position.setter
    def position(self, value):
        self._position = list(value)

    def update(self, dt): 

        """ cập nhật lại nhân vật """
        self._old_position = self._position[:]

        self._position[0] +=self.velocity[0]  # chiều ngang
        
        self._position[1] += self.velocity[1]  # chiều cao 
        
        self.rect.topleft = self._position
        self.feet.midbottom = self.rect.midbottom
        time_step = (pygame.time.get_ticks()/70)% (len(self.frames_l[self.state])-1)
        
        
         
         
        print(f"{self.state} :",int(time_step))
        self.image = self.frames_l[self.state][int(time_step)]
        
        
        

    def move_back(self, dt):
        
        
        self._position[1] = self._old_position[1]
        self.rect.topleft = self._position
        
        self.feet.midbottom = self.rect.midbottom
    

