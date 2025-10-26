from __builtins__ import *
from helper import *
change_hat(Hats.Pumpkin_Hat)
wosi = get_world_size() #WOrldSize
bla = wosi//7
nofili = (wosi-bla)//7 #Number Of FIelds in a LIne
#nofi = nofili**2 #Number Of FIelds
# Todo: Multidrones
def ppump():
	homex, homey = get_pos_x(), get_pos_y()
	for x in range(7):
		for y in range(7):
			water = get_water()
			if water < 0.01:
				use_item(Items.Water, 4)
			elif water < 0.75:
				hmw = (1-water) // 0.25
				use_item(Items.Water, hmw)
			#if num_items(Items.Fertilizer) > 0:
			#	use_item(Items.Fertilizer, 1)
			if get_ground_type() != Grounds.Soil:
				mktill()
				plant(Entities.Pumpkin)
			elif get_entity_type() != Entities.Pumpkin:
				plant(Entities.Pumpkin)
			if y < 6:
				if (x+1) % 2:
					move(North)
				else:
					move(South)
		move(East)
	goto(homex,homey)

def ensure_health():
	homex, homey = get_pos_x(), get_pos_y()
	dpump = set()
	for x in range(7):
		for y in range(7):
			mx,my = get_pos_x(),get_pos_y()
			if get_entity_type() != Entities.Pumpkin:
				dpump.add((mx,my))
				plant(Entities.Pumpkin)
			if y < 6:
				if (x+1) % 2:
					move(North)
				else:
					move(South)
		move(East)
	while len(dpump) > 0:
		dp2 = set()
		for d in dpump:
			dp2.add(d)
		for d in dpump:
			goto(d[0],d[1])
			if can_harvest():
				pass
			if get_entity_type() != Entities.Pumpkin:
				plant(Entities.Pumpkin)
			elif can_harvest() and get_entity_type() == Entities.Pumpkin:
				dp2.remove(d)
		dpump = set()
		for d in dp2:
			dpump.add(d)
	goto(homex,homey)
def logic():
	drone = 0
	if drone == 0:
		drone = num_drones()
	if drone == 1:
		goto()
		while num_drones() < max_drones():
			spawn_drone(logic)
			for i in range(50):
				pass
	drowo = drone - 1
	drofix = (drowo // nofili) * 8
	drofiy = (drowo % nofili) * 8
	goto(drofix,drofiy)
	while True:
		ppump()
		ensure_health()
		harvest()

if __name__ == "__main__":
	logic()