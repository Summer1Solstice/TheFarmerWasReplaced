from constants import *
from route import *
import go

Watering = False
items_yield = 0


##################work##################
def _harvest():  # 收获
    if can_harvest():
        harvest()
        return True
    return False


def _till():  # 耕地
    if get_ground_type() == Grounds.Grassland:
        till()
    else:
        _harvest()
    return True


def watering():  # 浇水
    if num_items(Items.Water) and get_water() <= 0.75:
        use_item(Items.Water)
        return True
    return False


def _plant(pe):  # 种植
    global Watering
    if get_entity_type() == None or get_entity_type() == Entities.Dead_Pumpkin:
        plant(pe)
        if Watering:
            watering()
        return True
    return False


def fertilize():  # 施肥
    if get_entity_type() == None or get_entity_type() == Entities.Dead_Pumpkin:
        return False
    if num_items(Items.Fertilizer) and not can_harvest():
        use_item(Items.Fertilizer)
        return True
    return False


##################ALL IN WORK##################
def _till_all(way=cycle()):  # 耕地所有
    go.to()
    for i in way:
        _till()
        move(i)
    return True


def _plant_all(way=cycle()):  # 种植所有
    go.to()
    for i in way:
        _plant(i)
        move(i)
    return True


##################多线程##################
def Assign(task, direction=right):  # 多线程分发
    go.to()
    drone_list = []
    for _ in range(max_drones()):
        drone = spawn_drone(task)
        if drone:
            drone_list.append(drone)
        else:
            task()
        move(direction)
    go.to()
    while num_drones() != 1:
        pass
    return drone_list


def _till_multi():  # 多线程耕地
    def work_func():
        for _ in range(get_world_size()):
            till()
            move(up)

    return Assign(work_func)


def _plant_multi(pe):  # 多线程种植
    def work_func():
        for _ in range(get_world_size()):
            plant(pe)
            move(up)

    return Assign(work_func)


##################if##################
def cost(pe, area=get_world_size() ** 2):  # 成本
    map = get_cost(pe)
    for i in map:
        if num_items(i) <= (map[i] * area):
            return False
    return True


def quit(itme, target):  # 是否退出; none 为无限
    if target == None:
        return False
    if target and num_items(itme) < target:
        return False
    return True


def _unlock(item):  # 解锁费用
    map = get_cost(item)
    if not len(map):
        return None
    for i in map:
        return map[i]


def UAVx32():
    if max_drones() == 32:
        return True
    return False


##################list##################
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


##################其他##################
def _yield(item):  # 统计收获
    global items_yield
    if items_yield == 0:
        items_yield = num_items(item)
    else:
        print(num_items(item) - items_yield)
        items_yield = 0
    return True


def loop(func, way, target=False):  # 循环
    while True:
        if way == None:
            var = func()
        else:
            var = func(way)
        if var and quit(var, target):
            return True
        else:
            return False
