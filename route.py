from A import *

from const import *
def route(side = get_world_size()):
	if side % 2:
		return None
	result = [up]
	for i in range(side):
		for ii in range(side - 2):
			if i % 2:
				result.append(down)
			else:
				result.append(up)
		result.append(right)

	result[-1] = down
	for i in range(side - 1):
		result.append(left)
	return result