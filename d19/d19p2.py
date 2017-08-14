import sys
puzle = open("puzzle")
puzzle = []
for p in puzle:
	if len(p) > 1 and (p[1] == ' ' or p[2] == ' '):
		puzzle.append(p.split('\n')[0])
	elif len(p) > 1:
		finall = p

working = ['e']
second = []
timer = 0

def swap(x, y, z, position):
	ret = ''
	for i in range(len(x)):
		if i == position and x[i:i + len(y)] == y:
			ret += z
			for j in range(i + len(y), len(x)):
				ret += x[j]
			return ret
		else:
			ret += x[i]
def my_split(x):
	ret = []
	for i in range(len(x)):
		if x[i] == x[i].upper() or x[i] == 'e':
			if i != len(x) - 1 and x[i + 1] == x[i + 1].upper():
				ret.append([x[i], i])
			elif i != len(x) - 1:
				ret.append([x[i] + x[i + 1], i])
			else:
				ret.append([x[i], i])
	return ret

def reverse_numeric(x, y):
	return y - x

def przesiew(x):
	global finall
	score = []
	for i in x:
		score.append(0)
		for idx in range(len(i)):
			if finall[idx] == i[idx]:
				score[len(score) - 1] += 1
			else:
				break
	rett = []
	highest = sorted(score, cmp=reverse_numeric)
	j = 0
	for i in range(len(x)):
		if score[i] == highest[j]:
			rett.append(x[i])
			j += 1
			if j == 500:
				return [rett, highest[0]]
	return [x, highest[0]]

while True:
	timer += 1
	for current in working:
		splited = my_split(current)
		for each in splited:
			for line in puzzle:
				if line[:len(each[0])] == each[0]:
					second.append(swap(current, each[0], line.split(' => ')[1], each[1]))
					if len(second[len(second) - 1]) > finall:
						second.pop()
					elif second[len(second) - 1] == finall:
						print second[len(second) - 1]
						print timer
						sys.exit()
	working = przesiew(second)[0]
	print przesiew(second)[1]
	#print len(working)
	#print len(working[len(working) - 1])
	second = []
	if timer == 20:
		sys.exit()