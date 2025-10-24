from __builtins__ import *
from helper import *
change_hat(Hats.Cactus_Hat)
si = get_world_size()
goto()
mkgrass()
while not can_harvest():
	pass
harvest()
fl = True
hc = []
cc = []
# Todo: Multidrone
while True: 
	if not fl:
		goto(hc[1][0],hc[1][1])
		while not can_harvest():
			pass
		harvest()
		hc = cc
		goto(cc[1][0],cc[1][1])
	if fl:
		hc = (Entities.Grass,(0,0))
		fl = False
	cc = get_companion()
	goto(cc[1][0],cc[1][1])
	water = get_water()
	if water < 0.01:
		use_item(Items.Water, 4)
	elif water < 0.75:
		cal = ((1 - water) / 0.25)
		hmw = cal - (cal % 1)
		use_item(Items.Water, hmw)
	if get_entity_type() != cc[0]:
		if cc[0] == Entities.Grass:
			mkgrass()
			harvest()
		elif cc[0] == Entities.Carrot:
			mktill()
			plant(Entities.Carrot)
		else:
			plant(cc[0])