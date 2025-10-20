# Example file showing a circle moving on screen
import pygame
import config as cfg
import sys,os,glob,math,random,logging,time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler

try:
    from location_script import location_script
except ImportError:
    location_script = [(0.0,0.0)]
    
pygame.init()
pygame.font.init() 

named_tuple = time.localtime()
date_string = time.strftime("%Y%m%d", named_tuple)
log_filename = date_string+'.log'
log_path = os.path.join(cfg.log_folder,log_filename)
os.makedirs(cfg.log_folder,exist_ok=True)
os.makedirs(cfg.data_folder,exist_ok=True)

logger = logging.getLogger(__name__)
logging.basicConfig(filename=log_path, encoding='utf-8', level=logging.INFO)


with open(os.path.join(cfg.data_folder,'fonts_available.log'),'w') as fid:
    font_list = sorted(pygame.font.get_fonts())
    for item in font_list:
        fid.write('%s\n'%item)

def log(message):
    named_tuple = time.localtime()
    formatted_time = time.strftime("%Y.%m.%d.%H.%M.%S", named_tuple)
    logger.info('%s: %s'%(formatted_time,message))

my_font = pygame.font.SysFont(cfg.text_font, cfg.text_font_size)

# pygame setup
screen = pygame.display.set_mode(cfg.display_mode,display=cfg.monitor_number)
clock = pygame.time.Clock()
running = True
dt = 0

bgc = cfg.background_color

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


class ObserverHandler(FileSystemEventHandler):
    def __init__(self,target):
        super().__init__()
        self.target = target
    def on_created(self,event):
        filename = event.src_path
        ext = os.path.splitext(filename)[-1]
        if ext.lower() in cfg.data_monitoring_extensions:
            outfn = filename.replace(ext,'')+'.looky'
            outstr = str(self.target)
            with open(outfn,'w') as fid:
                fid.write(outstr)
            try:
                assert os.path.exists(outfn)
            except AssertionError:
                sys.exit('ObserverHandler failed to write .looky file.')
            log('%s file found at %s, eccentricity written to %s'%(ext,filename,outfn))

                
class Target:

    def __str__(self):
        return '%0.2f,%0.2f'%(self.position_vector.x/cfg.pixels_per_deg,
                              self.position_vector.y/cfg.pixels_per_deg)
    
    def __init__(self,step=None,small_step=None):
        self.location_index = 0
        x,y = [k*cfg.pixels_per_deg for k in location_script[self.location_index]]
        
        self.position_vector = pygame.Vector2(x,y)
        if step is None:
            self.step = cfg.target_step*cfg.pixels_per_deg
        else:
            self.step = step
            
        if small_step is None:
            self.small_step = cfg.target_small_step*cfg.pixels_per_deg
        else:
            self.small_step = small_step

        self.age = 0.0
        self.logged = False

    def next(self):
        self.location_index = (self.location_index+1)%len(location_script)
        x,y = [k*cfg.pixels_per_deg for k in location_script[self.location_index]]
        self.move(x,y,absolute=True)
        
    def previous(self):
        self.location_index = (self.location_index-1)%len(location_script)
        x,y = [k*cfg.pixels_per_deg for k in location_script[self.location_index]]
        self.move(x,y,absolute=True)
        
        
    def move(self,dx,dy,absolute=False):
        if absolute:
            self.position_vector.x = dx
            self.position_vector.y = dy
        else:
            self.position_vector.x+=dx
            self.position_vector.y+=dy
        self.logged = False
        self.age = 0.0

    def left(self,fine=False):
        if fine:
            self.move(-self.small_step,0)
        else:
            self.move(-self.step,0)

    def right(self,fine=False):
        if fine:
            self.move(self.small_step,0)
        else:
            self.move(self.step,0)
            
    def up(self,fine=False):
        if fine:
            self.move(0,-self.small_step)
        else:
            self.move(0,-self.step)
            
    def down(self,fine=False):
        if fine:
            self.move(0,self.small_step)
        else:
            self.move(0,self.step)


class Origin(Target):
    
    def __init__(self):
        super().__init__(step=cfg.origin_step_px,small_step=cfg.origin_small_step_px)
        try:
            with open(os.path.join(cfg.data_folder,cfg.origin_filename),'r') as fid:
                origin_x,origin_y = [float(k) for k in fid.read().split(',')]
        except FileNotFoundError:
            origin_x,origin_y = [k/2.0 for k in cfg.display_mode]

        self.position_vector = pygame.Vector2(origin_x,origin_y)
            
        self.size = cfg.origin_size_px
        self.color = cfg.origin_color
        self.linewidth = cfg.origin_line_width

    def move(self,dx,dy):
        super().move(dx,dy)
        with open(os.path.join(cfg.data_folder,cfg.origin_filename),'w') as fid:
            x = self.position_vector.x
            y = self.position_vector.y
            fid.write('%0.1f,%01.f'%(x,y))
        
    def draw(self,screen):
        pygame.draw.line(screen,self.color,pygame.Vector2(self.position_vector.x-self.size,self.position_vector.y),pygame.Vector2(self.position_vector.x+self.size,self.position_vector.y),self.linewidth)
        pygame.draw.line(screen,self.color,pygame.Vector2(self.position_vector.x,self.position_vector.y-self.size),pygame.Vector2(self.position_vector.x,self.position_vector.y+self.size),self.linewidth)
                         
