lista = open("tekst")
w, h = 1000, 1000
mapa = [[0 for x in range(w)] for y in range(h)]
for i in lista:
	linijka = i.split(" ")
	if i[5:7]=="on":
		first = linijka[2].split(",")
		second = linijka[4].split(",")
		second[1] = second[1].split("\n")
		second[1] = second[1][0]
		for x in range(int(first[0]),int(second[0])+1):
			for y in range(int(first[1]),int(second[1])+1):
				mapa[x][y]+=1
	elif i[5:7]=="of":
		first = linijka[2].split(",")
		second = linijka[4].split(",")
		second[1] = second[1].split("\n")
		second[1] = second[1][0]
		for x in range(int(first[0]),int(second[0])+1):
			for y in range(int(first[1]),int(second[1])+1):
				if mapa[x][y]>0:
					mapa[x][y]-=1
	else:
		first = linijka[1].split(",")
		second = linijka[3].split(",")
		second[1] = second[1].split("\n")
		second[1] = second[1][0]
		for x in range(int(first[0]),int(second[0])+1):
			for y in range(int(first[1]),int(second[1])+1):
				mapa[x][y]+=2
wynik=0
for x in range(0,1000):
	for y in range(0,1000):
		wynik+=mapa[x][y]
print wynik