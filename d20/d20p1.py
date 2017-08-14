import numpy as np
#i = 831600
i = 1
elves = np.zeros((1000000))
def check(x):
	global elves
	ret = 0
	if x % 2 == 0:
		for i in range(x/2):
			i += 1
			if x % i == 0 and elves[i] < 50:
				elves[i] += 1
				ret += i * 11
		ret += x * 11
		elves[x] += 1
	else:
		for i in range(int(float(x)/4)):
			i += 1
			i *= 2
			i += 1
			if x % i == 0 and elves[i] < 50:
				elves[i] += 1
				ret += i * 11
		ret += 11 * x
		if elves[1] < 50:
			ret += 11
			elves[1] += 1
		elves[x] += 1
	if x % 10000 == 0:
		print x
		print ret
	return ret
while check(i) < 36000000:
	i += 1
print i