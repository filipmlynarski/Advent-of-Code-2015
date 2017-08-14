import numpy as np
puzle = open('puzzle')

puzzle = []
avg = 0

for i in puzle:
	puzzle.append(i.split('\n')[0])
	avg += int(i)
avg /= 3

got_it = []

def check(x, y):
	for i in x.split(','):
		if i == y:
			return False
	return True

def check2(x):
	global avg
	same = 0
	for i in range(len(x.split(',')) - 1):
		same += int(x.split(',')[i])
	if same == avg:
		return True
	return False

def combinations(x):
	global puzzle
	ret = [i + ',' for i in puzzle]
	ret2 = []
	while len(ret[0].split(',')) < x + 1:
		for i in range(len(ret)):
			for j in range(len(puzzle)):
				if check(ret[i], str(puzzle[j])):
					ret2.append(ret[i] + str(puzzle[j]) + ',')
		ret = ret2
		ret2 = []
	for i in ret:
		if check2(i):
			ret2.append(i)
	return ret2

def idx_of_smalles(x):
	small = x[0]
	idx = 0
	for i in range(len(x)):
		if x[i] < small:
			small = x[i]
			idx = i
	return idx

def qe(x):
	ret = 1
	for i in range(len(x.split(',')) - 1):
		ret *= int(x.split(',')[i])
	return ret

def QE(x):
	ret = []
	x2 = []
	for i in x:
		x2.append(qe(i))
	for i in x2:
		ret.append(x[idx_of_smalles(x2)])
		x2[idx_of_smalles(x2)] = 999
	return ret

def check3(x):
	global puzzle
	x = x.split(',')[:-1]
	puzzle2 = []
	for i in puzzle:
		lel = True
		for j in x:
			if i == j:
				lel = False
		if lel:
			puzzle2.append(i)
	print puzzle2

	return [True, 23]

for i in range(len(puzzle)):
	i += 1
	break
	got_it = combinations(i)
	if len(got_it) > 0:
		got_it = QE(got_it)

		#for j in got_it:
			#if check3(j)[0]:
				#print check3(j)[1]