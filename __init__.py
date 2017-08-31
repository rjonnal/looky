import sys, pygame
from constants import *
from components import Location,Target
import time

pygame.init()

# print pygame.KMOD_NONE
# mods = pygame.key.get_mods()
# print bin(mods)
# sys.exit()
# if mods & pygame.KMOD_NUM:
#     sys.exit('Please turn off the NUM LOCK and try again.')
# if mods & pygame.KMOD_CAPS:
#     sys.exit('Please turn off the CAPS LOCK and try again.')
                



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


key_triples = [
    (pygame.K_ESCAPE,None,sys.exit),
    (pygame.K_LEFT,~pygame.KMOD_CTRL,tar.left),
    (pygame.K_LEFT,pygame.KMOD_CTRL,tar.c_left)]

key_dict = {}

for key,mod,action in key_triples:
    if key in key_dict.keys():
        key_dict[key].append((mod,action))
    else:
        key_dict[key] = [(mod,action)]


while 1:
    clock.tick(30)
    for event in pygame.event.get():
        print event
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            mods = pygame.key.get_mods()
            print 'mods',mods
            try:
                modpairs = key_dict[event.key]
                for mod,action in modpairs:
                    print mod,mods,mods & mod
                sys.exit()
                func,mod = key_dict[event.key]
                if (mods and mod & mods) or (not mods):
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
        pygame.draw.line(screen,WHITE,pt1,pt2,1)
    
    pygame.display.flip()
    
    k = k + 1
    if k==100:
        t = time.time() - t0
        t0 = time.time()
        fps = 100.0/t
        k = 0
        print '%0.1f fps'%fps
