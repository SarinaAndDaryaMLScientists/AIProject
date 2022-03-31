import math
from PIL import Image, ImageDraw
import numpy as np
from hexalattice.hexalattice import *

def hexagon_generator(edge_length, offset, edge_num=6):
    """this method generates a hexagon"""
    "it can literally generate any rectangular polygon given the outer angle"
    "the inner angle of the hexagon is 120 which makes the outer 180 - 120 = 60"
    "so that means in each step go by the edge len then turn to tan 60, but python won't get that, it just learned to "
    "move straight and right/ left"
    "so we tell it to move right on cos 60 to right and then move to sin 60 to up"
    "and finally the code is set"
    "although some changes are required to generate any kind of rectangular polygon"
    "i will comment the code below and write the code to generate literally any kind of polygon"
    # a, b = offset
    # for angle in range(0, 360, 60):
    #     a += math.cos(math.radians(angle)) * edge_length
    #     b += math.sin(math.radians(angle)) * edge_length
    #      a, b
    "this part of function is just like saying that append x& y to a list and then return the list."
    a, b = offset
    "sorry for persian commenting my English is not perfect"
    "اینجا مبدا مختصات رو نقطه a,b در نظر میگیریم که میتونیم داخل بازی به هر دلیلی عوضش کنیم."
    "this means a = offset[0] and b = offset[1]"
    each_outer_degree = 360 // edge_num
    for teta in range(0, 360, each_outer_degree):
        a += np.cos(np.radians(teta)) * edge_length
        b += np.sin(np.radians(teta)) * edge_length
        yield a, b


def fun():
    image = Image.new('RGB', (1000, 1000), 'white')

    draw = ImageDraw.Draw(image)
    startx = 0,
    starty = 0;
    len  = 2 * 50
    hexagon = hexagon_generator(50, offset=(200, 200))
    hexagon2 = hexagon_generator(50, offset=(200, 285))
    hexagon3 = hexagon_generator(50, offset=(200, 115))
    # hexagon4 = hexagon_generator(50, offset=(300, ))

    draw.polygon(list(hexagon), outline='black', fill='red')
    draw.polygon(list(hexagon2), outline='black', fill='red')
    draw.polygon(list(hexagon3), outline='black', fill='red')
    draw.polygon(list(hexagon4), outline='black', fill='red')
    image.show()
fun()