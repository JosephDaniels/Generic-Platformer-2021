import pygame

class Controller(object):

    def __init__(self, ev_manager, screen):
        self.ev_manager = ev_manager
        self.ev_manager.register(self)
        self.screen = screen
        self.mousex = None
        self.mousey = None
        self.zoom_val = 0.125
        self.viewport = None
        #Listener Groups
        self.actors = []

    def add_actor(self, actor):
        self.actors.append(actor)
        actor.ev_manager = self.ev_manager
        self.ev_manager.register(actor)

    def on_tick(self, evt):
        self.screen.fill((0,0,0))
        for actor in self.actors:
            actor.draw_to(self.screen)
##            actor.tick()
        pygame.display.flip()

    def on_MouseMotion(self,evt):
        x,y = self.mousex, self.mousey

    def on_MouseButtonDown(self, evt):
        if evt.button == 1:
            self.grab_screen()
        if evt.button == 4:
            self.zoom(+1)
        if evt.button == 5:
            self.zoom(-1)

    def on_KeyDown(self,evt):
        if evt.key == pygame.K_KP_PLUS:
            self.zoom(+1)
        if evt.key == pygame.K_KP_MINUS:
            self.zoom(-1)

        if evt.key == pygame.K_ESCAPE:
            self.ev_manager.post_event("Quit")
        if evt.key == pygame.K_UP:
            self.ev_manager.post_event("Jump")
        if evt.key == pygame.K_DOWN:
            self.ev_manager.post_event("Duck")
        if evt.key == pygame.K_LEFT:
            self.ev_manager.post_event("Move_Left")
        if evt.key == pygame.K_RIGHT:
            self.ev_manager.post_event("Move_Right")

    def on_KeyUp(self,evt):
        if evt.key == pygame.K_UP:
            self.ev_manager.post_event("Stop_Jump")
        if evt.key == pygame.K_DOWN:
            self.ev_manager.post_event("Stop_Duck")
        if evt.key == pygame.K_LEFT:
            self.ev_manager.post_event("Stop_Move_Left")
        if evt.key == pygame.K_RIGHT:
            self.ev_manager.post_event("Stop_Move_Right")

    def on_Quit(self, evt):
        pygame.quit()
        exit()

    def grab_screen(self,):
        pass
##        if actor.get_rect().collidepoint(evt.pos[0],evt.pos[1]):
            
    def zoom(self,direction):
        self.zoom_val = self.zoom_val+(0.025*direction)
        for actor in self.actors:
            self.ev_manager.post_event("zoom", zoom_size = self.zoom_val)
