from constants import *

# # filename_list = [
# #     "Cactus_multi",
# #     "Cactus",
# #     "Pumpkin_multi",
# #     "Pumpkin",
# #     "Sunflower_multi",
# #     "Sunflower",
# # ]
filename = "Sunflower_multi"
sim_unlocks = Unlocks
sim_items = {}
for i in Items:
    sim_items[i] = 1 * B

sim_globals = {}
seed = 0
speedup = 128

# for _ in range(10):
# time_s = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)
# print(filename, ": ", time_s // 60, "分", time_s % 60, "秒")
leaderboard_run(Leaderboards.Sunflowers, filename, speedup)

