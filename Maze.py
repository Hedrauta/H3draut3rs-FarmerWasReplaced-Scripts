from __builtins__ import *
from helper import *
set_world_size(32)
si = get_world_size()
num = num_unlocked(Unlocks.Mazes)
ws = si*2**(num-1)
goto()
clear()
#Values needed for script
From = South
loop = 0
other_dirs_of = {North: (South, East, West), South: (North, East, West), East: (North, South, West), West: (North, South, East)}
val_other_dirs = {North:({"x":0,"y":-1}, {"x":1,"y":0}, {"x":-1,"y":0}), South: ({"x":0,"y":1}, {"x":1,"y":0}, {"x":-1,"y":0}), East: ({"x":0,"y":1}, {"x":0,"y":-1}, {"x":-1,"y":0}), West: ({"x":0,"y":1},{"x":0,"y":-1},{"x":1,"y":0})}
opposite_of = {North: South, South: North, East:West, West: East}
val_dirs = {North: {"x": 0 , "y": 1}, South: {"x": 0 , "y": -1}, West: {"x": -1, "y": 0}, East: {"x":1, "y": 0}}
(treasurex,treasurey) = (0,0)
(mx,my) = (get_pos_x(), get_pos_y())
on_treasure = False

#Function:
def do_maze():
	use_item(Items.Weird_Substance, ws)
def move_x_p():
	global From
	if can_move(East):
		move(East)
		From = West
		return True
	else:
		return False
def move_x_n():
	global From
	if can_move(West):
		move(West)
		From = East
		return True
	else:
		return False
def move_y_p():
	global From
	if can_move(North):
		move(North)
		From = South
		return True
	else:
		return False
def move_y_n():
	global From
	if can_move(South):
		move(South)
		From = North
		return True
	else:
		return False
def ded(dead, dir_from):	
	#ded = "Dead End Detection"
	n = list()
	for dir in other_dirs_of[dir_from]:
		n.append(can_move(dir))
	n1, n2, n3 = n[0], n[1], n[2]
	c1, c2, c3 = val_other_dirs[dir_from]
	nx1,ny1 = mx+c1["x"],my+c1["y"]
	nx2,ny2 = mx+c2["x"],my+c2["y"]
	nx3,ny3 = mx+c3["x"],my+c3["y"]
	if xor(not n1, (n1 and (nx1, ny1) in dead))	and xor(not n2, (n2 and (nx2,ny2) in dead)) and xor(not n3, (n3 and (nx3,ny3) in dead)):
		dead.add((mx,my))
		return dead
	else:
		return dead
def dec(Dir, de):
	#Dead-End-Check, needs dir and dead-end-set
	mox,moy = get_pos_x()+val_dirs[Dir]["x"], get_pos_y()+val_dirs[Dir]["y"]
	return (can_move(Dir) and not (mox, moy) in de)

#Prepare Lab:
plant(Entities.Bush)
while not can_harvest():
	if get_water() <= .75:
		use_item(Items.Water)
do_maze()


