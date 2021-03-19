from mapsettings import *
from constants import *

import pprint
import pygame

class Layer(object):
    def __init__(self, map_filename, tilename_dictionary):
        # tilename_keys is a dictionary which maps the char for that tile to its image filename
        #Tiles zoom to the factor that we want
        ## self.tiles is a dictionary of tile bitmaps
        self.tiles = {}
        self.tile_rows = [] ## Each line of the map text file translated into rows of bitmaps
        self.default_tile = pygame.image.load("Images/8x8_grid.png")
        self.load_map_from(map_filename)
        self.load_tiles(tilename_dictionary)
        print(tilename_dictionary.keys())
        self.resized_tiles = {}
        self.process_tiles()
        self.last_zoom_size = 1
        

    def load_map_from(self, map_filename):
        map_file = open(map_filename, 'rb')
        if map_file:
            for line in map_file:
                print(line)
                line = line.rstrip()
                keys = line[0: :3]
                orientation = line[1: :3]
                row = zip(keys, orientation)
                self.tile_rows.append(row)
        print ("Set map complete!")
##        print (pprint.pprint(self.tile_rows))

    def load_tiles(self, tilename_dictionary):
        width, height = self.default_tile.get_size()
        for key in tilename_dictionary:
            try:
                tile= pygame.image.load(tilename_dictionary[key])
                width, height = tile.get_size()
                self.tiles[key] = tile
            except KeyError:
                print (key + " not found! Maybe it is corrupted?")
            except IOError:
                print ("cannot open file - "+title)
                
    def process_tiles(self, zoom_factor=1):
        width, height = self.default_tile.get_size()
        new_size = int(width*zoom_factor), int(height*zoom_factor)
        self.resized_default_tile = pygame.transform.scale(self.default_tile, new_size)
        for key in self.tiles.keys():
            tile = self.tiles[key]
            #resized_tile = pygame.transform.scale(tile, new_size)
            resized_tile = pygame.image.load("Images/critter.bmp")
            self.resized_tiles[key] = {}
            for orientation, angle in zip(["0", "1", "2", "3"], [0, 90, 180, 270]):
                #self.resized_tiles[key][orientation] = pygame.transform.rotate(resized_tile, angle)
                self.resized_tiles[key][orientation] = resized_tile
              

    def on_tick(self,evt):
        pass

    def on_zoom(self,evt):
        if evt.zoom_size != self.last_zoom_size:
            self.resize(zoom_factor = evt.zoom_size)
        

    def draw_to(self,surface):
        width, height = self.default_tile.get_size()
        y = 0
        for row in self.tile_rows:
            x =0
            for char,orient in row:
                if char != b" ":
                    try:
                        tile_img = self.tiles[char][orient]
                    except:
                        tile_img = self.default_tile
                    surface.blit(tile_img,(x,y))
                x += width
            y += height


    def dump_chars(self):
        for row in self.tile_rows:
            st = "".join([elem[0] for elem in row])
            print(st)

    
    
    
def test():

    pygame.init()
    screen = pygame.display.set_mode( (800,600) )
    tile_files = MAP_DICTIONARY

    layer = Layer("Maps/cathedral2_walls.txt", tile_files)
    #layer.resize(1/16.0)
    layer.draw_to(screen)
    
    pygame.display.flip()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
    pygame.quit()

def test_2():
    pygame.init()
    screen = pygame.display.set_mode( SCREEN_SIZE )
    tile_files = MAP_DICTIONARY
    image = pygame.image.load("Images/cathedral_wall_corner.png")
    screen.blit(image, (0,0))
    screen.blit(pygame.transform.scale(image, (100,100)), (100,100))
    screen.blit(pygame.transform.rotate(image, 90), (200,200))
    pygame.display.flip()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
    
if __name__ == "__main__":
    test()


    
                
                    

