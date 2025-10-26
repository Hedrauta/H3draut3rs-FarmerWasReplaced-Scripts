from helper import *
tests = list()
for i in range(1):
	runtime = simulate("ashton_sunflower", Unlocks, {Items.Carrot:10000000, Items.Power:50000, Items.Water:2000000}, {}, 0, 100)
	tests.append(runtime)
test_count = len(tests)
test_time_total = 0
for i in tests:
	test_time_total += i
test_time_avg = test_time_total / test_count
rt_min = test_time_avg // 60
rt_sec = test_time_avg % 60
quick_print(rt_min,":",rt_sec)