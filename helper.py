def mktill():
	if get_ground_type() != Grounds.Soil:
		till()
def mkgrass():
	if get_ground_type() != Grounds.Grassland:
		till()
def xmove(Direction = North, Steps = 0):
	for i in range(Steps):
		move(Direction)
def goto(x=0,y=0):
	si = get_world_size()
	mx = get_pos_x()
	my = get_pos_y()
	if mx < x:
		if (mx + si - x) < (x - mx):
			xmove(West,mx + si - x)
		else:
			xmove(East,x - mx)
	elif mx > x:
		if (x + si - mx) < (mx - x):
			xmove(East,x + si - mx)
		else:
			xmove(West,mx-x)
	else:
		pass
	if my < y:
		if (my + si - y) < (y - my):
			xmove(South,my + si - y)
		else:
			xmove(North,y-my)
	elif my > y:
		if (y + si - my) < (my - y):
			xmove(North, y + si - my)
		else:
			xmove(South,my-y)
	else:
		pass
def reverse_set(gset):
	cachel = []
	for item in gset:
		cachel.insert(0, item)
	cache = set()
	for item in cachel:
		cache.add(item)
	return(cache)
def xor(a,b):
	return a != b
def sd_arg(fn, arg):
	def mitm():
		return fn(arg)
	return spawn_drone(mitm)