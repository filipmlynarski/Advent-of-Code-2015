lista = open('text')
wynik=0
for i in lista:
	linia = i.split("x")
	linia[2]=linia[2].split("\n")[0]
	wynik+=2*int(linia[0])*int(linia[1])+2*int(linia[1])*int(linia[2])+2*int(linia[2])*int(linia[0])

	maks = max(int(linia[0]),int(linia[1]),int(linia[2]))
	save = []
	for j in linia:
		if int(j)<int(maks):
			save.append(int(j))
	if len(save)==2 :
		wynik+=save[0]*save[1]
	else:
		wynik+=maks*min(int(linia[0]),int(linia[1]),int(linia[2]))
	save=[]
print wynik
lista.close()