import pygame
import random
import os


print("Current working directory:", os.getcwd())

os.chdir("c:/Users/datun/Desktop/goa homeworks/trash game")

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 1200
window_height = 875

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Money Catcher")

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Set up the font
font = pygame.font.SysFont(None, 30)

# Load the images
background_image = pygame.image.load("background_scifi2.png").convert()
game_over_background = pygame.image.load("goa_text_background.png").convert()
money_image = pygame.image.load("images.png").convert_alpha()
money_image = pygame.transform.scale(money_image, (100, 200))
jail_image = pygame.image.load("image.jpg").convert_alpha()
jail_image = pygame.transform.scale(jail_image, (200, 100))
player_image = pygame.image.load("image1.jpg").convert_alpha()
player_image = pygame.transform.scale(player_image, (150, 150))

game_over_screen = pygame.Surface((window_width, window_height))
game_over_screen.blit(game_over_background, (0, 0))




# Set up the game clock
clock = pygame.time.Clock()

# Set up the game variables
player_x = 400
player_y = 750
player_speed = 20
money_list = []
jail_list = []
score = 0

# Set up the game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < window_width - money_image.get_width():
        player_x += player_speed

    # Spawn money and jail
    if random.randint(1, 100) == 1:
        money_list.append(pygame.Rect(random.randint(0, window_width - money_image.get_width()), -
                          money_image.get_height(), money_image.get_width(), money_image.get_height()))
    if random.randint(1, 200) == 1:
        jail_list.append(pygame.Rect(random.randint(0, window_width - jail_image.get_width()), -
                         jail_image.get_height(), jail_image.get_width(), jail_image.get_height()))

    # Move money and jail
    for money in money_list[:]:
        money.move_ip(0, 5)
    for jail in jail_list:
        jail.move_ip(0, 5)

    # Check for collisions
    for money in money_list[:]:
        if money.colliderect(pygame.Rect(player_x, player_y, money_image.get_width(), money_image.get_height())):
            score += 1
            money_list.remove(money)

    for jail in jail_list[:]:
        if jail.colliderect(pygame.Rect(player_x, player_y, jail_image.get_width(), jail_image.get_height())):
            running = False
    # Draw the screen
    window.blit(background_image, (0, 0))
    for money in money_list:
        window.blit(money_image, money)
    for jail in jail_list:
        window.blit(jail_image, jail)
    window.blit(font.render("Score: " + str(score), True, black), (10, 10))
    window.blit(player_image, (player_x, player_y))
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Game over screen
game_over_screen = pygame.Surface((window_width, window_height))
game_over_screen.blit(game_over_background, (0, 0))
game_over_text = font.render(
    "GOA was accidentally thrown in the trash by an absolute moron", True, red, black, )
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (window_width // 2, window_height // 2 - 150)
game_over_screen.blit(game_over_text, game_over_rect)
window.blit(game_over_screen, (0, 0))

score_text = font.render("NOVATORI thrown in trash: " + str(score), True, white)
score_rect = score_text.get_rect()
score_rect.center = (window_width // 2, window_height // 2 + 115)
window.blit(score_text, score_rect)

pygame.display.update()

# Wait for the player to close the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
