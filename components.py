from constants import *
import math
import sys

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
        

class Target:

    def __init__(self,screen,location,x=0.0,y=0.0):
        self.x = 0.0
        self.y = 0.0
        self.loc = location
        self.screen = screen
        self.rad = 1.0
        self.step = 1.0
        self.c_step = 2.0

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
    def center(self):
        self.y = 0.0
        self.x = 0.0
