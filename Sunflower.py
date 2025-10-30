from __builtins__ import *
from helper import *
change_hat(Hats.Sunflower_Hat)
goto(31,0)
tct = num_items(Items.Power)
while True:
	sunflowers = dict()
	for i in range(15,6,-1):
		sunflowers[i] = set()
	drones = dict()
	drones_ret = dict()
	def sfp(i):
		goto(i,0)
		sf = dict()
		for key in range(15,6,-1):
			sf[key] = set()
		for y in range(32):
			mktill()
			plant(Entities.Sunflower)
			petals = measure()
			if y < 31:
				add_entry(sf,petals,get_pos_x(),get_pos_y())
			else:
				return add_entry(sf,petals,get_pos_x(),get_pos_y(), True)
			move(North)
	for i in range(31):
		def add_entry(set, key, valuex, valuey, end = False):
			set[key].add((valuex,valuey))
			if end:
				return set
		
		drones[i] = sd_arg(sfp, i)
	last_entry = sfp(31)
	move(North)
	for drone in drones:
		drones_ret[drone] = wait_for(drones[drone])
	drones_ret[32] = last_entry
	def sfar(pl):
		for p in pl:
			(x,y) = p
			goto(x,y)
			while not can_harvest():
				if get_water() <= .75:
					use_item(Items.Water)
			harvest()
	for i  in range(15,6,-1):
		for drone in drones_ret:
			sd_arg(sfar,drones_ret[drone][i])
			while num_drones() == max_drones():
				pass
	while num_drones() > 1:
		pass
		