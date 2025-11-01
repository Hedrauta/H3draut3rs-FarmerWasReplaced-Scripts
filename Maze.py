from __builtins__ import *
from helper import *
set_world_size(32)
si = get_world_size()
num = num_unlocked(Unlocks.Mazes)
ws = si*2**(num-1)
goto()


From = "South"
loop = 0
other_dirs_of = {North: (South, East, West), South: (North, East, West), East: (North, South, West), West: (North, South, East)}
val_other_dirs = {North:({"x":0,"y":-1}, {"x":1,y:0}, {"x":-1,"y":0}), South: ({"x":0,"y":1}, {"x":1,"y":0}, {"x":-1,"y":0}), East: ({"x":0,"y":1}, {"x":0,"y":-1}, {"x":-1,"y":0}), West: ({"x":0,"y":1},{"x":0,"y":-1},{"x":1,"y":0})}
opposite_of = {"North": South, "South": North, "East":West, "West": East}
(treasurex,treasurey) = (0,0)
(mx,my) = (get_pos_x(), get_pos_y())
on_treasure = False
def maze():
	use_item(Items.Weird_Substance, ws)

while loop < 300:
	treasurex, treasurey = measure()
	on_treasure = treasurex == mx and treasurey == my
	dead_ends = set()
	
	while not on_treasure:
		tmx, tmy = 0,0
		mx, my = get_pos_x(), get_pos_y
		tmx = treasurex - mx
		tmy = treasurey - my

		def move_x_p():
			if can_move(East):
				move(East)
				From = West
				return True
			else:
				return False
		def move_x_n():
			if can_move(West):
				move(West)
				From = East
				return True
			else:
				return False
		def move_y_p():
			if can_move(North):
				move(North)
				From = South
				return True
			else:
				return False
		def move_y_n():
			if can_move(South):
				move(South)
				From = North
				return True
			else:
				return False
		def ded(dead, dir_from):
			n = ()
			for dir in other_dirs_of[dir_from]:
				n.append(can_move(dir))
			n1, n2, n3 = n[0], n[1], n[2]
			c1, c2, c3 = val_other_dirs[dir_from]
			nx1,ny1 = mx+c1[x],my+c1[y]
			nx2,ny2 = mx+c2[x],my+c2[y]
			nx3,ny3 = mx+c3[x],my+c3[y]
			if xor(not n1, (n1 and (nx1, ny1) in dead))	and xor(not n2, (n1 and (nx2,ny2) in dead)) and xor(not n3, (n3 and (nx3,ny3) in dead)):
				dead.add((mx,my))
				return dead
			else:
				return dead
		