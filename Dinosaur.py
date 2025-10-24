from __builtins__ import *
from helper import *
change_hat(Hats.Brown_Hat)
wosi = get_world_size()
goto(0,0)

change_hat(Hats.Dinosaur_Hat)
bones = set() # coord-list unsorted, can been "searched"
bone_list = [] # coord-list in order, remove first entry, if len > bone_length, append new location
bone_length = 2 # Start with 2 "possible bones", increase by one everytime apple been eaten

def update(x,y):
	quick_print((x,y), bone_length, bones, bone_list)
	if not (x,y) in bones:
		if len(bones) >= bone_length:
			old_bone = bone_list[0]
			bones.remove(old_bone)
			bone_list.pop(0)
		bones.add((x,y))
		bone_list.append((x,y))

def smove(dir, step2 = False):
		if step2:
			move(dir)
			update(get_pos_x(), get_pos_y())
		move(dir)
		update(get_pos_x(), get_pos_y())

applex, appley = 0,0
mx, my = get_pos_x(), get_pos_y()
on_apple = applex == mx and appley == my
while True:
	if (applex == mx and appley == my):
		applex, appley = measure()
	while applex != mx or appley != my:
		if (mx == 1 and my < wosi - 2 and not (mx,my+2) in bones) and (appley - 1 > my or appley < my) and not on_apple:
			smove(North, True)
		elif (mx == 0) and (my > 0) and not on_apple:
			smove(South)
		elif (my+1) % 2 and not on_apple:
			if (mx == wosi - 1):
				smove(North)
			else:
				smove(East)
		elif not on_apple:
			if mx > 1 and my <= wosi-1:
				smove(West)
			elif mx == wosi - 1 or (my < wosi - 1 and mx == 1):
				smove(North)
			else:
				smove(West)
		
		mx, my = get_pos_x(), get_pos_y()
		on_apple = applex == mx and appley == my
	bone_length += 1