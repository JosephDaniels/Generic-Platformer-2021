from constants import *

import pygame


class Layer(object):
    def __init__(self, map_filename, tilename_dictionary, zoom = 1.0):
        # tilename_keys is a dictionary which maps the char for that tile to its image filename
        #Tiles zoom to the factor that we want
        ## self.tiles is a dictionary of tile bitmaps
        self.tile_width = int(128*zoom)
        self.tile_height = int(128*zoom)
        self.tiles = {}
        self.tile_rows = [] ## Each line of the map text file translated into rows of bitmaps
        self.default_tile = pygame.image.load("Images/8x8_grid.png")
        self.load_map_from(map_filename)
        self.load_tiles(tilename_dictionary)
        self.resized_tiles = {}
        self.process_tiles()

    def load_map_from(self, map_filename):
        map_file = open(map_filename, 'r')
        if map_file:
            for line in map_file:
                print(line)
                line = line.rstrip()
                keys = line[0: :3]
                orientation = line[1: :3]
                row = zip(keys, orientation)
                self.tile_rows.append(row)
        print ("Set map complete!")

    def load_tiles(self, tilename_dictionary):
        """load the tiles"""
        width, height = self.default_tile.get_size()
        for key in tilename_dictionary:
            try:
                filename = tilename_dictionary[key]
                tile = pygame.image.load(filename).convert_alpha()
                width, height = tile.get_size()
                self.tiles[key] = tile
            except KeyError:
                print (key + " not found! Maybe it is corrupted?")
            except IOError:
                print ("cannot open file - "+tile)

    def process_tiles(self):
        """for each tile, create rotated and resized version"""
        new_size = self.tile_width, self.tile_height
        for key in self.tiles.keys():
            tile = self.tiles[key]
            resized_tile = pygame.transform.scale(tile, new_size)
            self.resized_tiles[key] = {}
            for orientation, angle in zip(["0", "1", "2", "3"], [0, 90, 180, 270]):
                self.resized_tiles[key][orientation] = pygame.transform.rotate(resized_tile, angle)

              

    def on_tick(self,evt):
        pass



    def draw_to(self,surface):
        y = 0
        for row in self.tile_rows:
            x = 0
            for char,orient in row:
                if char != ' ' or orient != ' ':
                    try:
                        tile_img = self.resized_tiles[char][orient]
                        surface.blit(tile_img, (x, y))
                    except:
                        print("Unknown char", char,"or orientation", orient)
                x += self.tile_width
            y += self.tile_height


    def dump_chars(self):
        for row in self.tile_rows:
            st = "".join([elem[0] for elem in row])
            print(st)



    
    




def test():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    tile_files = MAP_DICTIONARY

    wall_layer =  Layer("Maps/cathedral2_walls.txt", tile_files, zoom=0.125)
    floor_layer = Layer("Maps/cathedral2_floor.txt", tile_files, zoom=0.125)
    furniture_layer = Layer("Maps/cathedral2_furniture.txt", tile_files, zoom=0.125)

    floor_layer.draw_to(screen)
    wall_layer.draw_to(screen)
    furniture_layer.draw_to(screen)

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

if __name__ == "__main__":
    test()

    
                
                    

