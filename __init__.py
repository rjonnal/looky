import sys, pygame
from constants import *
from components import Location,Target
import time

pygame.init()
pygame.key.set_repeat(100,50)
clock = pygame.time.Clock()

#size = width, height = pygame.display.list_modes()[0]
size = width, height = 512, 512
black = 0, 0, 0
screen = pygame.display.set_mode(size)

loc = Location(width,height,100.0,RIGHT)
tar = Target(screen,loc)

k = 0
t0 = time.time()

key_dict = {}
key_dict[(pygame.K_ESCAPE,pygame.KMOD_NONE)] = sys.exit

key_dict[(pygame.K_LEFT,pygame.KMOD_NONE)] = tar.left
key_dict[(pygame.K_RIGHT,pygame.KMOD_NONE)] = tar.right
key_dict[(pygame.K_UP,pygame.KMOD_NONE)] = tar.up
key_dict[(pygame.K_DOWN,pygame.KMOD_NONE)] = tar.down

key_dict[(pygame.K_LEFT,pygame.KMOD_CTRL)] = tar.c_left
key_dict[(pygame.K_RIGHT,pygame.KMOD_CTRL)] = tar.c_right
key_dict[(pygame.K_UP,pygame.KMOD_CTRL)] = tar.c_up
key_dict[(pygame.K_DOWN,pygame.KMOD_CTRL)] = tar.c_down

key_dict[(pygame.K_LEFT,ALT)] = tar.c_left
key_dict[(pygame.K_RIGHT,ALT)] = tar.c_right
key_dict[(pygame.K_UP,ALT)] = tar.c_up
key_dict[(pygame.K_DOWN,ALT)] = tar.c_down

key_dict[(pygame.K_c,pygame.KMOD_NONE)] = tar.center

while 1:
    clock.tick(30)
    for event in pygame.event.get():
        print event
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            try:
                func = key_dict[(event.key,event.mod)]
                func()
            except Exception as e:
                print 'oops'
                print event.key,event.mod
                #print key_dict
                #sys.exit()
                
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
    if k==100:
        t = time.time() - t0
        t0 = time.time()
        fps = 100.0/t
        k = 0
        print '%0.1f fps'%fps
