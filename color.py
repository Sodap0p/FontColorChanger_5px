from PIL import Image
from pathlib import Path
import os


def color_addition_pixel(pixel_color, addcolor):
    new_red = int(pixel_color[0] + addcolor[0])
    new_green = int(pixel_color[1] + addcolor[1])
    new_blue = int(pixel_color[2] + addcolor[2])
    new_red = max(0, min(new_red, 255))
    new_green = max(0, min(new_green, 255))
    new_blue = max(0, min(new_blue, 255))
    return(new_red, new_green, new_blue)


def color_addition_image(image, new_color):
    x, y = 0, 0
    for x in range(0,5):
        for y in range(0,5):
            pixel_color = image.getpixel((x, y))
            if pixel_color[3] < 255:
                continue
            image.putpixel((x, y), color_addition_pixel(pixel_color,new_color))
    return image



def iter_dir(start_dir, end_dir, color_name, color):
    file_list = os.listdir(start_dir)
    for f_ in file_list:
        image = Image.open(f'{start_dir}\\{f_}')
        image = color_addition_image(image, color)
        f_ = f_.replace("black", color_name)
        image.save(f'{end_dir}\\{f_}')
        image.close()


def iter_colors(start_dir, end_dir, color_dict):
    for key, value in color_dict.items():
        iter_dir(start_dir, end_dir, key, value)

    
# get the font file and define color

start_dir = "C:\\Users\\smbowles\\Desktop\\WorkingDIr\\fonts_before"
end_dir = "C:\\Users\\smbowles\\Desktop\\WorkingDIr\\fonts_after"
color_dict = {"green":(0,255,0),
              "red":(255,0,0),
              "blue":(0,0,255),
              "yellow": (255,255,0),
              "white": (255,255,255)
              }

iter_colors(start_dir, end_dir, color_dict)