class Star(Target):

    def __init__(self):
        super().__init__()
        self.radius = cfg.target_radius*cfg.pixels_per_deg
        self.thetas = [k*math.pi/4.0 for k in range(8)]
        self.linewidth = cfg.target_line_width
        self.color = cfg.target_color

    def draw(self, screen, origin=None):
        if origin is None:
            xoff = 0.0
            yoff = 0.0
        else:
            xoff = origin.position_vector.x
            yoff = origin.position_vector.y

        x0 = self.position_vector.x+xoff
        y0 = self.position_vector.y+yoff
        
        for theta in self.thetas:
            x1 = math.sin(theta)*self.radius+x0
            y1 = math.cos(theta)*self.radius+y0
            
            pygame.draw.line(screen, self.color, pygame.Vector2(x0,y0), pygame.Vector2(x1,y1), self.linewidth)

class Bullseye(Target):

    def __init__(self):
        super().__init__()
        self.radius = cfg.target_radius*cfg.pixels_per_deg
        self.linewidth = cfg.target_line_width
        self.color = cfg.target_color
        self.radii = [k*self.radius/8.0 for k in range(8,0,-1)]
        self.radii.append(0.25*self.radius/8.0)
        self.ring_colors = []
        for idx in range(len(self.radii)):
            self.ring_colors.append(cfg.colors[idx%2])
            
    def draw(self, screen, origin=None):
        if origin is None:
            xoff = 0.0
            yoff = 0.0
        else:
            xoff = origin.position_vector.x
            yoff = origin.position_vector.y

        x0 = self.position_vector.x+xoff
        y0 = self.position_vector.y+yoff

        for radius,color in zip(self.radii,self.ring_colors):
            pygame.draw.circle(screen, color, pygame.Vector2(x0,y0), radius)

