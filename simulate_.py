from utils import B
filename = "Weird_Substance"
sim_unlocks = Unlocks
sim_items = {}
for i in Items:
    sim_items[i] = 1*B

sim_globals = {"itmesTop":200}
seed = 0
speedup = 64
time_s = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)
print(time_s/60)