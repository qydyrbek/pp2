#Imports
import pygame, sys
from pygame.locals import *
import random, time
import math

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
COIN_SIZE = 35
SPEED = 5
SCORE = 0
balance = 0
background_speed = 10


#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)


#background
background = pygame.image.load("materialsforex1/AnimatedStreet.png")
bg_y = 0
#second background
background2 = pygame.image.load("materialsforex1/AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

#declaring an enemy class
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("materialsforex1/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 690):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

#declaring a player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("materialsforex1/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

#declaring a coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("materialsforex1/coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(COIN_SIZE,SCREEN_WIDTH-COIN_SIZE), 0) 
    
    def move(self):
        global balance
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            self.randomize_position()

    def randomize_position(self):
        self.rect.center = (random.randint(COIN_SIZE, SCREEN_WIDTH-COIN_SIZE), random.randint(0, SCREEN_HEIGHT-2*COIN_SIZE))


#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
coins.add(C1)


#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:
    
      
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    #display the scores
    DISPLAYSURF.blit(background, (0, bg_y))
    DISPLAYSURF.blit(background2, (0, bg_y - SCREEN_HEIGHT))
    bg_y += background_speed
    if bg_y >= SCREEN_HEIGHT:
        bg_y = 0
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,0))
    show_balance = font_small.render("Balance: " + str(balance), True, BLACK)
    DISPLAYSURF.blit(show_balance, (270, 0))


    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)


    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('materialsforex1\crash.wav').play()
                   
        DISPLAYSURF.blit(game_over, (30,250))
          
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
            time.sleep(3)
            pygame.quit()
            sys.exit()

    
     
    #To be run if collision occurs between Player and Coin
    for coin in pygame.sprite.spritecollide(P1, coins, True):
        pygame.mixer.Sound('materialsforex1\pfall_coin.mp3').play()
        balance += 1
        C1 = Coin()
        coins.add(C1)
        all_sprites.add(C1)
    
    #updating the display
    pygame.display.update()
    FramePerSec.tick(FPS)
