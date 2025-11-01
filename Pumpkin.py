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
	def loop(extra):
		xr = 3
		if extra:
			xr = 4
		for x in range(xr):
			for y in range(7):
				while get_water() <= .75:
					use_item(Items.Water)
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
	xmove(East, 3)
	dr = sd_arg(loop, True)
	goto(homex,homey)
	loop(False)
	goto(homex,homey)
	while not has_finished(dr):
		pass

def ensure_health():
	homex, homey = get_pos_x(), get_pos_y()
	def loop(extra):
		xr = 3
		if extra:
			xr = 4
		dpump = set()
		for x in range(xr):
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
	xmove(East, 3)
	dr = sd_arg(loop, True)
	goto(homex,homey)
	loop(False)
	goto(homex,homey)
	while not has_finished(dr):
		pass
def logic():
	drone = 0
	if drone == 0:
		drone = num_drones()
	if drone == 1:
		goto()
		while num_drones() < 16:
			spawn_drone(logic)
			for i in range(50):
				pass
	drowo = drone - 1
	drofix = (drowo // nofili) * 8
	drofiy = (drowo % nofili) * 8
	goto(drofix,drofiy)
	while num_drones() < 16:
		pass
	while True:
		ppump()
		ensure_health()
		harvest()

if __name__ == "__main__":
	logic()