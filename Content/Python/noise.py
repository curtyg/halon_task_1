import unreal
from unreal import Vector
import math
import random


def get_constant_vector(perm_value):

    v = perm_value % 8

    match v:
        case 0:
            return Vector(1, 1, 1)
        case 1:
            return Vector(-1, 1, 1)
        case 2:
            return Vector(1, -1, 1)
        case 3:
            return Vector(1, 1, -1)
        case 4:
            return Vector(1, -1, -1)
        case 5:
            return Vector(-1, 1, -1)
        case 6:
            return Vector(-1, -1, 1)
        case 7:
            return Vector(-1, -1, -1)


def fade(t):
    return t * t * t * (t * (t * 6 - 15) + 10)


def lerp(t, a, b):
    return a + t * (b - a)


def generate(x, y, z):
    ex = math.floor(x) & 511
    ey = math.floor(y) & 511
    ez = math.floor(z) & 511

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

    p = [i for i in range(256)]

    random.shuffle(p)

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

    value_bottom_left_front = p[p[p[ex] + ey] + ez]
    value_bottom_right_front = p[p[p[ex + 1] + ey] + ez]
    value_top_left_front = p[p[p[ex] + ey + 1] + ez]
    value_top_right_front = p[p[p[ex + 1] + ey + 1] + ez]
    value_bottom_left_back = p[p[p[ex] + ey] + ez + 1]
    value_bottom_right_back = p[p[p[ex + 1] + ey] + ez + 1]
    value_top_left_back = p[p[p[ex] + ey + 1] + ez + 1]
    value_top_right_back = p[p[p[ex + 1] + ey + 1] + ez + 1]

    dot_bottom_left_front = bottom_left_front.dot(value_bottom_left_front)
    dot_bottom_right_front = bottom_right_front.dot(value_bottom_right_front)
    dot_top_left_front = top_left_front.dot(value_top_left_front)
    dot_top_right_front = top_right_front.dot(value_top_right_front)
    dot_bottom_left_back = bottom_left_back.dot(value_bottom_left_back)
    dot_bottom_right_back = bottom_right_back.dot(value_bottom_right_back)
    dot_top_left_back = top_left_back.dot(value_top_left_back)
    dot_top_right_back = top_right_back.dot(value_top_right_back)

    u = fade(xf)
    v = fade(yf)
    w = fade(zf)

    # resolve on x-axis

    bottom_front = lerp(u, dot_bottom_left_front, dot_bottom_right_front)
    top_front = lerp(u, dot_top_left_front, dot_top_right_front)
    bottom_back = lerp(u, dot_bottom_left_back, dot_bottom_right_back)
    top_back = lerp(u, dot_top_left_back, dot_top_right_back)

    # resolve on y axis then on z
    return lerp(w, lerp(v, bottom_front, top_front), lerp(v, bottom_back, bottom_front))
