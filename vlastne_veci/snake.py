import pygame
import random

# Initialize Pygame
pygame.init()

# Set the screen size
SCREEN_SIZE = (800, 600)

# Set the screen
screen = pygame.display.set_mode(SCREEN_SIZE)

# Set the title
pygame.display.set_caption("Snake Game")

# Set the font
font = pygame.font.Font(None, 36)

# Set the direction of the snake
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Set the snake initial position
snake_position = [100,100]

# Set the snake body
snake_body = [[100,100],[90,100],[80,100]]

# Set the initial direction of the snake
direction = RIGHT

# Set the food position
food_position = [random.randrange(1, (SCREEN_SIZE[0]//10)) * 10, random.randrange(1, (SCREEN_SIZE[1]//10)) * 10]
food_spawn = True

# Set the score
score = 0

# Set the game over flag
game_over = False

# Set the clock
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = UP
            elif event.key == pygame.K_DOWN:
                direction = DOWN
            elif event.key == pygame.K_LEFT:
                direction = LEFT
            elif event.key == pygame.K_RIGHT:
                direction = RIGHT

    # Change the snake position
    if direction == UP:
        snake_position[1] -= 10
    elif direction == DOWN:
        snake_position[1] += 10
    elif direction == LEFT:
        snake_position[0] -= 10
    elif direction == RIGHT:
        snake_position[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()
        
    if not food_spawn:
        food_position = [random.randrange(1, (SCREEN_SIZE[0]//10)) * 10, random.randrange(1, (SCREEN_SIZE[1]//10)) * 10] 
    food_spawn = True
    
    screen.fill((0,0,0))
    
    for pos in snake_body:
        pygame.draw.rect(screen, (0,255,0), pygame.Rect(pos[0], pos[1], 10, 10))
        
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(pos[0], pos[1], 10, 10))
