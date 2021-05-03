SCREEN_SIZE = SCREEN_WIDTH,SCREEN_HEIGHT = 800,600

BLACK = (0,0,0)

RED = (255,0,0)

GREEN = (0,255,0)

BLUE = (0,0,255)

GRAVITY = 1.2

JUMP_STRENGTH = 20

ROTATION = {
    ' ' : 0,
    '0' : 0,
    '1' : 90,
    '2' : 180,
    '3' : 270
    }

# This is a map! A dictionary by Care
# a cathedral map which is completely and totally awesome
# this is for joey game!!!

image_folder = "Images/"

##wall_folder =
##floor_folder =

MAP_DICTIONARY = {
    ' ': image_folder + '8x8_grid.png',
    'w': image_folder + 'cathedral_wall_vertical.png',
    'd': image_folder + 'cathedral_wall_diagonal.png',
    'm': image_folder + 'cathedral_floor_m.png',
    'o': image_folder + 'cathedral_door.png',
    'r': image_folder + 'cathedral_redcarpet.png',
    's': image_folder + 'cathedral_stainglass.png',
    'p': image_folder + 'cathedral_pillar.png',
    'g': image_folder + 'grass.png',
    'b': image_folder + 'cathedral_bench.png',
    'e': image_folder + 'cathedral_bench_end.png',
    'E': image_folder + 'cathedral_bench_end_2.png',
    'a': image_folder + 'cathedral_altar.png',
    'z': image_folder + 'cathedral_altar_end.png',
    'Z': image_folder + 'cathedral_altar_end_2.png',
    ' ': image_folder + 'blank.png',
    'c': image_folder + 'cathedral_wall_corner.png',
    'T': image_folder + 'cathedral_wall_t.png',
    'C': image_folder + 'cathedral_wall_cross.png',
    'n': image_folder + 'cathedral_floor_w.png',
    't': image_folder + 'cathedral_stairs_m.png',
    'f': image_folder + 'cathedral_stairs_redcarpet.png'
}