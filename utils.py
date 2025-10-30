K = 1000  # 千
M = 1000000  # 百万
B = 1000000000  # 十亿

Watering = False  # 是否需要浇灌


def jiao_shui():
    if num_items(Items.Water) and get_water() <= 0.75:
        use_item(Items.Water)
        return True
    return False


def dan_1(pe):
    if get_entity_type() == None or get_entity_type() == Entities.Dead_Pumpkin:
        plant(pe)
        if Watering:
            jiao_shui()
        return True
    return False


def shou_huo():
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


def _unlock(item):  # 解锁
    map = get_cost(item)
    if not len(map):
        return 1000000000
    for i in map:
        return map[i]


def reverse(array): # 翻转
    for i in range(len(array)):
        array.insert(i, array.pop())
    return array


def sort(array):
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
