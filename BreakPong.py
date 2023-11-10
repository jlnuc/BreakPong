
#Main code for BreakPong 
#Additional parts of code will be modified from this
import pygame 
from pygame.locals import *
pygame.init()
#fps lock I believe
fps=60
fpsClock=pygame.time.Clock()
#Screen
size=width, height= 1280, 920
screen=pygame.display.set_mode(size)
#player sprite/collision
class Player1(pygame.sprite.Sprite):
    def __init__(self):
        super(Player1, self).__init__()
        self.surf=    #please fill in with something likely just make a couple of squares
        self.rect=self.surf.get_rect()
    def update(self, pressed_keys):
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 5)
        if self.rect.top <= 0:
            self.rect.top=0
        elif self.rect.bottom >= height:
            self.rect.bottom=height
class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super(Player2, self).__init__()
        self.surf= #same as P1
        self.rect=self.surf.get_rect()
    def update(self, pressed_keys):
        if pressed_key[K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if self.rect.top <= 0:
            self.rect.top=0
        elif self.rect.bottom >= height:
            self.rect.bottom=height

