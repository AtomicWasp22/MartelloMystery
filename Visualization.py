import pygame
import json
import data_loader
import datetime
import time

device_inventory = data_loader.load_data()


with open("Murder-on-the-2nd-Floor-Raw-Data.json") as file:
    data = json.load(file)

pygame.init()
pygame.font.init()

window_width = 1200
window_height = 744

clock_tick_rate = 20

size = (window_width, window_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Richcraft Hall Hotel Surveillance Footage")

complete = False

clock = pygame.time.Clock()
background_image = pygame.image.load("Floor-Plan.png").convert()

timer_font = pygame.font.SysFont('Comic Sans MS', 30)
name_font = pygame.font.SysFont('Comic Sans MS', 14)
legend_font = pygame.font.SysFont('Comic Sans MS', 14)
title_font = pygame.font.SysFont('Comic Sans MS', 14)

screen.fill(pygame.Color("white"))
screen.blit(background_image, [0, 0])

paused = False

#current_time = 1578151801
final_time = 1578236760


guests = {}

user_date = input("Time at which to begin surveillance (in Datetime e.g. 2020-01-04 15:30:01): ")
dt = datetime.datetime.strptime(user_date, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(hours=-5)


current_time = int(datetime.datetime.timestamp(dt))


while not complete:
    #keyboard event handling
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
        #refresh background
        screen.blit(background_image, [0, 0])

        #repaint time
        screen.fill(pygame.Color("white"), (800, 0, 400, 700))
        time = timer_font.render("Time: " + datetime.datetime.utcfromtimestamp(current_time).strftime('%Y-%m-%d %H:%M:%S'), False, (0, 0, 0))
        screen.blit(time, (800,0))

        title = title_font.render("Last Known Locations:", False, (0,0,0))

        #legend creation
        count = 2
        for i in guests.keys():
            count += 1
            guest = legend_font.render(i + ": " + guests[i], True, (255,0,0))
            screen.blit(guest, (800, 40* count))


        #init list of sensors
        used_locations = []

        #Add/Update last known location
        if str(current_time) in data.keys():
            guests.update({data[str(current_time)]["guest-id"]: data[str(current_time)]["device-id"]})

        #Write the last known locations of each guest
        for i in guests.keys():
            guest = name_font.render(i, True, (255,0,0))

            if used_locations.count(guests[i]) > 0:
                y_offset = used_locations.count(guests[i]) * 20
            else:
                y_offset = 0

            used_locations.append(guests[i])

            screen.blit(guest, (device_inventory[guests[i]].x, device_inventory[guests[i]].y + y_offset))

        current_time += 1
        pygame.display.flip()

    clock.tick(clock_tick_rate)

pygame.quit()