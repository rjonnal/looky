from constants import RIGHT,LEFT

class Converter:

    def __init__(self,width,height,pixels_per_degree,eye):
        self.width = width
        self.height = height
        self.pixels_per_degree = pixels_per_degree
        self.x0 = width/2.0
        self.y0 = height/2.0
        self.eye = eye

    def deg2px(self,xdeg,ydeg):
        xpx = xdeg*self.pixels_per_degree*self.eye+self.x0
        ypx = ydeg*self.pixels_per_degree+self.y0
        return xpx,ypx

    def px2deg(self,xpx,ypx):
        xdeg = (xpx-self.x0)/(self.pixels_per_degree*self.eye)
        ydeg = (ypx-self.y0)/(self.pixels_per_degree)
        return xdeg,ydeg
        

class Target:

    def __init__(self,x=0.0,y=0.0):
        self.x = 0.0
        self.y = 0.0
        
