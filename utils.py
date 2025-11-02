from directions import *
import go

K = 1000  # 千
M = 1000000  # 百万
B = 1000000000  # 十亿

Watering = False  # 是否需要浇灌

side = get_world_size()  # 地图边长
area = side**2  # 地图面积


def update():
    global side
    global area
    side = get_world_size()
    area = side**2


def _till():  # 只耕地
    if get_ground_type() == Grounds.Grassland:
        till()
    elif can_harvest():
        harvest()
    return True


def _plant(pe):  # 只种植
    if get_entity_type() == None or get_entity_type() == Entities.Dead_Pumpkin:
        plant(pe)
        if Watering == True:
            jiao_shui()
        return True
    return False


def jiao_shui():  # 浇灌
    if num_items(Items.Water) and get_water() <= 0.75:
        use_item(Items.Water)
        return True
    return False


def _harvest():  # 收获
    if can_harvest():
        harvest()
        return True
    return False


def cost(pe, area):  # 成本
    map = get_cost(pe)
    for i in map:
        if num_items(i) <= (map[i] * area):
            return False
    return True


def fertilize():  # 施肥
    if not can_harvest():
        use_item(Items.Fertilizer)
        return True
    return False


def _unlock(item):  # 解锁费用
    map = get_cost(item)
    if not len(map):
        return 1000000000
    for i in map:
        return map[i]


def reverse(array):  # 翻转
    for i in range(len(array)):
        array.insert(i, array.pop())
    return array


def sort(array):  # 升序排序
    result = []

    for item in array:
        inserted = False
        for i in range(len(result)):
            if (item[0] + item[1]) < (result[i][0] + result[i][1]):
                result.insert(i, item)
                inserted = True
                break
        if not inserted:
            result.append(item)

    return result


def out(itme, target):  # 是否break
    if target == None:
        return False
    if num_items(itme) < target:
        return False
    return True


def loop(func, way, target):  # 循环
    while True:
        if way == None:
            var = func()
        else:
            var = func(way)
        if var != False:
            if out(var, target):
                return True
        else:
            return False


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


def zigzag_Y(side=get_world_size()):  # 蛇形
    if side % 2:
        return None
    result = []
    for x in range(side):
        if x % 2:
            for _ in range(side - 1):
                result.append(down)
        else:
            for _ in range(side - 1):
                result.append(up)
        result.append(right)
    return result


def zigzag_X(side=get_world_size()):  # 蛇形
    if side % 2:
        return None
    result = []
    for y in range(side):
        if y % 2:
            for _ in range(side - 1):
                result.append(left)
        else:
            for _ in range(side - 1):
                result.append(right)
        result.append(up)
    return result


def stair_X(side=get_world_size()):  # 梯形
    result = []
    for _ in range(side):
        for _ in range(side):
            result.append(right)
        result.append(up)
    return result


def stair_Y(side=get_world_size()):  # 梯形
    result = []
    for _ in range(side):
        for _ in range(side):
            result.append(up)
        result.append(right)
    return result
