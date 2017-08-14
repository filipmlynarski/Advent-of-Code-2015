puzle = open('puzzle')
puzzle = []
for p in puzle:
	puzzle.append(p.split('\n')[0])
print puzzle
test = 0
for p in puzzle:
	test += int(p)
print test