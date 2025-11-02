from utils import B
filename = "Pumpkin_multi"
sim_unlocks = Unlocks
sim_items = {}
for i in Items:
    sim_items[i] = 1*B

sim_globals = {}
seed = 0
speedup = 64
time_s = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)
print(time_s/60)
