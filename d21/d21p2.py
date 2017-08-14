import numpy as np
enemy = open('enemy')
shop = open('shop')
items = []
cash = []
for line in shop:
	if len(line.split('\n')[0].split(':')) > 1:
		items.append([])
		index = -1
	else:
		if line.split('\n')[0] != '':
			for things in line.split('\n')[0].split(' '):
				if things != '':
					if len(things) > 4:
						items[len(items)-1].append([])
						index += 1
					items[len(items)-1][index].append(things)
def pas(x):
	if int(i[0]) < 6 and int(i[1]) < 6 and int(i[2]) < 7 and int(i[3]) < 7 and i[2] != i[3]:
		return True
	return False
def set_me(x):
	global items
	ret = [0,0,0]
	if x[0] != '5':
		ret[0] += int(items[0][int(x[0])][1])
		ret[1] += int(items[0][int(x[0])][2])
		ret[2] += int(items[0][int(x[0])][3])
	if x[1] != '5':
		ret[0] += int(items[1][int(x[1])][1])
		ret[1] += int(items[1][int(x[1])][2])
		ret[2] += int(items[1][int(x[1])][3])
	if x[2] != '6':
		ret[0] += int(items[2][int(x[2])][2])
		ret[1] += int(items[2][int(x[2])][3])
		ret[2] += int(items[2][int(x[2])][4])
	if x[3] != '6':
		ret[0] += int(items[2][int(x[3])][2])
		ret[1] += int(items[2][int(x[3])][3])
		ret[2] += int(items[2][int(x[3])][4])
	return ret
def repair(x):
	ret = ''
	ret += (4 - len(x)) * '0'
	ret += x
	return ret
def fight(x):
	my_dmg = x[1]
	my_armor = x[2]
	my_hp = 100
	enemy_dmg = 9
	enemy_armor = 2
	enemy_hp = 103
	while my_hp > 0 and enemy_hp > 0:
		if my_dmg - enemy_armor < 1:
			enemy_hp -= 1
		else:
			enemy_hp -= my_dmg - enemy_armor
		if enemy_hp > 0:
			if enemy_dmg - my_armor < 1:
				my_hp -= 1
			else:
				my_hp -= enemy_dmg - my_armor
		else:
			return True
	return False
for i in range(4566):
	i = str(i)
	i = repair(i)
	if pas(i):
		i = set_me(i)
		if not fight(i):
			cash.append(i[0])
print np.max(cash)