import numpy as np
puzle = open('puzzle')

puzzle = []
avg = 0

for i in puzle:
	puzzle.append(i.split('\n')[0])
	avg += int(i)
avg /= 4

current = []
current2 = []

for idx, i in enumerate(puzzle):
	current.append([])
	current[idx].append(i)

done = True

def check(x, y):
	for i in y:
		if x == i:
			return False
	return True

def compare(x, y):
	ret = []
	for i in x:
		ret.append(i)
	ret.append(y)
	return ret

def sum_of(x):
	equal = 0
	for i in x:
		equal += int(i)
	return equal == avg

def sum_of_rest(x, y):
	global puzzle
	global avg
	ret = 0
	for i in puzzle:
		agree = True
		for j in x:
			if i == j:
				agree = False
		for j in y:
			if i == j:
				agree = False
		if agree:
			ret += int(i)
	return avg == ret

def fits(x):
	print x
	global puzzle
	global check
	global compare
	global sum_of
	puzzle2, x2, x3 = [], [], []
	for i in puzzle:
		dont = False
		for j in x:
			if j == i and dont == False:
				dont = True
		if not dont:
			puzzle2.append(i)
			x2.append([])
			x2[len(x2) - 1].append(i)
	while len(x2[0]) < len(puzzle2):
		for i in range(len(x2)):
			for j in puzzle2:
				if check(j, x2[i]):
					x3.append(compare(x2[i], j))
					if sum_of(x3[len(x3) - 1]):
						return True

		x2 = x3
		x3 = []
	return False

def QE(x):
	ret = 1
	for i in x:
		ret *= int(i)
	return ret

min_qe = QE(puzzle)

while done:
	for idx in range(len(current)):
		for j in puzzle:
			if check(j, current[idx]):
				current2.append(compare(current[idx], j))
				if sum_of(current2[len(current2) - 1]) and QE(current2[len(current2) - 1]) < min_qe:
					print current2[len(current2) - 1]
					print QE(current2[len(current2) - 1])
					min_qe = QE(current2[len(current2) - 1])
					done = False
	current = current2
	current2 = []