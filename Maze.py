from __builtins__ import *
from helper import *
si = get_world_size()
num = num_unlocked(Unlocks.Mazes)
ws = si*2**(num-1)
set_world_size(32)
From = ""
im = {From:None}

opposite_of = {North:South, South:North, West:East, East:West}
left_of = {North:West, West:South, South:East, East:North}
right_of = {North:East, East:South, South:West, West:North}

loop = 1

# TODO: Multidrone non-visited

while True:
	he = get_entity_type() != Entities.Hedge
	tr = get_entity_type() != Entities.Treasure
	if not ((he or tr) and not (he and tr)):
		goto(si//2,si//2)
		#startup
		use_item(Items.Water,4)
		plant(Entities.Bush)
		while not can_harvest():
			pass
		use_item(Items.Weird_Substance, ws)
		loop = 0
	# treasure Pos
	tpx, tpy = measure()
	# visited area
	va = set()
	
	#dead area
	da = set()
	
	#last4 = loop-breaker
	last = set()
	# self-lock-breaker
	lava = set()
	while not (get_pos_x() == tpx) or not (get_pos_y() == tpy):
		mx = get_pos_x()
		my = get_pos_y()
		if not (mx,my) in va:
			va.add((mx,my))
		omn = (not can_move(East) or (((mx+1,my) in da) and can_move(East))) and (not can_move(South) or (((mx,my-1) in da) and can_move(South))) and (not can_move(West) or (((mx-1,my) in da) and can_move(West)))
		ome = (not can_move(South) or (((mx,my-1) in da) and can_move(South))) and (not can_move(West) or (((mx-1,my) in da) and can_move(West))) and (not can_move(North) or (((mx,my+1) in da) and can_move(North)))
		oms = (not can_move(West) or (((mx-1,my) in da) and can_move(West))) and (not can_move(North) or (((mx,my+1) in da) and can_move(North))) and (not can_move(East) or (((mx+1,my) in da) and can_move(East)))
		omw = (not can_move(North) or (((mx,my+1) in da) and can_move(North))) and (not can_move(East) or (((mx+1,my) in da) and can_move(East))) and (not can_move(South) or (((mx,my-1) in da) and can_move(South)))
		omo = (omn and not (ome or oms or omw)) or (ome and not (oms or omw or omn)) or (oms and not (omw or omn or ome)) or (omw and not (omn or ome or oms))
		
		lenlast = len(last)
		last.add((mx,my))
		if len(last) == lenlast:
			opx = mx
			opy = my
			if im[From] == North:
				opy = opy + 1
			elif im[From] == East:
				opx = opy + 1
			elif im[From] == South:
				opy = opy - 1
			elif im[From] == West:
				opx = opx - 1
			da.add((opx,opy))
			last = set()
		if omo:
			da.add((mx,my))
			if (mx,my) in last:
					last.remove((mx,my))
					last = set()
		if can_move(North) and not im[From] == North and not (mx,my+1) in da:
			lava = set()
			if not (mx,my+1) in va and can_move(North):
				move(North)
				im[From] = South
			elif not (mx+1,my) in va and can_move(East):
				move(East)
				im[From] = West
			elif not (mx,my-1) in va and can_move(South):
				move(South)
				im[From] = North
			elif not (mx-1,my) in va and can_move(West):
				move(West)
				im[From] = East
			else:
				move(North)
				im[From] = South
		elif can_move(East) and not im[From] == East and not (mx+1,my) in da:
			lava = set()
			if not (mx+1,my) in va and can_move(East):
				move(East)
				im[From] = West
			elif not (mx,my-1) in va and can_move(South):
				move(South)
				im[From] = North
			elif not (mx-1,my) in va and can_move(West):
				move(West)
				im[From] = East
			elif not (mx,my+1) in va and can_move(North):
				move(North)
				im[From] = South
			else:
				move(East)
				im[From] = West
		elif can_move(South) and not im[From] == South and not (mx, my-1) in da:
			lava = set()
			if not (mx,my-1) in va and can_move(South):
				move(South)
				im[From] = North
			elif not (mx-1,my) in va and can_move(West):
				move(West)
				im[From] = East
			elif not (mx,my+1) in va and can_move(North):
				move(North)
				im[From] = South
			elif not (mx+1,my) in va and can_move(East):
				move(East)
				im[From] = West
			else:
				move(South)
				im[From] = North
		elif can_move(West) and not im[From] == West and not (mx-1,my) in da:
			lava = set()
			if not (mx-1,my) in va and can_move(West):
				move(West)
				im[From] = East
			elif not (mx,my+1) in va and can_move(North):
				move(North)
				im[From] = South
			elif not (mx+1,my) in va and can_move(East):
				move(East)
				im[From] = West
			elif not (mx,my-1) in va and can_move(South):
				move(South)
				im[From] = North
			else:
				move(West)
				im[From] = East
		elif omo:
			if omn and im[From] == North and not (mx,my+1) in lava:
				da.add((mx,my))
				if (mx,my) in last:
					last.remove((mx,my))
					last = set()
					va = set()
				move(North)
				im[From] = South
			elif ome and im[From] == East and not (mx+1,my) in lava:
				da.add((mx,my))
				if (mx,my) in last:
					last.remove((mx,my))
					last = set()
					va = set()
				move(East)
				im[From] = West
			elif oms and im[From] == South and not (mx,my-1) in lava:
				da.add((mx,my))
				if (mx,my) in last:
					last.remove((mx,my))
					last = set()
					va = set()
				move(South)
				im[From] = North
			elif omw and im[From] == West and not (mx-1,my) in lava:
				da.add((mx,my))
				if (mx,my) in last:
					last.remove((mx,my))
					last = set()
				move(West)
				im[From] = East
			else:
				if can_move(opposite_of[im[From]]):
					move(opposite_of[im[From]])
				elif can_move(right_of[im[From]]):
					move(right_of[im[From]])
				elif can_move(left_of[im[From]]):
					move(left_of[im[From]])
				else:
					lava.add((mx,my))
					move(opposite_of[im[From]])
					

		else:
			print("burnt: ", (mx,my),"Loop: ", loop)
			print(lava)
			if can_move(North) and not (mx,my+1) in lava:
				lava.add((mx,my))
				lava.add((mx,my+1))
				move(North)
				im[From] = South
			elif can_move(East) and not (mx+1,my) in lava:
				lava.add((mx,my))
				lava.add((mx+1,my))
				move(East)
				im[From] = West
			elif can_move(South) and not (mx,my-1) in lava:
				lava.add((mx,my))
				lava.add((mx,my-1))
				move(South)
				im[From] = North
			elif can_move(West) and not (mx-1,my) in lava:
				lava.add((mx,my))
				lava.add((mx-1,my))
				move(West)
				im[From] = East
			else:
				da = set()
				va = set()
				lava = set()
				
			
			
	harvest()
