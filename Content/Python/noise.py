import unreal
import itertools
from unreal import Vector
import math
import random
import sys



def get_constant_vector(perm_value):

    # I would have used a match statment below but for some reason
    # my unreal engine python version is 3.9.7 despite it saying
    # in the docs that it should be 3.11.8 (maybe this is the dif between 5.3 and 5.4)
    val = perm_value % 8

    if val == 0:
        return Vector(1, 1, 1)
    elif val == 1:
        return Vector(-1, 1, 1)
    elif val == 2:
        return Vector(1, -1, 1)
    elif val == 3:
        return Vector(1, 1, -1)
    elif val == 4:
        return Vector(1, -1, -1)
    elif val == 5:
        return Vector(-1, 1, -1)
    elif val == 6:
        return Vector(-1, -1, 1)
    elif val == 7:
        return Vector(-1, -1, -1)


def fade(t):
    return t * t * t * (t * (t * 6 - 15) + 10)


def lerp(t, a, b):
    return a + t * (b - a)


def get__permutation_list(seed: int, permuation_wrap_size: int = 256):
    permutation: list[int] = [i for i in range(permuation_wrap_size)]
    random.seed(seed)
    random.shuffle(permutation)
    return permutation * 2

def generate(x: float, y: float, z: float, seed: int):
    
    ex = math.floor(x) & 255
    ey = math.floor(y) & 255
    ez = math.floor(z) & 255

    xf = z - math.floor(x)
    yf = y - math.floor(y)
    zf = z - math.floor(z)

    top_right_front = Vector(xf - 1.0, yf - 1.0, zf - 1.0)
    top_left_front = Vector(xf, yf - 1.0, zf - 1.0)
    top_right_back = Vector(xf - 1.0, yf - 1.0, zf)
    top_left_back = Vector(xf, yf - 1.0, zf)
    bottom_right_front = Vector(xf - 1.0, yf, zf - 1.0)
    bottom_left_front = Vector(xf, yf, zf - 1.0)
    bottom_right_back = Vector(xf - 1.0, yf, zf)
    bottom_left_back = Vector(xf, yf, zf)
    
    # p[p[ex] + ey] + ez              #AA
    # p[p[ex + 1] + ey] + ez          #BA
    # p[p[ex] + ey + 1] + ez          #AB
    # p[p[ex + 1] + ey + 1] + ez      #BB

    # 0,1,0                         and 1,1,1
    # p[p[p[0] + 1]]                p[p[p[1] + 1] + 1] - #bottomleftfront
    # p[p[p[1] + 1]]                p[p[p[2] + 1] + 1]
    # p[p[p[0] + 2]]                p[p[p[1] + 2] + 1] - #topleftfront
    # p[p[p[1] + 2]]                p[p[p[2] + 2] + 1]

    # p[p[p[0] + 1] + 1]            p[p[p[1] + 1] + 2]
    # p[p[p[1] + 1] + 1]            p[p[p[2] + 2] + 1] - #bottomrightback
    # p[p[p[0] + 2] + 1]            p[p[p[1] + 2] + 1]
    # p[p[p[1] + 2] + 1]            p[p[p[2] + 2] + 1] - #toprightback

    # toprightback = topleftfront       = p[p[p[1] + 2] + 1]
    # bottomrightback = bottomleftfront = p[p[p[1] + 1] + 1]

    p = get__permutation_list(seed)

    value_bottom_left_front = p[p[p[ex] + ey] + ez]
    value_bottom_right_front = p[p[p[ex + 1] + ey] + ez]
    value_top_left_front = p[p[p[ex] + ey + 1] + ez]
    value_top_right_front = p[p[p[ex + 1] + ey + 1] + ez]
    value_bottom_left_back = p[p[p[ex] + ey] + ez + 1]
    value_bottom_right_back = p[p[p[ex + 1] + ey] + ez + 1]
    value_top_left_back = p[p[p[ex] + ey + 1] + ez + 1]
    value_top_right_back = p[p[p[ex + 1] + ey + 1] + ez + 1]

    dot_bottom_left_front = bottom_left_front.dot(
        get_constant_vector(value_bottom_left_front)
    )
    dot_bottom_right_front = bottom_right_front.dot(
        get_constant_vector(value_bottom_right_front)
    )
    dot_top_left_front = top_left_front.dot(get_constant_vector(value_top_left_front))
    dot_top_right_front = top_right_front.dot(
        get_constant_vector(value_top_right_front)
    )
    dot_bottom_left_back = bottom_left_back.dot(
        get_constant_vector(value_bottom_left_back)
    )
    dot_bottom_right_back = bottom_right_back.dot(
        get_constant_vector(value_bottom_right_back)
    )
    dot_top_left_back = top_left_back.dot(get_constant_vector(value_top_left_back))
    dot_top_right_back = top_right_back.dot(get_constant_vector(value_top_right_back))

    u = fade(xf)
    v = fade(yf)
    w = fade(zf)

    # resolve on x-axis
    bottom_front = lerp(u, dot_bottom_left_front, dot_bottom_right_front)
    top_front = lerp(u, dot_top_left_front, dot_top_right_front)
    bottom_back = lerp(u, dot_bottom_left_back, dot_bottom_right_back)
    top_back = lerp(u, dot_top_left_back, dot_top_right_back)

    # resolve on y axis then on z
    return lerp(w, lerp(v, bottom_front, top_front), lerp(v, bottom_back, top_back))

