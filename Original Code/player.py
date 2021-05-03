import glob
import pygame
from gui import Event

class Player(object):
    def __init__(self, x, y):
        self.dx = 0
        self.dy = 0
        self.x = x
        self.y = y
        self.pastx = []
        self.pasty = []
        self.animations = {}
        self.frames = []
        self.state = ""
        self.rot = 0
        self.obstructedflag = False
        self.pushed_left = 0
        self.pushed_right = 0
        self.pushed_up = 0
        self.pushed_down = 0
        

    def level_up(self):
        if self.exp >= self.exprequirement:
            lastlevelbonus = self.bonus
            self.level +=1
            bonus = 1000*(self.level+lastlevelbonus)

    def load_anim(self, state_name, filepattern, reverse = False):
        frames = []
        filenamelist = glob.glob(filepattern)
        filenamelist.sort()
        for filename in filenamelist:
            x = pygame.image.load(filename)
            green_screen_color = x.get_at((0,0))
##            x = alphamasked(x, green_screen_color)
            if reverse == True:
                frames.append( pygame.transform.flip(x,1,0) )
            else:
                frames.append( x )
        print (len(frames))
        self.animations[state_name] = frames
        return frames

    def on_push_up(self, evt):
        self.pushed_up = 1
##        self.set_state ("Walk_Up")

    def on_push_down(self, evt):
        self.pushed_down = 1
##        self.set_state("Walk_Down")

    def on_push_left(self, evt):
        self.pushed_left = 1
##        self.set_state("Walk_Left")

    def on_push_right(self, evt):
        self.pushed_right = 1
##        self.set_state("Walk_Right")

    def on_stop_push_left(self, evt):
        self.pushed_left = 0

    def on_stop_push_right(self, evt):
        self.pushed_right = 0

    def on_stop_push_up(self, evt):
        self.pushed_up = 0

    def on_stop_push_down(self, evt):
        self.pushed_down = 0

    def on_fire_at(self, evt):
        pass

    def on_tick(self, evt):
        self.next_frame()
        self.dx = (self.pushed_right - self.pushed_left)* self.speed
        self.dy = (self.pushed_down - self.pushed_up)* self.speed

    def get_rect(self,x = None,y = None):
        if x == None:
            x = self.x
        if y == None:
            y = self.y
        return pygame.Rect(x,y, self.img.get_width(), self.img.get_height())

    def on_obstructed(self, evt):
        self.obstructedflag = True
    

