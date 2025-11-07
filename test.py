from constants import *

filename_list = [
    "Cactus_multi",
    "Cactus",
    "Pumpkin_multi",
    "Pumpkin",
    "Sunflower_multi",
    "Sunflower",
]
filename = ""
sim_unlocks = Unlocks
sim_items = {}
for i in Items:
    sim_items[i] = 1 * B

sim_globals = {}
seed = 0
speedup = 64

for filename in filename_list:
    time_s = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)

    print(filename, ": ", time_s // 60, "分", time_s % 60, "秒")
