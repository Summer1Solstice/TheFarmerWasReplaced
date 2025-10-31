from direction import *  # 转换地图方向为屏幕方向
import utils  # 种植、收获、浇水
from utils import K, M, B, side, area

import go  # 前往指定坐标
import Hay  # 草
import Wood  # 木材种植、收获
import Carrot  # 胡萝卜种植、收获
import Pumpkin  # 南瓜种植、收获
import Cactus  # 仙人掌种植、收获
import Bone  # 骨、贪吃蛇
import Sunflower  # 向日葵种植、收获


set_world_size(10)
utils.Watering = True

# 寻路路径
cycle = utils.cycle()  # 环回路径
zigzag_Y = utils.zigzag_Y()  # Y轴蛇形路径
zigzag_X = utils.zigzag_X()  # X轴蛇形路径
stair_X = utils.stair_X()  # X轴楼梯路径
stair_Y = utils.stair_Y()  # Y轴楼梯路径


def run():
    utils.plough(cycle)
    do_a_flip()

    while True:
        if num_items(Items.Hay) <= 1 * M:
            Hay.run(cycle, 50 * M)
        elif num_items(Items.Wood) <= 1 * M:
            Wood.run(cycle, 50 * M)
        elif num_items(Items.Carrot) <= 1 * M:
            Carrot.run(cycle, 50 * M)
        elif num_items(Items.Power) <= 1 * K:
            Sunflower.run(cycle, 50 * K)
        elif num_items(Items.Pumpkin) <= 1 * M:
            Pumpkin.run(cycle, 50 * M)
        elif num_items(Items.Cactus) <= 1 * M and False:
            Cactus.run(cycle, 50 * M)


run()
