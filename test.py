from directions import *  # 转换地图方向为屏幕方向
import utils  # 种植、收获、浇水
from utils import K, M, B

import go  # 前往指定坐标
import Hay  # 草
import Wood  # 木材种植、收获
import Carrot  # 胡萝卜种植、收获
import Pumpkin  # 南瓜种植、收获
import Cactus  # 仙人掌种植、收获
import Bone  # 骨、贪吃蛇
import Sunflower  # 向日葵种植、收获


side = get_world_size()  # 地图边长
area = side**2  # 地图面积

filename = "Sunflower_multi"
sim_unlocks = Unlocks
sim_items = {}
for i in Items:
    sim_items[i] = 1*B

sim_globals = {}
seed = 0
speedup = 64
time_s = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)
print(time_s/60)
