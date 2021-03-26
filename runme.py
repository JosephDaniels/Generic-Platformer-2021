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
        self.left_vx = 0
        self.right_vx = 0
        self.vy = 0
        self.grounded = False
        
    ## Create Event Handlers
    def on_Jump(self, evt):
        if self.grounded:
            self.vy -= JUMP_STRENGTH
            
    def on_Duck(self, evt):
        pass
    
    def on_Move_Left(self, evt):
        self.set_state("walk_left")
        self.left_vx = -5
        
    def on_Move_Right(self, evt):
        self.set_state("walk_right")
        self.right_vx = +5
        
    def on_Stop_Duck(self, evt):
        pass
    
    def on_Stop_Move_Left(self, evt):
        self.left_vx = 0
        
    def on_Stop_Move_Right(self, evt):
        self.right_vx = 0



class Block(actor.Actor):
    def __init__(self, *args):
        super().__init__(*args)

        

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    
    # set up the main controller
    em = gui.EventManager()
    ctrl = controller.Controller(em, screen)
    
    # create the "megaman"
    player = Player(0,300)
    player.load_animation("walk_right","Images\\Sprites\\run*.png", scaling = 0.1)
    player.load_animation("walk_left","Images\\Sprites\\run*.png", scaling = 0.1, reverse=True )
    player.set_state("walk_right")
    
    ctrl.add_actor(player)
    
    #create the blocks
    for x in range(6):
        block = Block(x*64,416)
        block.load_animation("static", "Images\\Basic_Block.png");
        block.set_state("static")
        ctrl.add_block(block)
    for x in range(6):
        block = Block(x*64+192, 480)
        block.load_animation("static", "Images\\Basic_Block.png");
        block.set_state("static")
        ctrl.add_block(block)

    # kickstart the game
    em.run()

        
if __name__ == "__main__":
    main()

##Make a viewport for controlling the screen and world chords together
    
##    viewport = Viewport(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)
##    controller.viewport = viewport
