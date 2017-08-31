import sys, pygame
from constants import *
from components import Location,Target

pygame.init()

size = width, height = pygame.display.list_modes()[0]
speed = [50, 50]
black = 0, 0, 0
screen = pygame.display.set_mode(size)
loc = Location(width,height,100.0,RIGHT)
tar = Target(screen,loc)

k = 0


while 1:
    for event in pygame.event.get():
        print event
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            print event
            mousex,mousey = event.pos
            x_deg,y_deg = loc.px2deg(mousex,mousey)
            tar.x = x_deg
            tar.y = y_deg
        elif event.type == pygame.K_RETURN : sys.exit()

    screen.fill(black)

    # draw here

    lines = tar.get_lines()

    for pt1,pt2 in lines:
        pygame.draw.line(screen,WHITE,pt1,pt2,5)
    
    pygame.display.flip()
    k = k + 1
