
#Main code for BreakPong 
#Additional parts of code will be modified from this
import pygame 
from pygame.locals import *
import random
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
        self.rect=self.surf.get_rect(
                center=(
                    width/4, height/2,
                    )
                )
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
        self.rect=self.surf.get_rect(
                center=(
                    (3*width)/4, height/2,
                    )
                )
    def update(self, pressed_keys):
        if pressed_key[K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if self.rect.top <= 0:
            self.rect.top=0
        elif self.rect.bottom >= height:
            self.rect.bottom=height
class Block(pygame.sprite.Sprite):
    def __init__(self):
        super(Block, self).__init__()
        self.surf= #block surface
        self.rect= self.surf.get_rect(
                center=(
                    #positions of the blocks
                    )
                )
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.surf= #ball surface
        self.rect=self.surf.get_rect()
        self.speed=random.randint(-20, 20)
        self.reflect=-self.speed
    def update(self):
        self.rect.move_ip(self.speed, self.speed)
        if self.rect.right < 0:
            self.kill()
        elif self.rect.left > width:
            self.kill()
        if self.rect.top <= 0:
            self.rect.move_ip(self.speed, random.randint(0,20))
        elif self.rect.bottom >= height:
            self.rect.move_op(self.speed, random.randint(-20,0))
player1=Player1()
player2=Player2()

block=pygame.sprite.Group()
ball=Ball()
all_sprites=pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(player2)
all_sprites.add(ball)

running=True

While running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running=False
        elif event.type == QUIT:
            running=False
    pressed_keys=pygame.key.get_pressed()
    player1.update(pressed_keys)
    player2.update(pressed_keys)

    ball.update()

    screen.fill((0,0,0))

    for entity in all_sprites:
        screen.blit(entitiy.surf, entity.rect)

    if pygame.sprite.spritecollideany(ball, block):
        block.kill()
        ball.rect.move_ip(ball.reflect,ball.speed)
    elif pygame.sprite.spritecollideany(ball, player1, player2):
        ball.rect.move_ip(ball.reflect,ball.speed)

    pygame.display.flip()
    fpsClock.tick(fps)


