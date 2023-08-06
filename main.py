import pygame
import sys
import random

# Constants Declaration.....
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 640
TITLE_SIZE = 32
SPEED = 3
SCORE = 0

# Initialize Pygame Module
pygame.init()

# Screen caption
pygame.display.set_caption('Apple Catcher')

# Define Game Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define Clock for FPS
clock = pygame.time.Clock()

# Font
font = pygame.font.Font('./assets/PixeloidMono.ttf', TITLE_SIZE)

# DRAW : Background, Player & Floor
def draw():
    global SCORE 

    screen.fill('aqua')
    screen.blit(player_image, player_rect)
    screen.blit(floor_image, floor_rect)

    for apple in apples:
        screen.blit(apple.image, apple.rect)

    score_text = font.render(f'Score: {SCORE}', True, 'blue')

    screen.blit(score_text, (5, 5))

# Floor
floor_image = pygame.image.load('./assets/floor.png').convert_alpha()
floor_image = pygame.transform.scale(floor_image, (TITLE_SIZE*10, TITLE_SIZE*5))
floor_rect = floor_image.get_rect(bottomleft = (0, screen.get_height()))

# Player
player_image = pygame.image.load('./assets/player_static.png').convert_alpha()
player_image = pygame.transform.scale(player_image, (TITLE_SIZE, TITLE_SIZE*2))
player_rect = player_image.get_rect(center = (SCREEN_WIDTH // 2, 
                                              screen.get_height()-floor_image.get_height()-player_image.get_height()//2
                                             ))

# Apple
apple_image = pygame.image.load('./assets/apple.png').convert_alpha()
apple_image = pygame.transform.scale(apple_image, (TITLE_SIZE, TITLE_SIZE))

class Apple:
    def __init__(self, image, position, speed):
        self.image = image
        self.rect = self.image.get_rect(topleft = position)
        self.speed = speed
    def move(self):
        self.rect.y += self.speed

apples = [
    Apple(apple_image, (100, 0), SPEED),
    Apple(apple_image, (200, 0), SPEED)
]

running = True

def apple_movement():
    global SPEED
    global SCORE 

    for apple in apples:
        apple.move()

        if apple.rect.colliderect(floor_rect):
            apples.remove(apple)
            apples.append(Apple(apple_image, (random.randint(50, 300), -50), SPEED))

        elif apple.rect.colliderect(player_rect):
            apples.remove(apple)
            apples.append(Apple(apple_image, (random.randint(50, 300), -50), SPEED))
            SPEED += 0.2
            SCORE += 1

def player_movement():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_rect.x -= 4
    if keys[pygame.K_RIGHT]:
        player_rect.x += 4

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw()
    apple_movement()
    player_movement()
    clock.tick(60)
    pygame.display.update()