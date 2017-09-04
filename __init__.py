import sys, pygame
from constants import *
from components import Target,Modstate
import time
import looky_config as lcfg

line_color = lcfg.LINE_COLOR
background_color = lcfg.BACKGROUND_COLOR
font = lcfg.FONT
font_size = lcfg.FONT_SIZE

pygame.init()
myfont = pygame.font.SysFont(font, font_size)
pygame.key.set_repeat(100,50)
clock = pygame.time.Clock()

size = width, height = pygame.display.list_modes()[0]
screen = pygame.display.set_mode(size)
hwidth = width//2
hheight = height//2

pygame.display.toggle_fullscreen()

tar = Target()
fps = lcfg.MAX_FPS

help_on = False

def exit():
    """Exit via sys.exit()."""
    sys.exit()

def fullscreen():
    """Toggle fullscreen mode."""
    pygame.display.toggle_fullscreen()

def toggle_help():
    """Toggle help hints."""
    global help_on
    help_on = not help_on
    
key_triples = [
    (pygame.K_ESCAPE,Modstate('any'),exit),
    (pygame.K_q,Modstate('any'),exit),
    (pygame.K_F5,Modstate(''),fullscreen),
    (pygame.K_LEFT,Modstate(''),tar.left),
    (pygame.K_RIGHT,Modstate(''),tar.right),
    (pygame.K_UP,Modstate(''),tar.up),
    (pygame.K_DOWN,Modstate(''),tar.down),
    (pygame.K_LEFT,Modstate('ctrl'),tar.small_left),
    (pygame.K_RIGHT,Modstate('ctrl'),tar.small_right),
    (pygame.K_UP,Modstate('ctrl'),tar.small_up),
    (pygame.K_DOWN,Modstate('ctrl'),tar.small_down),
    (pygame.K_LEFT,Modstate('alt'),tar.offset_left),
    (pygame.K_RIGHT,Modstate('alt'),tar.offset_right),
    (pygame.K_UP,Modstate('alt'),tar.offset_up),
    (pygame.K_DOWN,Modstate('alt'),tar.offset_down),
    (pygame.K_EQUALS,Modstate(''),tar.increment_line_width),
    (pygame.K_MINUS,Modstate(''),tar.decrement_line_width),
    (pygame.K_EQUALS,Modstate('ctrl'),tar.increase_radius),
    (pygame.K_MINUS,Modstate('ctrl'),tar.decrease_radius),
    (pygame.K_SPACE,Modstate(''),tar.switch_eye),
    (pygame.K_SLASH,Modstate(''),toggle_help)
    ]

# Use the keys and function docstrings to make a help menu.
help_strings = []
for kt in key_triples:
    modifier = kt[1].__str__()
    if modifier in ['any','none']:
        modifier = ''
    else:
        modifier = modifier+'-'
    doc = kt[2].__doc__
    lead = '%s%s:'%(modifier,pygame.key.name(kt[0]))
    while len(lead)<12:
        lead = lead+' '
    help_strings.append('%s %s'%(lead,doc))

# convert to a dictionary for efficient lookup:
key_dict = {}
for key,key_ms,func in key_triples:
    if key in key_dict.keys():
        key_dict[key].append((key_ms,func))
    else:
        key_dict[key] = [(key_ms,func)]
        
current_ms = Modstate()

t0 = time.time()
printed = False

while 1:
    clock.tick(lcfg.MAX_FPS)
    fps = clock.get_fps()
    t = time.time()
    age = t-t0
    state_changed = False
    
    if not printed and age>5.0:
        print age
        print tar
        print
        printed = True
        
    for event in pygame.event.get():
        t0 = time.time()
        printed = False
        state_changed = True
        current_ms.update()
        alt_on = current_ms.alt
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            try:
                tups = key_dict[event.key]
                for key_ms,func in tups:
                    if key_ms==current_ms:
                        func()
                        break
            except Exception as e:
                pass
        elif event.type == pygame.MOUSEBUTTONUP:
            mousex,mousey = event.pos
            x_deg,y_deg = loc.px2deg(mousex,mousey)
            tar.x = x_deg
            tar.y = y_deg

    if not state_changed:
        continue

    screen.fill(background_color)

    # draw here

    lines = tar.get_lines()
    for pt1,pt2 in lines:
        dpt1 = (pt1[0]+hwidth,pt1[1]+hheight)
        dpt2 = (pt2[0]+hwidth,pt2[1]+hheight)
        pygame.draw.line(screen,line_color,dpt1,dpt2,tar.line_width_px)

    if alt_on:
        offset_lines = tar.get_offset_lines()
        for pt1,pt2 in offset_lines:
            dpt1 = (pt1[0]+hwidth,pt1[1]+hheight)
            dpt2 = (pt2[0]+hwidth,pt2[1]+hheight)
            pygame.draw.line(screen,RED,dpt1,dpt2,tar.line_width_px)
            
    msg_list = [tar.msg_ret_location(),tar.msg_abs_location()]
    msg_colors = [lcfg.WHITE,lcfg.GRAY]
    msg_list.append('%0.1f fps'%fps)
    msg_colors.append(lcfg.GRAY)
    if alt_on:
        msg_list.append(tar.msg_offset_location())
        msg_colors.append(lcfg.OFFSET_COLOR)
    if help_on:
        msg_list = msg_list + help_strings
        msg_colors = msg_colors + [lcfg.HELP_COLOR]*len(help_strings)
    for idx,(msg,color) in enumerate(zip(msg_list,msg_colors)):
        textsurface = myfont.render(msg, False, color)
        screen.blit(textsurface,(0,0+idx*font_size))
        
    pygame.display.flip()
    
