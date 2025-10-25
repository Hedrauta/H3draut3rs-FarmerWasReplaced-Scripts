#Todo: rework, keeps breaking, remove set, add "avoid-loops" depending on length on first rows
from __builtins__ import *
from helper import *
change_hat(Hats.Traffic_Cone)
goto(0,0)
wosi = get_world_size()
change_hat(Hats.Dinosaur_Hat)
bone_length = 2 # Start with 2 "possible bones", increase by one everytime apple been eaten

applex, appley = 0,0
mx, my = get_pos_x(), get_pos_y()
on_apple = False

#rework starts here:
while True:
	if (applex == mx and appley == my):
		applex, appley = measure()
	while applex != mx or appley != my:
		if (mx == 1 and (my+1) % 2 and my+2 < wosi and not (mx,my+2) in bones) and (appley >= my+2 or appley < my) and not on_apple:
			smove(North, True)
		elif (mx == 0) and (my > 0) and not on_apple:
			smove(South)
		elif ((my+1) % 2 and not on_apple):
			if appley < my and mx == 1 and not (mx,my+2) in bones:
				smove(North)
			elif (mx == wosi - 1):
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