class Viewport(object):
    """ Maps from world coordinates to screen coordinates"""
    def __init__(self,xpos,ypos,viewportheight,viewportwidth):
        ##xpos and ypos are the upper left corner of the viewport in world coordinates.
        self.xpos = xpos
        self.ypos = ypos
        self.vpheight = viewportheight
        self.vpwidth = viewportwidth

    def set_focus(self, x, y):
        self.focus_x = x
        self.focus_y = y
        self.xpos = self.focus_x-self.vpwidth/2
        self.ypos = self.focus_y-self.vpheight/2

    def calc_screen_cords(self, world_x, world_y):
        screen_x = world_x-self.xpos
        screen_y = world_y-self.ypos
        return screen_x,screen_y

    def in_viewport(self,x,y):
        ##tests if a given x position is in the viewport
        if x >= self.xpos and x <= self.xpos+self.vpwidth:
            if y >= self.ypos and y <= self.ypos+self.vpheight:
                return True
        return False
            
        
