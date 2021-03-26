from  PIL import Image, ImageSequence


def convert(gif_filename, target_name):
    """opens a gif_file and splits the images into
    individual png files named {target_name]_xxx.png
    where xxx= 001, 002, etc"""
    with Image.open(gif_filename) as frames:
        num_frames = frames.n_frames
        print("number of frames =", num_frames)
        n = 1
        for frame in ImageSequence.Iterator(frames):
            new_filename = target_name+str(n)+".png"
            print(n, new_filename)
            frame.save(new_filename)
            n += 1

convert("Images\Sprites\Megaman run cycle.gif", "run")
