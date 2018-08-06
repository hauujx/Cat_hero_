""" Quest - An epic journey.

Simple demo that demonstrates PyTMX and pyscroll.

requires pygame and pytmx.

https://github.com/bitcraft/pytmx

pip install pytmx
"""
import os.path

import pygame
from pygame.locals import *
from pytmx.util_pygame import load_pygame

import pyscroll
import pyscroll.data
from pyscroll.group import PyscrollGroup
from chapater import Hero

# define configuration variables here
RESOURCES_DIR = 'data'

HERO_MOVE_SPEED = 2.5 # pixels per second
MAP_FILENAME = 'winter_map.tmx'


# simple wrapper to keep the screen resizeable
def init_screen(width, height):
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    return screen


# make loading maps a little easier
def get_map(filename):
    return os.path.join(RESOURCES_DIR, filename)


# make loading images a little easier
def load_image(filename):
    return pygame.image.load(os.path.join(RESOURCES_DIR, filename)).convert()


class QuestGame(object):
    """ This class is a basic game.

    This class will load data, create a pyscroll group, a hero object.
    It also reads input and moves the Hero around the map.
    Finally, it uses a pyscroll group to render the map and Hero.
    """
    filename = get_map(MAP_FILENAME)

    def __init__(self):

        # true while running
        self.running = True
        self.time_step = 0
        # load data from pytmx
        tmx_data = load_pygame(self.filename)

        # setup level geometry with simple pygame rects, loaded from pytmx
        self.walls = list()
        for object in tmx_data.objects:
            self.walls.append(pygame.Rect(
                object.x, object.y,
                object.width, object.height))

        # create new data source for pyscroll
        map_data = pyscroll.data.TiledMapData(tmx_data)

        # create new renderer (camera)
        screens=screen.get_size()
        self.map_layer = pyscroll.BufferedRenderer(map_data,(10,40) , clamp_camera=True, tall_sprites=1)
        self.map_layer.zoom = 0.75

        # pyscroll supports layered rendering.  our map has 3 'under' layers
        # layers begin with 0, so the layers are 0, 1, and 2.
        # since we want the sprite to be on top of layer 1, we set the defaultmm m,m
        # layer for sprites as 2
        self.group = PyscrollGroup(map_layer=self.map_layer, default_layer=3)

        self.hero = Hero()


        # put the hero in the center of the map
        
        self.hero._position[0] += 200
        self.hero._position[1] += 100

                # add our hero to the group
        self.group.add(self.hero)

        self.map_layer.set_size(screens)

    def draw(self, surface):

        # center the map/screen on our Hero
        self.group.center(self.hero.rect)

        # draw the map and all sprites
        self.group.draw(surface)

    def handle_input(self,dt):
        """ Handle pygame input events
        """
        



        
        
        for event in pygame.event.get():
           if event.type ==pygame.QUIT:
                self.running = False
           if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.hero.velocity[0] = -HERO_MOVE_SPEED
                    self.hero.direction = "Left"
                    self.hero.state ="Fall"
                    print(event.type)
                if event.key == pygame.K_RIGHT:
                    self.hero.velocity[0] = HERO_MOVE_SPEED
                    self.hero.direction = "Right"


                    self.hero.state ="Run"
                    print(event.type)
                if event.key == pygame.K_UP:
                    self.hero.velocity[1] =  -12
                    self.hero.state ="Jump"
                    print(event.type)
                
           else:
                self.hero.velocity[0] = 0
                self.hero.velocity[1] = 0
                self.hero.state ="Idle"
            # this will be handled if the window is resized
        

        # using get_pressed is slightly less accurate than testing for events
        # but is much easier to use.
         # User did something
             # Flag that we are done so we exit this loop
            
                    
             
             

    def update(self, dt):
        """ Tasks that occur over time should be handled here
        """
        self.group.update(dt)

        # check if the sprite's feet are colliding with wall
        # sprite must have a rect called feet, and move_back method,
        # otherwise this will fail
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) >-1:
                self.hero.move_back(dt)
                print(sprite)
            else:
                self.hero._position[1] += 3.35
                




    def run(self):
        """ Run the game loop
        """
        clock = pygame.time.Clock()
        self.running = True

        from collections import deque
        times = deque(maxlen=30)

        try:
            while self.running:
                dt = clock.tick() / 1000.
                times.append(clock.get_fps())
                #print(sum(times)/len(times))


                self.handle_input(dt)
                self.update(dt)
                self.draw(screen)
                pygame.display.flip()


        except KeyboardInterrupt:
            self.running = False


if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    screen = init_screen(800, 640)
    pygame.display.set_caption('ví dụ lập trình game với PyTMX và pyscroll + sheet sprite')

    try:
        game = QuestGame()
        game.run()
    except:
        pygame.quit()
        raise
