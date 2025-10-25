from direction import *


def cycle(side=get_world_size()):
    if side % 2:
        return None
    result = [up]
    for i in range(side):
        for ii in range(side - 2):
            if i % 2:
                result.append(down)
            else:
                result.append(up)
        result.append(right)

    result[-1] = down
    for i in range(side - 1):
        result.append(left)
    return result


def zigzag_Y(side=get_world_size()):
    if side % 2:
        return None
    result = []
    for x in range(side):
        if x % 2:
            for y in range(side - 1):
                result.append(down)
        else:
            for y in range(side - 1):
                result.append(up)
        result.append(right)
    return result


def zigzag_X(side=get_world_size()):
    if side % 2:
        return None
    result = []
    for y in range(side):
        if y % 2:
            for x in range(side - 1):
                result.append(left)
        else:
            for x in range(side - 1):
                result.append(right)
        result.append(up)
    return result


def stair_X(side=get_world_size()):
    result = []
    for _ in range(side):
        for _ in range(side):
            result.append(right)
        result.append(up)
    return result


def stair_Y(side=get_world_size()):
    result = []
    for _ in range(side):
        for _ in range(side):
            result.append(up)
        result.append(right)
    return result
