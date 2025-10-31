filename = "Wood"
sim_unlocks = Unlocks
sim_items = {Items.Carrot:1000000000000,Items.Power:0}
sim_globals = {"itmesTop":200}
seed = -1
speedup = 64
time_s = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)
print(time_s/60)