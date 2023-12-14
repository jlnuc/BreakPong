#libraries
import pygame
import random
import pygame.freetype

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

#Scoreboard
score1 = 0 #Initialize the score for P1
score2 = 0 #Initialize the score for P2



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
        #Globalize the scores so they can be used in here
        global score1
        global score2

        self.rect.move_ip(self.speed, self.reflect)#Move the ball using x and y
        if self.rect.right < 0: #If ball gets off screen to the right reset.
            self.__init__()
            score1 +=1
        if self.rect.left > width: #If ball gets off screen to the left reset.
            self.__init__()
            score2 +=1
        if self.rect.top < 0: #If ball hits the top, change the y value to the opposite sign
            self.reflect = -self.reflect
        elif self.rect.bottom > height: #If ball hits the bottom, change the y value to the opposite sign
            self.reflect = -self.reflect
        
        if self.rect.colliderect(player1): #If ball hits player1, change the x value
            self.speed = -self.speed
        elif self.rect.colliderect(player2): #If ball hits player2, change the x value
            self.speed = -self.speed


#Start Game

pygame.init() #Initialize game
clock = pygame.time.Clock() #The Clock
screen = pygame.display.set_mode((width,height)) #Make Screen

player1 = Player1() #Create player1
player2 = Player2() #Create player2
ball = Ball() #Create Ball

all_sprites = pygame.sprite.Group() #Create a group for the sprites
ball = pygame.sprite.Group() #Group the balls when creating them
all_sprites.add(player1) #Make player1 Visible
all_sprites.add(player2) #Make player2 Visible


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
            ball.add(new_ball)
            all_sprites.add(new_ball)


    pressed_keys = pygame.key.get_pressed()
    player1.update(pressed_keys) #Player 1 Keys (W and S)
    player2.update(pressed_keys) #Player2 Keys (Up and Down Arrow)
    ball.update() #Update ball to move

    screen.fill((0,0,0)) #Make the background black
    font = pygame.font.SysFont("ariel", 20) #Setting a font
    scoreboard1 = font.render("P1 = "+str(score1), 1, (255,255,255)) #Displaying score for P1
    scoreboard2 = font.render("P2 = "+str(score2), 1, (255,255,255)) #Displaying score for P2
    screen.blit(scoreboard1, (5, 10)) # The scoreboard updates but I can't figure out how
    screen.blit(scoreboard2, (5, 30)) # to get the score to increase when the ball goes to each x-axis border

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect) #Make every single sprite visible
    
    pygame.display.flip()
    clock.tick(60) #FPS
