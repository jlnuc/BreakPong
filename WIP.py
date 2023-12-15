#libraries
import pygame
import random

#Controls
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_w,
    K_s,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#Size
width = 1280
height = 500

#Color...
WHITE = (255, 255, 255)

#Score counter lol
score1 = 0
score2 = 0

#Classes
#P1
class Player1(pygame.sprite.Sprite):
    def __init__(self):
        super(Player1, self).__init__()
        self.surf = pygame.Surface((10, 70)) #Rect Size
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
            center=(
                width/4, height/2 #Rect Location
            )
        )

    #Movement
    def update(self, pressed_keys):
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 5)
    #Borders
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= height:
            self.rect.bottom = height

#P2
class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super(Player2, self).__init__()
        self.surf = pygame.Surface((10, 70)) #Rect Size 10,70
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
            center=(
                (3*width)/4, height/2 #Rect Location
            )
        )

    #Movement
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
    #Borders
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= height:
            self.rect.bottom = height
#Bricks
class Brick(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.surf = pygame.Surface([width, height])
        self.surf.fill(WHITE)
        self.surf.set_colorkey(WHITE)
        pygame.draw.rect(self.surf, color, [0, 0, width, height])
        self.rect = self.surf.get_rect()
    def update(self):
        if self.rect.colliderect(ball):
            self.kill()
#Ball
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.surf = pygame.Surface((5,5)) #Ball Size
        self.surf.fill((255,255,255)) #Ball Color
        self.rect = self.surf.get_rect(
            center=(
                (width/2,height/2)
            )
        )
        #These variables down here are for changing up the initial direction for more varied gameplay.
        rng1=random.randrange(0,2) #RNG for the initial X direction.
        rng2=random.randrange(0,2) #RNG for the initial Y direction.
        if rng1 == 1:
            Xinit=-1
        if rng1 == 0:
            Xinit=1
        if rng2 == 1:
            Yinit=-1
        if rng2 == 0:
            Yinit=1

        self.speed = random.randrange(2,6)*Xinit #Ball X Speed with variation
        self.reflect = random.randrange(2,6)*Yinit #Ball Y Speed with variation

    #There may be a slight bug where the ball disappears near the paddle when hitting the roof when I used a random number, couldn't figure it out.    
    def update(self): 
        self.rect.move_ip(self.speed, self.reflect)#Move the ball using x and y
        if self.rect.right < 0: #If ball gets off screen to the right reset.
            self.__init__()
        if self.rect.left > width: #If ball gets off screen to the left reset.
            self.__init__()
        if self.rect.top < 0: #If ball hits the top, change the y value to the opposite sign
            self.reflect = -self.reflect
        elif self.rect.bottom > height: #If ball hits the bottom, change the y value to the opposite sign
            self.reflect = -self.reflect
        
        if self.rect.colliderect(player1): #If ball hits player1, change the x value
            self.speed = -self.speed
        elif self.rect.colliderect(player2): #If ball hits player2, change the x value
            self.speed = -self.speed
        elif self.rect.colliderect(brick):
            self.speed = -self.speed


#Start Game

pygame.init() #Initialize game
clock = pygame.time.Clock() #The Clock
screen = pygame.display.set_mode((width,height)) #Make Screen

player1 = Player1() #Create player1
player2 = Player2() #Create player2
ball = Ball() #Create Ball

all_sprites = pygame.sprite.Group() #Create a group for the sprites
balls = pygame.sprite.Group() #Group the balls when creating them
all_sprites.add(player1) #Make player1 Visible
all_sprites.add(player2) #Make player2 Visible

bricks = pygame.sprite.Group()
for j in range(3):
    for i in range(5):
        brick = Brick(WHITE, 50, 30)
        brick.rect.x = 1 - j*70
        brick.rect.y = 40 + i*40
        all_sprites.add(brick)
        bricks.add(brick)
for k in range(3):
    for l in range(5):
        brick = Brick(WHITE, 50, 30)
        brick.rect.x = 100 + k*70
        brick.rect.y = 40 + l*40
        all_sprites.add(brick)
        bricks.add(brick)

ADDBALL = pygame.USEREVENT +1 #AddBall Event
add_ball = pygame.event.Event(ADDBALL) #Assigning it as an event


running = True 
pygame.event.post(add_ball) #Add a event at the end of the list for the ball

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN: 
            if event.key == K_ESCAPE: #ESC = Exit
                running = False
        elif event.type == QUIT: #X Key = Exit
            running = False
        elif event.type == ADDBALL: #Adding ball event
            new_ball = Ball()
            balls.add(new_ball)
            all_sprites.add(new_ball)
    if ball.rect.right < 0 or ball.rect.left > width: #reset when ball get to that point
        bricks.kill()
        for j in range(3):
            for i in range(5):
                brick = Brick(WHITE, 50, 30)
                brick.rect.x = 1 - j*70
                brick.rect.y = 40 + i*40
                all_sprites.add(brick)
                bricks.add(brick)
        for k in range(3):
            for l in range(5):
                brick = Brick(WHITE, 50, 30)
                brick.rect.x = 100 + k*70
                brick.rect.y = 40 + l*40
                all_sprites.add(brick)
                bricks.add(brick)
    if ball.rect.right < 0:
        score2 = score2 + 1
    if ball.rect.left > width:
        score1 = score1 + 1


    pressed_keys = pygame.key.get_pressed()
    player1.update(pressed_keys) #Player 1 Keys (W and S)
    player2.update(pressed_keys) #Player2 Keys (Up and Down Arrow)
    ball.update() #Update ball to move
    bricks.update() #checking if hit

    screen.fill((0,0,0)) #Make the background black

    #Score stuff
    font = pygame.font.Font(None, 34)
    text = font.render("P1 Score: " + str(score1), 1, WHITE)
    screen.blit(text, (20, 10))
    text = font.render("P2 Score: " + str(score2), 1, WHITE)
    screen.blit(text, (650, 10))
                
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect) #Make every single sprite visible
    
    pygame.display.flip()
    clock.tick(60) #FPS

