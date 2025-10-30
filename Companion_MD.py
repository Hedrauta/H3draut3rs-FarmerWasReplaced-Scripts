from __builtins__ import *
from helper import *
clear()
change_hat(Hats.Traffic_Cone)
set_world_size(32)
# Todo/Idea: Multidrone, bunny-hop
# NOTE: only works with 32 Drones on size 32
def comp(main):
	while True:
		hx,hy = get_pos_x(),get_pos_y()
		harvest()
		if main == Entities.Carrot:
			mktill()
			plant(Entities.Carrot)
		elif main == Entities.Grass:
			mkgrass()
		else:
			plant(main)
		wa = get_water()
		while wa <= .75:
			use_item(Items.Water)
			wa = get_water()
		(coe,(cx,cy)) = get_companion()
		goto(cx,cy)
		wa = get_water()
		while wa <= .75:
			use_item(Items.Water)
			wa = get_water()
		while not can_harvest() or get_entity_type() == None:
			pass
		if can_harvest():
			harvest()
		ce = get_entity_type() == coe
		if coe == Entities.Carrot and not ce:
			mktill()
			plant(Entities.Carrot)
		elif coe == Entities.Grass and not ce:
			mkgrass()
		elif not ce:
			plant(coe)
		goto(hx,hy)
def run():
	wosi = get_world_size
	order = Entities.Carrot
	while num_drones() < max_drones():
		droi = num_drones() - 1
		sx,sy = (droi*5) % 32, (droi*7) % 32
		goto(sx,sy)
		sd_arg(comp, order)
	sd_arg(comp, 2)
if __name__ == "__main__":
	run()