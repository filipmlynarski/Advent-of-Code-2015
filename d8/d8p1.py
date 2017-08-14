lista = open("tekst")
lght = 0
lght2 = 0
chars = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f']
def check(x):
	for y in range(len(chars)):
		if x==chars[y]:
			return True
def first():
	if (i[j]=='\\' and i[j+1]=='\"') or (i[j]=='\\' and i[j+1]=='\\'):
		return True
def second():
	if i[j]=='\\' and i[j+1]=='x':
		if check(i[j+2]):
			if check(i[j+3]):
				return True
for i in lista:
	save1 = lght
	save = lght2
	i=i.split("\n")
	i=i[0]
	print i
	lght+= len(i)
	lght2-=2
	freeze=0
	for j in range(len(i)-2):
		lght2+=1
		if freeze<1:
			if first():
				print i[j:j+2]
				lght2-=1
				freeze=2
			elif second():
				print i[j:j+4]
				freeze=4
				lght2-=3
		freeze-=1
	lght2+=2
	print lght - save1
	print lght2 - save
print lght - lght2