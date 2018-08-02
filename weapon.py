import pygame
from set_sprite import set_sprite

class wp(pygame.sprite.Sprite):
   size_frames = {
    "walk_r" : [(0, 0, 240, 90),
                (66, 0, 66, 90),
                (132, 0, 67, 90),
                (0, 93, 66, 90),
                (66, 93, 66, 90),
                (132, 93, 72, 90),
                (0, 186, 70, 90)],
                }
   def __init__(self):	
    pygame.sprite.Sprite.__init__(self)
    self.velocity = [100, 0] 
    self._position = [400,800]
    self._old_position = self._position[:]
    self.size= self.size_frames.get('walk_r')
    # nạp hình ảnh nhân vật di chuyển sang phải
    self.frames_r= set_sprite("part.png",self.size).get_image()
    self.image = self.frames_r[0]
    #
    #lấy diện tích của khung ảnh nhân vật
    self.rect = self.image.get_rect()
    self._position[0] += 400
    print(self.rect.x)
    print(self.rect.y)
    self.feet = pygame.Rect(0, 0,40,40)
   def update(self,dt):
    self.rect.topleft = self._position
   def move_back(self, dt):
        """ If called after an update, the sprite can move back
        """
        self._position = self._old_position
        self.rect.topleft = self._position
      
        

    
        