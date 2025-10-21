def jiao_shui():
    if num_items(Items.Water) and get_water() <= 0.75:
        use_item(Items.Water)
        return True
    return False


def dan_1(pe):
    if get_entity_type() == None or get_entity_type() == Entities.Dead_Pumpkin:
        plant(pe)
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
