import pygame
import time, math
import gui
import actor
import controller

##import glob

from constants import *

class Player(actor.Actor):
    def __init__(self, *args):
        super().__init__(*args)
        self.vx = 0
        self.vy = 0
        
    ## Create Event Handlers
    def on_Jump(self, evt):
        self.vy = -5
    def on_Duck(self, evt):
        self.vy = +5
    def on_Move_Left(self, evt):
        self.vx = -5
    def on_Move_Right(self, evt):
        self.vx = +5

    def on_Stop_Jump(self, evt):
        self.vy = 0
    def on_Stop_Duck(self, evt):
        self.vy = 0
    def on_Stop_Move_Left(self, evt):
        self.vx = 0
    def on_Stop_Move_Right(self, evt):
        self.vx = 0
        
    def on_tick(self, evt):
        self.x+=self.vx
        self.y+=self.vy
        

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    
    player = Player(0,0, pygame.image.load(PLAYER_IMAGE))
    em = gui.EventManager()
    ctrl = controller.Controller(em, screen)
    ctrl.add_actor(player)
    em.run()
        
if __name__ == "__main__":
    main()

##Make a viewport for controlling the screen and world chords together
    
##    viewport = Viewport(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)
##    controller.viewport = viewport
