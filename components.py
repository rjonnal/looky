from constants import *
import math
import sys
import pygame

class Location:

    def __init__(self,width,height,pixels_per_degree,eye):
        self.width = width
        self.height = height
        self.pixels_per_degree = pixels_per_degree
        self.x0 = width/2.0
        self.y0 = height/2.0
        self.eye = eye
        self.offset_step_px = 10

    def deg2px(self,xdeg,ydeg):
        xpx = xdeg*self.pixels_per_degree+self.x0
        ypx = ydeg*self.pixels_per_degree+self.y0
        return xpx,ypx

    def px2deg(self,xpx,ypx):
        xdeg = (xpx-self.x0)/(self.pixels_per_degree)
        ydeg = (ypx-self.y0)/(self.pixels_per_degree)
        return xdeg,ydeg

    def offset_left(self):
        self.x0 = self.x0 - self.offset_step_px
    def offset_right(self):
        self.x0 = self.x0 + self.offset_step_px
    def offset_up(self):
        self.y0 = self.y0 - self.offset_step_px
    def offset_down(self):
        self.y0 = self.y0 + self.offset_step_px

class Target:

    def __init__(self,screen,location,x=0.0,y=0.0):
        self.x = 0.0
        self.y = 0.0
        self.loc = location
        self.screen = screen
        self.rad = 1.0
        self.step = 1.0
        self.c_step = 2.0

    def __str__(self):
        if self.loc.eye==RIGHT:
            eye = 'right'
        else:
            eye = 'left'
            
        outlist = ['location (%0.1f,%0.1f)'%(self.x,self.y),
                'offset (%0.1f,%0.1f)'%(self.loc.x0,self.loc.y0),
                'eye %s'%eye]
        return '\n'.join(outlist)
        
    def get_lines(self):
        lines = []
        for theta in range(0,180,45):
            line = []
            theta_rad = float(theta)/180.0*math.pi
            x1 = self.rad*math.sin(theta_rad)+self.x
            y1 = self.rad*math.cos(theta_rad)+self.y
            x2 = self.rad*math.sin(theta_rad+math.pi)+self.x
            y2 = self.rad*math.cos(theta_rad+math.pi)+self.y
            x1px,y1px = self.loc.deg2px(x1,y1)
            x2px,y2px = self.loc.deg2px(x2,y2)
            lines.append([(x1px,y1px),(x2px,y2px)])
        return lines

    def left(self):
        self.x = self.x - self.step
    def right(self):
        self.x = self.x + self.step
    def up(self):
        self.y = self.y - self.step
    def down(self):
        self.y = self.y + self.step
    def c_left(self):
        self.x = self.x - self.c_step
    def c_right(self):
        self.x = self.x + self.c_step
    def c_up(self):
        self.y = self.y - self.c_step
    def c_down(self):
        self.y = self.y + self.c_step

    def a_left(self):
        self.loc.offset_left()
    def a_right(self):
        self.loc.offset_right()
    def a_up(self):
        self.loc.offset_up()
    def a_down(self):
        self.loc.offset_down()
        
    def center(self):
        self.y = 0.0
        self.x = 0.0


class Modstate:

    def __init__(self,state_string=''):
        self.ctrl = state_string.lower().find('ctrl')>-1
        self.shift = state_string.lower().find('shift')>-1
        self.alt = state_string.lower().find('alt')>-1
        self.any = state_string.lower().find('any')>-1
        
    def __str__(self):
        out = []
        if self.shift: out.append('shift')
        if self.alt: out.append('alt')
        if self.ctrl: out.append('ctrl')
        if self.any: out.append('any')
        if len(out):
            out = '_'.join(out)
        else:
            out = 'none'
        return out

    def __eq__(self,ms):
        return (self.ctrl==ms.ctrl and self.alt==ms.alt and self.shift==ms.shift) or self.any

    def update(self):
        mods = pygame.key.get_mods()
        self.ctrl = not (mods & pygame.KMOD_CTRL)==0
        self.alt = not (mods & pygame.KMOD_ALT)==0
        self.shift = not (mods & pygame.KMOD_SHIFT)==0
    

