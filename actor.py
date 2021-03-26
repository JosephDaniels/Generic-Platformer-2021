import glob

import pygame

class Actor(object):
    def __init__(self, x, y):
        
        self.animations = {}
        self.frames = []
        self.state = ""
        self.currframe = 0
        
        self.x = x
        self.y = y


    def _get_curr_img(self):
        print("Frame", self.currframe, "of", len(self.frames))
        return self.frames[self.currframe]

    img = property(_get_curr_img)

    def next_frame(self):

        self.currframe+=1
        if self.currframe >= len(self.frames):
            self.currframe = 0
            
    @staticmethod
    def alphamasked(img, green_screen_color):
        """returns an image alpha masked so that pixels with the given
           RGB green_screen_color are made transparent"""
        new_image = img.convert_alpha()
        mask_r, mask_g, mask_b = green_screen_color
        width, height = img.get_size()
        for x in range(width):
            for y in range(height):
                r,g,b,a = new_image.get_at((x,y))
                if  r == mask_r and g == mask_g and b == mask_b:
                    new_image.set_at((x,y), (r,g,b,0))
        return new_image

    def load_animation(self, state_name, filepattern, scaling = 1, reverse = False):
        frames = []
        filenamelist = glob.glob(filepattern)
        filenamelist.sort()
        for filename in filenamelist:
            img = pygame.image.load(filename)
            w,h = img.get_size()
            w = int(w*scaling)
            h = int(h*scaling)
            img = pygame.transform.scale( img, (w,h))
            #green_screen_color = x.get_at((0,0))
            #x = self.alphamasked(x, green_screen_color)
            if reverse == True:
                frames.append(pygame.transform.flip(img, 1, 0) )
            else:
                frames.append(img)
        print(len(frames), "frames loaded for animation", state_name)
        self.animations[state_name] = frames

    
    def set_state(self, state_name):
        self.state = state_name
        self.frames = self.animations[self.state]
        self.currframe = 0

    def draw_to(self, surface):
        surface.blit(self.frames[self.currframe], (self.x, self.y))

    def get_rect(self):
        return pygame.Rect((self.x, self.y), self.img.get_size())

    def on_tick(self, evt):
        self.next_frame()

    def dump(self):
        print("State", self.state)