class Inset:

    def __init__(self, width, height, x, y, update_frequency=5.0):
        self.width = int(round(width))
        self.height = int(round(height))
        self.x = x-width/2.0
        self.y = y-height/2.0
        self.update_frequency = update_frequency
        
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(cfg.inset_background_color)
        self.clock = pygame.time.Clock()
        self.last_update_time = 0.0

    def draw(self, screen, origin = None):
        if origin is None:
            xoff = 0.0
            yoff = 0.0
        else:
            xoff = origin.position_vector.x
            yoff = origin.position_vector.y
            
        dt = self.clock.tick()*1e-3
        self.last_update_time = self.last_update_time + dt
        if self.last_update_time>=1/self.update_frequency:
            self.update()
            self.last_update_time = 0.0
        screen.blit(self.surface, (self.x+xoff, self.y+yoff))
        
    def update(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        self.surface.fill((r,g,b))


class DeadLeaves(Inset):

    def __init__(self):
        xoff = origin.position_vector.x
        yoff = origin.position_vector.y
        
        super().__init__(cfg.inset_width_deg*cfg.pixels_per_deg,
                         cfg.inset_height_deg*cfg.pixels_per_deg,
                         cfg.inset_x_deg*cfg.pixels_per_deg,
                         cfg.inset_y_deg*cfg.pixels_per_deg,
                         cfg.deadleaves_frequency)
        self.s1 = pygame.Surface((self.width,self.height))
        self.s2 = pygame.Surface((self.width,self.height))
        g = cfg.deadleaves_gray_mean
        self.s1.fill((g,g,g))
        self.s2.fill((g,g,g))
        n_ellipses = cfg.deadleaves_n_ellipses
        mu = cfg.deadleaves_rad_mean_deg*2*cfg.pixels_per_deg
        sigma = cfg.deadleaves_rad_std_deg*2*cfg.pixels_per_deg
        self.counter = 0
        self.surfaces = [self.s1,self.s2]
        random.seed(cfg.deadleaves_seed)
        for k in range(n_ellipses):
            width = random.gauss(mu,sigma)
            height = random.gauss(mu,sigma)

            left = random.randint(0,int(self.width))-width//2
            top = random.randint(0,int(self.height))-height//2
            rect = pygame.Rect(left,top,width,height)
            
            gray_shift = random.randint(0,cfg.deadleaves_gray_range)-cfg.deadleaves_gray_range//2#+cfg.deadleaves_gray_mean
            gray1 = cfg.deadleaves_gray_mean+gray_shift
            gray2 = cfg.deadleaves_gray_mean-gray_shift
            
            gray1 = max(0,gray1)
            gray1 = min(gray1,255)
            gray2 = max(0,gray2)
            gray2 = min(gray2,255)
            
            alpha = cfg.deadleaves_alpha
            pygame.draw.ellipse(self.s1,(gray1,gray1,gray1,alpha),rect)
            pygame.draw.ellipse(self.s2,(gray2,gray2,gray2,alpha),rect)
        pygame.image.save(self.s1,os.path.join(cfg.data_folder,'deadleaves_1.png'))
        pygame.image.save(self.s2,os.path.join(cfg.data_folder,'deadleaves_2.png'))

    def update(self):
        self.surface = self.surfaces[self.counter]
        self.counter = (self.counter+1)%2
        
if cfg.target_type=='bullseye':
    tar = Bullseye()
elif cfg.target_type=='star':
    tar = Star()
else:
    sys.exit('%s is an invalid target_type in config.py')
    
origin = Origin()
    
step = cfg.target_step*cfg.pixels_per_deg
small_step = cfg.target_small_step*cfg.pixels_per_deg

inset = DeadLeaves()
inset_exists = False

try:
    path = cfg.data_monitoring_folder
    event_handler = ObserverHandler(tar)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
except AttributeError as ae:
    print('data_monitoring_folder not set in config.py. Proceeding without data monitoring.')
    pass
except FileNotFoundError as fnfe:
    print('data_monitoring_folder %s not found. Please edit config.py as required.'%cfg.data_monitoring_folder)
    sys.exit()


def close_match(tup,tup_list,tolerance=0.01):
    out = False
    x0,y0 = tup
    for idx,(x,y) in enumerate(tup_list):
        d = math.sqrt((y0-y)**2+(x0-x)**2)
        if d<tolerance:
            out = idx
            break
    return out



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        mods = pygame.key.get_mods()
        
        origin_mode = mods & pygame.KMOD_ALT
        fine_mode = mods & pygame.KMOD_SHIFT
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if origin_mode:
                    origin.left(fine_mode)
                else:
                    tar.left(fine_mode)
                    
            if event.key == pygame.K_RIGHT:
                if origin_mode:
                    origin.right(fine_mode)
                else:
                    tar.right(fine_mode)
                    
            if event.key == pygame.K_UP:
                if origin_mode:
                    origin.up(fine_mode)
                else:
                    tar.up(fine_mode)
                    
            if event.key == pygame.K_DOWN:
                if origin_mode:
                    origin.down(fine_mode)
                else:
                    tar.down(fine_mode)


            if event.key == pygame.K_PAGEUP:
                if origin_mode:
                    pass
                else:
                    tar.previous()

            if event.key == pygame.K_PAGEDOWN:
                if origin_mode:
                    pass
                else:
                    tar.next()

            if event.key == pygame.K_i:
                inset_exists = not inset_exists
                    
                
            if event.key in [pygame.K_ESCAPE,pygame.K_q]:
                running = False

            
    # fill the screen with a color to wipe away anything from last frame
    screen.fill(bgc)

    if inset_exists:
        inset.draw(screen,origin)
        
    if origin_mode:
        origin.draw(screen)
    else:
        tar.draw(screen,origin)

    # keys = pygame.key.get_pressed()

    # if keys[pygame.K_w]:
    #     tar.move(0,step)
    # if keys[pygame.K_s]:
    #     tar.move(0,-step)
    # if keys[pygame.K_a]:
    #     tar.move(-step,0)
    # if keys[pygame.K_d]:
    #     tar.move(step,0)

    # if keys[pygame.K_ESCAPE] or keys[pygame.K_q]:
    #     running = False

        

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick() / 1000

    tar.age = tar.age + dt

    x_deg = tar.position_vector.x/cfg.pixels_per_deg
    y_deg = tar.position_vector.y/cfg.pixels_per_deg
    try:
        lidx = close_match((x_deg,y_deg),location_script)
    except Exception as e:
        print(e)
        lidx = -1
    message = 'x = %0.3f, y = %0.3f (loc %d)'%(x_deg,y_deg,lidx)
    if origin_mode:
        ox_px = origin.position_vector.x
        oy_px = origin.position_vector.y
        message = message + ' origin x = %d, y = %d'%(ox_px,oy_px)
    
    
    text_surface = my_font.render(message, False, cfg.text_color)
    screen.blit(text_surface,(0,0))
    
    if tar.age > cfg.logging_interval and not tar.logged:
        log(message)
        tar.logged = True
    
    # flip() the display to put your work on screen
    pygame.display.flip()


pygame.quit()
