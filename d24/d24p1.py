import numpy as np
puzle = open('puzzle')
puzzle2 = []
puzzle = []
test = 0

for p in puzle:
	puzzle2.append(p.split('\n')[0])
for idx in range(len(puzzle2)):
	puzzle.append(puzzle2[len(puzzle2) - (idx + 1)])
for p in puzzle:
	test += int(p)
print test / 3
def repair(x, y):
	return (y - len(x)) * '0' + x

def binar(x):
	out = ''
	while x > 0:
		out = str(x % 3) + out
		if x % 3 == 1:
			x = (x - 1) / 3
		else:
			x = x / 3
	return out

def one(x):
	global puzzle

	save1 = 0
	for idx, noumber in enumerate(x):
		if noumber == '0':
			save1 += int(puzzle[idx])

	save2 = 0
	for idx, noumber in enumerate(x):
		if noumber == '1':
			save2 += int(puzzle[idx])

	save3 = 0
	for idx, noumber in enumerate(x):
		if noumber == '2':
			save3 += int(puzzle[idx])

	equal = 508
	if save1 == equal and save2 == equal and save3 == equal:
		return [True, True]
	elif save1 > equal or save2 > equal and save3 > equal:
		return [False, False]
	else:
		return [False, True]


def small(x):
	global puzzle
	tri = 1
	tri2 = [0, 0, 0]
	for idx, i in enumerate(x):
		if i == '0':
			tri2[0] += 1
		elif i == '1':
			tri2[1] += 1
		else:
			tri2[2] += 1
	if tri2[0] < tri2[1] and tri2[0] < tri2[2]:
		liczba = '0'
	elif tri2[1] < tri2[0] and tri2[1] < tri2[2]:
		liczba = '1'
	else:
		liczba = '2'
	for idx, i in enumerate(x):
		if i == liczba:
			tri *= int(puzzle[idx])
	return [tri, np.min(tri2)]

first = [str(i) for i in range(3)]
second = []

smallest = 344266178324
smallest2 = 6

while len(first) > 0:

	f = open('result2','w')
	f.write(str(len(first[0])) + ' - ' + str(len(first)) + ' zamiast ' + str(3 ** len(first[0])))
	print str(len(first[0])) + ' - ' + str(len(first)) + ' zamiast ' + str(3 ** len(first[0])) + ' czyli roznica to ' + str(3 ** len(first[0]) - len(first))
	f.close()
	for c in first:
		one_save = one(c)
		if one_save == [False, True] and len(c) < len(puzzle):
			for i in range(3):
				small2_save = small(c + str(i))
				if smallest > small2_save[0] and smallest2 >= small2_save[1]:
					second.append(c + str(i))
		elif one_save == [True, True]:
			small_save = small(c)
			if smallest > small_save[0] and smallest2 >= small_save[1]:
				smallest = small_save[0]
				smallest2 = small_save[1]
				f = open('result','r+')
				f.write(str('+++++++++++++') + '\n')
				f.write(str(smallest) + '\n')
				f.write(str(c) + '\n')
				f.write(str('+++++++++++++') + '\n')
				f.close()
				print '+++++++++++++'
				print smallest
				print c
				print '+++++++++++++'

	first = second
	second = []