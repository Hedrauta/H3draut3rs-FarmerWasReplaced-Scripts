from helper import *
testruns = 150
testtime = list()
for i in range(testruns):
	runtime = simulate("Cactus_Multidrone", Unlocks, {Items.Pumpkin:10000000, Items.Power:500000, Items.Water:2000000}, {}, -1, 50)
	testtime.append(runtime)
test_time_total = 0
for i in range(testruns):
	test_time_total += testtime[i]
test_time_avg = test_time_total / testruns
rt_min = test_time_avg // 60
rt_sec = test_time_avg % 60
quick_print("Avg time:",rt_min,":",rt_sec,)