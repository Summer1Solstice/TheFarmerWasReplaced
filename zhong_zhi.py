from A import *
def jiao_shui():
	if num_items(Items.Water) and get_water() <= 0.75:
		use_item(Items.Water)


def dan_1(pe):
	if get_entity_type() == None or get_entity_type() == Entities.Dead_Pumpkin:
		plant(pe)
		jiao_shui()


def ji_chu(x, y):
	if get_entity_type() == None:
		if (x + y) % 2:
			plant(Entities.Tree)
		else:
			plant(Entities.Grass)
		jiao_shui()

def shou_huo():
	if can_harvest():
		harvest()