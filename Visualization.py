import pygame
import json


with open("Murder-on-the-2nd-Floor-Raw-Data.json") as file:
    data = json.load(file)

pygame.init()
pygame.font.init()

window_width = 745
window_height = 744

animation_increment = 10
clock_tick_rate = 20

size = (window_width, window_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Richcraft Hall Hotel Surveillance Footage")

complete = False

clock = pygame.time.Clock()
background_image = pygame.image.load("Floor-Plan.png").convert()

my_font = pygame.font.SysFont('Comic Sans MS', 30)

screen.blit(background_image, [0, 0])

paused = False

while not complete:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            complete = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    paused = False
                else:
                    paused = True

    if not paused:
        #do nothing
        pass
    else:
        for event in data:
            time = my_font.render("Time: " + event, False, (0, 0, 0))
            screen.blit(time, (0,0))



    pygame.display.flip()
    clock.tick(clock_tick_rate)