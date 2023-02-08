import os.path
from random import randint
from PIL import Image, ImageDraw

def circles_generator(num_of_circles=100):

    if not os.path.exists("circles"):
        os.mkdir("circles")

    for pic_name in range(1, num_of_circles + 1):
        ing = Image.new("RGB", (600,600), (255,255,255))
        draw = ImageDraw.Draw(ing)
        draw.ellipse((0,0,600,600), fill=(randint(0,255), randint(0,255),randint(0,255)))
        ing.save(f"circles/{pic_name}.jpg", quality=85)

circles_generator()
