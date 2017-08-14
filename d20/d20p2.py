import numpy as np

elves = np.zeros((1000000))
i = 0
def check(x):
	ret = 0
	for i in range(x):
		i += 1
		if x % i == 0 and elves[i] < 50:
			ret += i * 12
	return ret
while check(i) < 150:
	i += 1
print i