while loop < 300:
	treasurex, treasurey = measure()
	on_treasure = treasurex == mx and treasurey == my
	dead_ends = set()
	while not on_treasure:
		tmx, tmy = 0,0
		mx, my = get_pos_x(), get_pos_y()
		tmx = treasurex - mx
		tmy = treasurey - my
		if abs(tmx) > abs(tmy):
			if tmx > 0 and dec(East, dead_ends):
				if not From == East and dec(East, dead_ends):
					move_x_p()
				elif tmy > 0:
					if not From == North and dec(North, dead_ends):
						move_y_p()
					elif dec(South, dead_ends):
						if not From == South and can_move(South):
							move_y_n()
						else:
							cx,cy = get_pos_x(), get_pos_y()
							if not (treasurex == cx and treasurey == cy):
								move_x_n()
					else:
						cx,cy = get_pos_x(), get_pos_y()
						if not (treasurex == cx and treasurey == cy):
							move_x_p()
				elif tmy <= 0:
					if not From == South and dec(South, dead_ends):
						move_y_n()
					elif dec(North, dead_ends):
						if not From == North and can_move(North):
							move_y_p()
						else:
							cx,cy = get_pos_x(), get_pos_y()
							if not (treasurex == cx and treasurey == cy):
								move_x_n()
					else:
						cx,cy = get_pos_x(), get_pos_y()
						if not (treasurex == cx and treasurey == cy):
							move_x_p()
				else:
					cx,cy = get_pos_x(), get_pos_y()
					if not (treasurex == cx and treasurey == cy):
						move_x_n()
			elif tmx <= 0 and dec(West, dead_ends):
				if not From == West and dec(West, dead_ends):
					move_x_n()
				elif tmy > 0:
					if not From == North and dec(North, dead_ends):
						move_y_p()
					elif dec(South, dead_ends):
						if not From == South and can_move(South):
							move_y_n()
						else:
							cx,cy = get_pos_x(), get_pos_y()
							if not (treasurex == cx and treasurey == cy):
								move_x_p()
					else:
						cx,cy = get_pos_x(), get_pos_y()
						if not (treasurex == cx and treasurey == cy):
							move_x_n()
				elif tmy <= 0:
					if not From == South and dec(South, dead_ends):
						move_y_n()
					elif dec(North, dead_ends):
						if not From == North and can_move(North):
							move_y_p()
						else:
							cx,cy = get_pos_x(), get_pos_y()
							if not (treasurex == cx and treasurey == cy):
								move_x_p()
					else: 
						cx,cy = get_pos_x(), get_pos_y()
						if not (treasurex == cx and treasurey == cy):
							move_x_n()
				else:
					cx,cy = get_pos_x(), get_pos_y()
					if not (treasurex == cx and treasurey == cy):
						move_x_p()
			elif dec(South, dead_ends) and not From == South:
				move_y_n()
			elif dec(North, dead_ends) and not From == North:
				move_y_p()
			elif dec(West, dead_ends) and not From == West:
				move_x_n()
			elif dec(East, dead_ends) and not From == East:
				move_x_p()
			else:
				quick_print("X: Dead end detected, going ",From,(mx, my), dead_ends)
				cx,cy = get_pos_x(), get_pos_y()
				if not (treasurex == cx and treasurey == cy):
					move(From)

		else:
			if tmy > 0 and dec(North, dead_ends):
				if not From == North and dec(North, dead_ends):
					move_y_p()
				elif tmx > 0:
					if not From == East and dec(East, dead_ends):
						move_x_p()
					elif dec(West, dead_ends):
						if not From == West and can_move(West):
							cx,cy = get_pos_x(), get_pos_y()
							if not (treasurex == cx and treasurey == cy):
								move_x_n()
						else:
							cx,cy = get_pos_x(), get_pos_y()
							if not (treasurex == cx and treasurey == cy):
								move_y_n()
					else:
						cx,cy = get_pos_x(), get_pos_y()
						if not (treasurex == cx and treasurey == cy):
							move_y_n()
				elif tmx <= 0:
					if not From == West and dec(West, dead_ends):
						move_x_n()
					elif dec(East, dead_ends):
						if not From == East and can_move(East):
							move_x_p()
						else:
							cx,cy = get_pos_x(), get_pos_y()
							if not (treasurex == cx and treasurey == cy):
								move_y_n()
					else:
						cx,cy = get_pos_x(), get_pos_y()
						if not (treasurex == cx and treasurey == cy):
							move_y_p()
				else: 
					cx,cy = get_pos_x(), get_pos_y()
					if not (treasurex == cx and treasurey == cy):
						move_y_n()
			elif tmy <= 0 and dec(South, dead_ends):
				if not From == South and dec(South, dead_ends):
					move_y_n()
				elif tmx > 0:
					if not From == East and dec(East, dead_ends):
						move_x_p()
					elif dec(West, dead_ends):
						if not From == West and can_move(West):
							move_x_n()
						else:
							cx,cy = get_pos_x(), get_pos_y()
							if not (treasurex == cx and treasurey == cy):
								move_y_p()
					else:
						cx,cy = get_pos_x(), get_pos_y()
						if not (treasurex == cx and treasurey == cy):
							move_y_p()
				elif tmx <= 0:
					if not From == West and dec(West, dead_ends):
						move_x_n()
					elif dec(East, dead_ends):
						if not From == East and can_move(East):
							move_x_p()
						else:
							cx,cy = get_pos_x(), get_pos_y()
							if not (treasurex == cx and treasurey == cy):
								move_y_p()
					else:
						cx,cy = get_pos_x(), get_pos_y()
						if not (treasurex == cx and treasurey == cy):
							move_y_n()
				else:
					cx,cy = get_pos_x(), get_pos_y()
					if not (treasurex == cx and treasurey == cy):
						move_y_p()
			elif dec(East, dead_ends) and not From == East:
				move_x_p()
			elif dec(West, dead_ends) and not From == West:
				move_x_n()
			elif dec(South, dead_ends) and not From == South:
				move_y_n()
			elif dec(North, dead_ends) and not From == North:
				move_y_p()
			else:
				quick_print("Y: Dead end detected, going ",From,(mx, my), dead_ends)
				cx,cy = get_pos_x(), get_pos_y()
				if not (treasurex == cx and treasurey == cy):
					move(From)
		ld = len(dead_ends)
		mx, my = get_pos_x(), get_pos_y()
		dead_ends = ded(dead_ends, From)
		on_treasure = treasurex == mx and treasurey == my
		if not on_treasure and (len(dead_ends) > ld):
			move(From)
	if loop < 300:
		do_maze()
		loop += 1
		on_treasure = False
	else:
		harvest()