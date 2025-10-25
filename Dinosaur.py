from __builtins__ import *
from helper import *
change_hat(Hats.Brown_Hat)
goto(0,0)
wosi = get_world_size()
change_hat(Hats.Dinosaur_Hat)
tail_length = 2 # Start with 1 "tail + head", increase by one everytime apple been eaten

applex, appley = 0,0
mx, my = get_pos_x(), get_pos_y()
on_apple = False

while True:
	applex, appley = measure()
	on_apple = False
	while not on_apple:
		# avoid-loop:
		loops = ((tail_length -(2 * wosi)) // 60) - (my / 2)
		if mx == 1 and (my+1) % 2 and loops > 0 and not on_apple:
			for i in range(loops):
				if appley < my+2:
					break
				xmove(East, wosi-2)
				move(North)
				xmove(West, wosi-2)
				move(North)
				mx,my = get_pos_x(), get_pos_y()
				on_apple = applex == mx and appley == my
			mx, my = get_pos_x(), get_pos_y()
			on_apple = applex == mx and appley == my
		if on_apple:
			break
		#snake-logic:
		if (my+1) % 2 and mx == 1 and (appley-2 >= my or appley < my) and my < 30 and not on_apple:
			move(North)
			mx, my = get_pos_x(), get_pos_y()
			on_apple = applex == mx and appley == my
			yup = move(North)
			if not yup and not on_apple:
				move(East)
		elif mx == 0 and my > 0 and not on_apple:
			move(South)
		elif (my +1 ) % 2 and not on_apple:
			if appley < my and mx == 1:
				yup = move(North)
				if not yup:
					move(East)
			elif mx == wosi - 1:
				move(North)
			else:
				move(East)
		elif not on_apple:
			if mx > 1 and my % 2:
				move(West)
			elif mx == 1 and my < wosi - 1:
				move(North)
			else:
				move(West)
		mx, my = get_pos_x(), get_pos_y()
		on_apple = applex == mx and appley == my
	tail_length += 1
	if (wosi**2) == tail_length:
		break
#harvest():
change_hat(Hats.Brown_Hat)