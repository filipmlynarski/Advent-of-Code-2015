import time

puzle = open('puzzle')
puzzle = []
for p in puzle:
	puzzle.append(p.split('\n')[0])
idx = 0
a = 1
b = 0
while idx < len(puzzle):
	if puzzle[idx][:3] == 'hlf':
		if puzzle[idx].split(' ')[1] == 'a':
			a /= 2
		else:
			b /= 2
	elif puzzle[idx][:3] == 'tpl':
		if puzzle[idx].split(' ')[1] == 'a':
			a *= 3
		else:
			b *= 3
	elif puzzle[idx][:3] == 'inc':
		if puzzle[idx].split(' ')[1] == 'a':
			a += 1
		else:
			b += 1
	elif puzzle[idx][:3] == 'jmp':
		jmp = puzzle[idx].split(' ')[1]
		if jmp[0] == '+':
 			idx += (int(jmp[1:]) - 1)
		else:
			idx -= (int(jmp[1:]) + 1)
		
	elif puzzle[idx][:3] == 'jie':
		if puzzle[idx].split(' ')[1][0] == 'a':
			if a % 2 == 0:
				jmp = puzzle[idx].split(',')[1].split(' ')[1]
				if jmp[0] == '+':
					idx += (int(jmp[1:]) - 1)
				else:
					idx -= (int(jmp[1:]) + 1)
		else:
			if b % 2 == 0:
				jmp = puzzle[idx].split(',')[1].split(' ')[1]
				if jmp[0] == '+':
					idx += (int(jmp[1:]) - 1)
				else:
					idx -= (int(jmp[1:]) + 1)
	elif puzzle[idx][:3] == 'jio':
		if puzzle[idx].split(' ')[1][0] == 'a':
			if a == 1:
				jmp = puzzle[idx].split(',')[1].split(' ')[1]
				if jmp[0] == '+':
					idx += (int(jmp[1:]) - 1)
				else:
					idx -= (int(jmp[1:]) + 1)
		else:
			if a == 1:
				jmp = puzzle[idx].split(',')[1].split(' ')[1]
				if jmp[0] == '+':
					idx += (int(jmp[1:]) - 1)
				else:
					idx -= (int(jmp[1:]) + 1)
	idx += 1

print 'a =', a
print 'b =', b