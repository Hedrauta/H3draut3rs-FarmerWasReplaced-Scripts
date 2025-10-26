change_hat(Hats.Brown_Hat)
from __builtins__ import *
from helper import *
si = get_world_size()
goto(0,0)
fert = False
# TODO: Multidrone, wosi/maxdrone logic, vert und horizontal movement sorting,
# NOTE: after plant, spawn drones, do sort, if numdrones == 32 behave as master and sort nort and east pos
# TODO: Planting vert multidrone
# NOTE: only works on 32 drones

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
	ws = 200
	while not sorted:
		sorted = True
		for y in range(32):
			ce = measure()
			we = 0
			ea = 99
			no = 99
			so = 0
			if get_pos_x() < 31:
				ea = measure(East)
			if get_pos_x() > 0:
				we = measure()
			if get_pos_y() < 31:
				no = measure(North)
			if get_pos_y() > 0:
				so = measure(South)
			if we > ce:
				sorted = False
				while not swap(West):
					pass
				if we > ea:
					while not swap(East):
						pass
			elif ce > ea:
				sorted = False
				while not swap(East):
					pass
				if we > ea:
					while not swap(West):
						pass
			ce = measure()
			if so > ce:
				sorted = False
				while not swap(South):
					pass
				if so > no:
					while not swap(North):
						pass
			elif ce > no:
				sorted = False
				while not swap(North):
					pass
				if so > no:
					while not swap(South):
						pass
			move(North)
		if not sorted and num_drones() < 30:
			if get_pos_x() > 0:
				move(West)
				spawn_drone(sort)
				move(East)
			if get_pos_x() < 31:
				move(East)
				spawn_drone(sort)
				xmove(West,2)
				move(East)
def run():
	sird = si//max_drones()
	for x in range (32):
		move(East)
		spawn_drone(drplant)
	drplant()
	goto()
	for x in range(32):
		move(East)
		spawn_drone(sort)
	sort()

if __name__ == "__main__":
	run()
	while num_drones() > 1:
		pass
	goto()
	harvest()
	quick_print(num_items(Items.Cactus))