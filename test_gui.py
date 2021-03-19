import sys, time, math, glob

import pygame
from gui import *

        
def test_gui():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    
    em = EventManager()
    
    controller = GUIController(em, screen)
    
    frame = Frame()
    frame.x = 10
    frame.y = 10
    frame.width = 400
    frame.height = 300
    controller.add(frame)
    
    label = Label(text="This is a label")
    label.x = 20
    label.y = 210
    controller.add(label)
    
    button = Button(text="Hello World")
    button.x = 200
    button.y = 200
    button.width = 130
    button.height = 40
    def click1():
        print("Ahhh I'm clicked!!")

    button.do_click = click1
    controller.add(button)

    button = Button(text="Bonjour")
    button.x = 200
    button.y = 80
    button.width = 130
    button.height = 40
    controller.add(button)

    button = Button(text="Allo")
    button.x = 200
    button.y = 140
    button.width = 130
    button.height = 40
    controller.add(button)
    
    text_edit = TextEdit(text="test")
    text_edit.x = 200
    text_edit.y = 260
    controller.add(text_edit)
    
    controller.start()
    controller.redraw()
    em.run()
    

if __name__ == "__main__":
    test_gui()
    
