change_hat(Hats.Brown_Hat)
from __builtins__ import *
from helper import *
si = get_world_size()
goto(0,0)
fert = False
# NOTE: only works on 32 drones
def wait(sec = 263):
	for i in range(sec):
		pass
def drplant():
	sird = 0
	md = max_drones()
	si = get_world_size()
	if num_drones() != max_drones():
		sird = si//md
	else:
		sird = si - ((md-1)*(si//md))
	for x in range(sird):
		for y in range(si):
			if not get_entity_type() == Entities.Cactus:
				mktill()
				harvest()
				plant(Entities.Cactus)
				if fert:
					use_item(Items.Fertilizer)
			move(North)
		move(East)
	# field prepared, now start sort
	sorted = False
	#rework here:
def sort():
	sorted = False
	sortwe = False
	sortea = False
	while not sorted:
		sorted = True
		sortwe = True
		sortea = True
		for y in range(32):
			if measure() != None:
				mx,my = get_pos_x(),get_pos_y()
				# quick_print((mx,my),measure(),(measure(South), measure(North)), (measure(West), measure(East)))
				if measure(West) > measure() and mx > 0:
					#quick_print((mx,my),measure(),(measure(West), measure(East)))
					swap(West)
					sorted = False
					sortwe = False
					if measure() > measure(East) and mx < 31:
						swap(East)
				if measure() > measure(East) and mx < 31:
					#quick_print((mx,my),measure(),(measure(West), measure(East)))
					swap(East)
					sorted = False
					sortea = False
					if measure(West) > measure() and mx > 0:
						swap(West)
				if measure(South) > measure() and my > 0:
					#quick_print((mx,my),measure(),(measure(South), measure(North)))
					swap(South)
					sorted = False
					if measure() > measure(North) and my < 31:
						swap(North)
				if measure() > measure(North) and my < 31:
					#quick_print((mx,my),measure(),(measure(South), measure(North)))
					swap(North)
					sorted = False
					if measure(South) > measure() and y > 0:
						swap(South)
			move(North)
		if not sorted and num_drones() < 6:
			if get_pos_x() > 1 and not sortwe:
				move (West)
			if get_pos_x() < 30 and not sortea:
				xmove(East,2)
				spawn_drone(sort)
				xmove(West,2)
def run():
	sird = si//max_drones()
	for x in range (32):
		move(East)
		spawn_drone(drplant)
	drplant()
	goto()
	for x in range(32):
		move(East)
		wait()
		spawn_drone(sort)
	sort()

if __name__ == "__main__":
	a = num_items(Items.Cactus)
	run()
	while num_drones() > 1:
		pass
	goto()
	harvest()
	quick_print("yield: ", num_items(Items.Cactus) - a)