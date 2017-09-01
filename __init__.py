import sys, pygame
from constants import *
from components import Location,Target,Modstate
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
                
myfont = pygame.font.SysFont('Times New Roman', 30)
pygame.key.set_repeat(100,50)
clock = pygame.time.Clock()

size = width, height = pygame.display.list_modes()[0]
#size = width, height = 512, 512
black = 0, 0, 0
screen = pygame.display.set_mode(size)

loc = Location(width,height,100.0,RIGHT)
tar = Target(screen,loc)

k = 0
t0 = time.time()

key_triples = [
    (pygame.K_ESCAPE,Modstate('any'),sys.exit),
    (pygame.K_LEFT,Modstate(''),tar.left),
    (pygame.K_RIGHT,Modstate(''),tar.right),
    (pygame.K_UP,Modstate(''),tar.up),
    (pygame.K_DOWN,Modstate(''),tar.down),
    (pygame.K_LEFT,Modstate('ctrl'),tar.c_left),
    (pygame.K_RIGHT,Modstate('ctrl'),tar.c_right),
    (pygame.K_UP,Modstate('ctrl'),tar.c_up),
    (pygame.K_DOWN,Modstate('ctrl'),tar.c_down),
    (pygame.K_LEFT,Modstate('alt'),tar.a_left),
    (pygame.K_RIGHT,Modstate('alt'),tar.a_right),
    (pygame.K_UP,Modstate('alt'),tar.a_up),
    (pygame.K_DOWN,Modstate('alt'),tar.a_down),
    ]

# convert to a dictionary for efficient lookup:
key_dict = {}
for key,key_ms,func in key_triples:
    if key in key_dict.keys():
        key_dict[key].append((key_ms,func))
    else:
        key_dict[key] = [(key_ms,func)]
        
current_ms = Modstate()

while 1:
    #clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            current_ms.update()
            try:
                tups = key_dict[event.key]
                for key_ms,func in tups:
                    #print key_ms,current_ms,key_ms==current_ms,func
                    if key_ms==current_ms:
                        print tar
                        func()
                        break
            except Exception as e:
                print e
                
        elif event.type == pygame.MOUSEBUTTONUP:
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

    msg_list = tar.__str__().split('\n')
    for idx,msg in enumerate(msg_list):
        textsurface = myfont.render(msg, False, (255, 255, 255))
        screen.blit(textsurface,(0,0+idx*30))
        
    pygame.display.flip()
    
    k = k + 1
    if k==100:
        t = time.time() - t0
        t0 = time.time()
        fps = 100.0/t
        k = 0
        print '%0.1f fps'%fps
