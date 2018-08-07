"""
cắt hình ảnh của nhân vật

"""
import pygame 
import os.path
import config as cg 

filename = cg.DIR_CT
def load_image(filename):
    return pygame.image.load(os.path.join(cg.DIR,filename)).convert()

class set_sprite(object): 
  #  nhân vật ,hành động , hướng ,size (lớn,nhỏ ) 
    def __init__(self,character,action,dicrection=None,size=None):
      self.character = character
      self.State = action
      self.select_size = size
      self.size_frame = cg.Size_frames[character]
      self.dicrection = dicrection

      
    def get_image(self):
        
        for j in range(0,len(self.State)):
          
          for i in range(0,len(self.size_frame)):
            filename = cg.DIR_CT+cg.CHAR[self.character]+"\\"+self.State[j]+f"\\{self.State[j]} ({i+1}).png"
            sprite_sheet = load_image(filename)
            width = self.size_frame[self.State[j]][i][2] 
            height = self.size_frame[self.State[j]][i][3] 
            x = self.size_frame[self.State[j]][i][0] 
            y = self.size_frame[self.State[j]][i][1]
          # tạo con mẹ nó lớp mặt nạ -
            image = pygame.Surface([width, height]).convert()

      # copy cái hình muốn cắt vào lớp mặt nạ
            image.blit(sprite_sheet, (0, 0), (x, y, width, height))

      # xóa toàn bộ màu đen ( #màu đen 0,0,0 )
            image.set_colorkey((0,0,0))
            if self.dicrection == "Left" :
              image = pygame.transform.flip(image, True, False)
              cg.frame_state_l[self.State[j]].append(image)
            elif self.dicrection == "Right":
              cg.frame_state_r[self.State[j]].append(image)
    
        
