from tracemalloc import start
import pygame
import os

WIDTH, HEIGHT = 1000, 600
FPS = 120
VEL = 40
SPEEDSTER_WIDTH, SPEEDSTER_HEIGHT = 300, 250
BURGER_WIDTH, BURGER_HEIGHT = 30, 30
SOUNDTRACK = '/Users/jhonny/Documents/Programming/VegasDesertPursuit/Assets/soundtrack.wav'

ROAD_FRAME_1 = pygame.image.load(os.path.join(
    '/Users/jhonny/Documents/Programming/VegasDesertPursuit/Assets/roadFrame1.png'))
ROAD1 = pygame.transform.scale(
    ROAD_FRAME_1, (WIDTH, HEIGHT))
ROAD_FRAME_2 = pygame.image.load(os.path.join(
    '/Users/jhonny/Documents/Programming/VegasDesertPursuit/Assets/roadFrame2.png'))
ROAD2 = pygame.transform.scale(
    ROAD_FRAME_2, (WIDTH, HEIGHT))
ROAD_FRAME_3 = pygame.image.load(os.path.join(
    '/Users/jhonny/Documents/Programming/VegasDesertPursuit/Assets/roadFrame3.png'))
ROAD3 = pygame.transform.scale(
    ROAD_FRAME_3, (WIDTH, HEIGHT))
ROAD_FRAME_4 = pygame.image.load(os.path.join(
    '/Users/jhonny/Documents/Programming/VegasDesertPursuit/Assets/roadFrame4.png'))
ROAD4 = pygame.transform.scale(
    ROAD_FRAME_4, (WIDTH, HEIGHT))
ROAD_FRAME_5 = pygame.image.load(os.path.join(
    '/Users/jhonny/Documents/Programming/VegasDesertPursuit/Assets/roadFrame5.png'))
ROAD5 = pygame.transform.scale(
    ROAD_FRAME_5, (WIDTH, HEIGHT))
ROAD_FRAME_6 = pygame.image.load(os.path.join(
    '/Users/jhonny/Documents/Programming/VegasDesertPursuit/Assets/roadFrame6.png'))
ROAD6 = pygame.transform.scale(
    ROAD_FRAME_6, (WIDTH, HEIGHT))
ROAD_FRAME_7 = pygame.image.load(os.path.join(
    '/Users/jhonny/Documents/Programming/VegasDesertPursuit/Assets/roadFrame7.png'))
ROAD7 = pygame.transform.scale(
    ROAD_FRAME_7, (WIDTH, HEIGHT))
ROAD_FRAME_8 = pygame.image.load(os.path.join(
    '/Users/jhonny/Documents/Programming/VegasDesertPursuit/Assets/roadFrame8.png'))
ROAD8 = pygame.transform.scale(
    ROAD_FRAME_8, (WIDTH, HEIGHT))
RED_SPEEDSTER_IMAGE = pygame.image.load(os.path.join(
    '/Users/jhonny/Documents/Programming/VegasDesertPursuit/Assets/brgrbySpeedsterBack.png'))
RED_SPEEDSTER = pygame.transform.scale(
    RED_SPEEDSTER_IMAGE, (SPEEDSTER_WIDTH, SPEEDSTER_HEIGHT))

FALLING_BURGER_IMAGE = pygame.image.load(os.path.join(
    '/Users/jhonny/Documents/Programming/VegasDesertPursuit/Assets/burger.png'))
FALLING_BURGER = pygame.transform.scale(
    FALLING_BURGER_IMAGE, (BURGER_WIDTH, BURGER_HEIGHT))


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > 100:  # left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x - VEL < 600:  # right
        red.x += VEL
    # if keys_pressed[pygame.K_UP] and red.y - VEL > 250:  # up
    #     red.y -= VEL
    # if keys_pressed[pygame.K_DOWN] and red.y - VEL < 315:  # down
    #     red.y += VEL


# MAIN
pygame.init()
screen = pygame.display.set_mode((128, 128))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Impact", 64)
red = pygame.Rect(300, 325, SPEEDSTER_WIDTH, SPEEDSTER_HEIGHT)
surface_type = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE
window = pygame.display.set_mode((WIDTH, HEIGHT), surface_type)
pygame.display.set_caption("DESERT PURSUIT")

# Variables to manage the background change
background_delay = 20  # milliseconds
background_time = 0     # when the background last changed
backgrounds = [ROAD1, ROAD2, ROAD3, ROAD4, ROAD5, ROAD6, ROAD7, ROAD7, ROAD8]
background_index = 0     # index of the currently used background


def draw_window(red):
    window.blit(RED_SPEEDSTER, (red.x, red.y))
    pygame.display.update()


start_time = pygame.time.get_ticks()
# Main loop
clock = pygame.time.Clock()
done = False
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
pygame.mixer.init()
pygame.mixer.music.load(SOUNDTRACK)
pygame.mixer.music.play(10)
while not done:

    # Handle user-input
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            done = True

    # Re-draw the screen background from the list after a delay
    time_now = pygame.time.get_ticks()
    counting_time = pygame.time.get_ticks() - start_time

    # change milliseconds into minutes, seconds, milliseconds
    # counting_minutes = str(counting_time/60000).zfill(2)
    counting_seconds = str((counting_time % 60000)/1000).zfill(2)

    counting_string = "%s" % (counting_seconds)

    counting_text = font.render(
        str(counting_string), 1, (255, 255, 255))
    counting_rect = counting_text.get_rect(center=screen.get_rect().center)

    screen.fill((0, 0, 0))
    screen.blit(counting_text, counting_rect)

    if (time_now > background_time + background_delay):
        # switch to the next background
        background_time = time_now
        background_index += 1
        # if we're out of backgrounds, start back at the head of the list
        if (background_index >= len(backgrounds)):
            background_index = 0

    # Draw the background
    window.blit(backgrounds[background_index], (0, 0))
    window.blit(RED_SPEEDSTER, (red.x, red.y))
    keys_pressed = pygame.key.get_pressed()
    red_handle_movement(keys_pressed, red)
    draw_window(red)
    screen.blit(counting_text, counting_rect)
    pygame.display.flip()
    pygame.display.update()
    clock.tick(25)
    # Update the window, but not more than 60fps
    clock.tick_busy_loop(60)

pygame.quit()
