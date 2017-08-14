import sys
puzle = open("puzzle")
puzzle = []
for p in puzle:
	if len(p) > 1 and (p[1] == ' ' or p[2] == ' '):
		puzzle.append(p.split('\n')[0])
	elif len(p) > 1:
		finall = p

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

def find(x):
	global puzzle
	for i in puzzle:
		if x == i.split(' => ')[1]:
			return i.split(' => ')[0]

lonk = sorted(str(i.split(' => ')[1]) for i in puzzle if str(i.split(' => ')[0]) != 'e')
lonk = sorted(lonk, key=len, reverse=True)
#print swap(p, 'Rn', 'N', 1)

Time = 0
while p != 'e':
	for i in lonk:
		for idx, j in enumerate(p):
			if idx < len(p) - len(i) + 1 and p[idx: idx + len(i)] == i:
				p = swap(p, p[idx: idx + len(i)], find(i), idx)
				print p
				if p == 'HF' or p == 'NAl' or p == 'OMg':
					p = 'e'
					Time += 1
				Time += 1
				break
print Time