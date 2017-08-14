i = 0
def check(x):
	ret = 0
	if x % 2 == 0:
		for i in range(x/2):
			i += 1
			if x % i == 0:
				ret += i * 10
		ret += x * 10
	else:
		for i in range(int(float(x)/4)):
			i += 1
			i *= 2
			i += 1
			if x % i == 0:
				ret += i * 10 + 10
		ret += 10 + 10 * x
	return ret
while check(i) < 10000:
	i += 1
print i