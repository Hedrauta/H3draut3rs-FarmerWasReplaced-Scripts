from helper import *
change_hat(Hats.Sunflower_Hat)
goto(0,0)
tct = num_items(Items.Power)
while True:
	sunflowers = dict()
	for i in range(15,6,-1):
		sunflowers[i] = set()
	drones = dict()
	drones_ret = dict()
	for i in range(32):
		def add_entry(set, key, valuex, valuey, end = False):
			set[key].add((valuex,valuey))
			if end:
				return set
		def sfp():
			goto(i,0)
			sf = dict()
			for key in range(15,6,-1):
				sf[key] = set()
			sf[None] = set()
			for y in range(32):
				mktill()
				plant(Entities.Sunflower)
				petals = measure()
				if y < 31:
					add_entry(sf,petals,get_pos_x(),get_pos_y())
				else:
					return add_entry(sf,petals,get_pos_x(),get_pos_y(), True)
				move(North)
		drones[i] = spawn_drone(sfp)
		while num_drones() == max_drones():
			pass
	for drone in drones:
		if drones[drone] != None:
			drones_ret[drone] = wait_for(drones[drone])
	for drone in drones_ret:
		for petal in drones_ret[drone]:
			if petal != None:
				for coord in drones_ret[drone][petal]:
					sunflowers[petal].add(coord)
	for i  in range(15,6,-1):
		while num_drones() > 1:
			pass
		for coord in sunflowers[i]:
			def hsf():
				(x,y) = coord
				goto(x,y)
				while not can_harvest():
					if get_water() < .75:
						use_item(Items.Water)
					pass
				harvest()
				sunflowers[i].remove(coord)
			if num_drones() < max_drones():
				spawn_drone(hsf)
			while num_drones() == max_drones():
				pass
