def pas2(x):
	global finall_mana
	used_mana = 0
	for i in x:
		if i == '0':
			used_mana += 53
		elif i == '1':
			used_mana += 73
		elif i == '2':
			used_mana += 113
		elif i == '3':
			used_mana += 173
		else:
			used_mana += 229
	if used_mana > finall_mana:
		return False
	for letter1 in range(len(x)):
		if (x[letter1] == '2' or x[letter1] == '3'or x[letter1] == '4') and (letter1 + 2 < len(x) - 1):
			for letter2 in range(letter1 + 1, letter1 + 3):
				if x[letter1] == x[letter2]:
					return False
	return True

def fight(x):

	my_hp = 50
	my_mana = 500
	my_armor = 0
	used_mana = 0
	#my_hp = 10
	#my_mana = 250
	
	enemy_hp = 58
	enemy_dmg = 9
	#enemy_hp = 14
	#enemy_dmg = 8
	
	effect_1 = 0
	effect_2 = 0
	effect_3 = 0

	#equal = '0'
	for i in range(len(x)):
		#if x == equal:
			#print ' '
			#print '-- Player Turn --'
			#print '- Player has', my_hp, 'hit points,', my_armor,'armor,',my_mana,'mana'
			#print '- Boss has',enemy_hp,'hit points'

		my_hp -= 1
		if my_hp < 1:
			return [False, False]

		if effect_1 > 0:
			my_armor = 7
			effect_1 -= 1

			if effect_1 == 0:
				my_armor = 0

			#if x == equal and effect_1 != 0:
				#print 'Shield\'s timer is now ' + str(effect_1) + '.'
			#elif x == equal and effect_1 == 0:
				#print 'Shield\'s timer is now 0.'
				#print 'Shield wears off, decreasing armor by 7.'
				#my_armor = 0
		else:
			my_armor = 0
		if effect_2 > 0:
			enemy_hp -= 3
			effect_2 -= 1
			#if x == equal:
				#print 'Poison deals 3 damage; its timer is now ' + str(effect_2) + '.'
		if effect_3 > 0:
			my_mana += 101
			effect_3 -= 1
			#if x == equal:
				#print 'Recharge provides 101 mana; its timer is now ' + str(effect_3) + '.'
			#if effect_3 == 0:
				#print 'Recharge wears off.'

		if enemy_hp < 1:
			return [True, used_mana]

		if x[i] == '0':
			#if x == equal:
				#print 'Player cast Magic Missle, dealing 4 damage.'
			used_mana += 53

			my_mana -= 53
			enemy_hp -= 4

		elif x[i] == '1':
			#if x == equal:
				#print 'Player cast Drain, dealing 2 damage, and healing 2 hit points.'
			used_mana += 73

			my_mana -= 73
			enemy_hp -= 2
			my_hp += 2

		elif x[i] == '2':
			#if x == equal:
				#print 'Player cast Shield, increasing armor by 7.'
			used_mana += 113

			my_armor = 7
			my_mana -= 113
			effect_1 = 6

		elif x[i] == '3':
			#if x == equal:
				#print 'Player cast Poison'

			used_mana += 173

			my_mana -= 173
			effect_2 = 6

		else:
			#if x == equal:
				#print 'Player cast Recharge'
			used_mana += 229

			my_mana -= 229
			effect_3 = 5

		if my_mana > 0:
			if  enemy_hp > 0:
				#if x == equal:
					#print ' '
					#print '-- Boss Turn --'
					#print '- Player has', my_hp, 'hit points,', my_armor,'armor,',my_mana,'mana'
					#print '- Boss has',enemy_hp,'hit points'
					
				if effect_1 > 0:
					my_armor = 7
					effect_1 -= 1
					if effect_1 == 0:
						my_armor = 0
					#if x == equal and effect_1 != 0:
						#print 'Shield\'s timer is now ' + str(effect_1) + '.'
					#elif x == equal and effect_1 == 0:
						#print 'Shield\'s timer is now 0.'
						#print 'Shield wears off, decreasing armor by 7.'
						#my_armor = 0
				else:
					my_armor = 0
				if effect_2 > 0:
					enemy_hp -= 3
					effect_2 -= 1
					#if x == equal:
						#print 'Poison deals 3 damage; its timer is now ' + str(effect_2) + '.'
				if effect_3 > 0:
					
					my_mana += 101
					effect_3 -= 1
					#if x == equal:
						#print 'Recharge provides 101 mana; its timer is now ' + str(effect_3) + '.'
					#if x == equal and effect_3 == 0:
						#print 'Recharge wears off.'

				if enemy_hp < 1:
					return [True, used_mana, my_mana]

				if enemy_dmg - my_armor < 1:
					#if x == equal:
						#print 'Boss atacks for 1 damage.'
					my_hp -= 1
				else:
					#if x == equal:
						#print 'Boss atacks for',str(enemy_dmg - my_armor),'damage.'
					my_hp -= (enemy_dmg - my_armor)

				if my_hp < 1:
					return [False, False]
			else:
				return [True, used_mana, my_mana]

			
		else:
			return [False, False]
			
	return [False, True]


first = [str(i) for i in range(5)]
second = []
finall_mana = 99999999999

while len(first) > 0:

	for combinations in first:

		fajt = fight(str(combinations))
		if fajt[0]:
			if finall_mana > fajt[1]:

				finall_mana = fajt[1]

				f = open('result','w')
				f.write(str(combinations) + '\n')
				f.write(str(fajt[1]) + '\n')
				f.close()

				print '++++++++++++++++++++++++'
				print combinations
				print fajt[1]
				print '++++++++++++++++++++++++'

		elif fajt[1] == True:
			for i in range(5):
				if pas2(combinations + str(i)):
					second.append(combinations + str(i))

	first = second
	second = []