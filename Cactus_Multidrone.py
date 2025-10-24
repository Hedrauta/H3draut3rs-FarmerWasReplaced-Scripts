change_hat(Hats.Cactus_Hat)
from helper import *
si = get_world_size()
goto(0,0)

# TODO: Multidrone, wosi/maxdrone logic, vert und horizontal movement sorting,
# TODO: Planting vert multidrone
while True:
# prepare field
	sx = 0
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
	#				use_item(Items.Fertilizer)
				move(North)
			move(East)
	# field prepared, now start sort
	sorted = False
	def sort():
		sorted = False
		while not sorted:
			sort_x = True
			for x in range(si):
				sort_y = True
				for y in range(si):
					ce = measure()
					no = measure(North)
					ea = measure(East)
					we = measure(West)
					so = measure(South)
					if ce > no and get_pos_y() < (si-1):
						sort_y = False
						sort_x = False
						swap(North)
						if no < so and get_pos_y() > 0:
							swap(South)
					elif ce > ea and get_pos_x() < (si -1):
						sort_y = False
						sort_x = False
						swap(East)
						if ea < we and get_pos_x() > 0:
							swap(West)
					else:
						sort_y = True
					move(North)
				if x+1 == si and y+1 == si and sort_x and sort_y:
					sorted = True
				move(East)
	
		
	sird = si//max_drones()
	while num_drones() < max_drones():
		if (si % max_drones()) == 0:
			spawn_drone(drplant)
			xmove(East, si/max_drones())
		else:
			spawn_drone(drplant)
			xmove(East, sird)
	if (si % max_drones()) == 0:
		drplant()
	else:
		drplant()
	while num_drones() < max_drones():
		spawn_drone(sort)
		if (si % max_drones()) == 0:
			xmove(East,si/max_drones())
		else:
			xmove(East, sird)
		pass
	sort()
	goto(0,0)
	while num_drones() != 1:
		pass
	harvest()