from constants import *


def cycle(side=get_world_size()):  # 哈密尔顿回路
    if side % 2:
        return None
    result = [up]
    for i in range(side):
        for _ in range(side - 2):
            if i % 2:
                result.append(down)
            else:
                result.append(up)
        result.append(right)

    result[-1] = down
    for i in range(side - 1):
        result.append(left)
    return result


def zigzag_Y(
    side=get_world_size(), direction={"odd": down, "even": up, "newline": right}
):  # 蛇形
    if side % 2:
        return None
    result = []
    for x in range(side):
        if x % 2:
            for _ in range(side - 1):
                result.append(direction["odd"])
        else:
            for _ in range(side - 1):
                result.append(direction["even"])
        result.append(direction["newline"])
    return result


def zigzag_X(
    side=get_world_size(), direction={"odd": left, "even": right, "newline": up}
):  # 蛇形
    return zigzag_Y(side, direction)


def stair_X(side=get_world_size(), direction={"advance": right, "newline": up}):  # 梯形; 有缺陷
    result = []
    for _ in range(side):
        for _ in range(side):
            result.append(direction["advance"])
        result.append(direction["newline"])
    return result


def stair_Y(side=get_world_size(), direction={"advance": up, "newline": right}):  # 梯形
    return stair_X(side, direction)


def line(direction=up, len=get_world_size()):  # 直线
    result = []
    if not (direction in [North, South, West, East]):
        return None
    for _ in range(len):
        result.append(direction)
    return result
