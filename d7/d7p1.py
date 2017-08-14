import numpy as np

lista = open("tekst")
kable = []
sygnal = np.uint16([])
liczby=["1","2","3","4","5","6",'7','8','9','0']
def is_integer(x1):
	for i in x1:
		if check(i)==False:
			return False
	return True
def check(x):
	for liczba in liczby:
		if x==liczba:
			return True
	return False
def check2(h1):
	for x in range(len(kable)):
		if h1==kable[x]:
			return False
	return True
end=0
while end==0:
	for i in lista:
		h = i.split(" -> ")
		h = h[1].split("\n")
		h = h[0]
		linijka = i.split(" ")
		if check2(h):
			if linijka[1]=="AND":
				for j in range(len(kable)):
					if kable[j]==linijka[0] or check(linijka[0]):
						for j1 in range(len(kable)):
							if kable[j1]==linijka[2]:
								kable.append(h)
								if check(linijka[0]):
									sygnal = np.uint16(np.append(sygnal, int(sygnal[0])&int(sygnal[j1])))
								else:
									sygnal = np.uint16(np.append(sygnal, int(sygnal[j])&int(sygnal[j1])))					
			elif linijka[1]=="OR":
				for j in range(len(kable)):
					if kable[j]==linijka[0]:
						for j1 in range(len(kable)):
							if kable[j1]==linijka[2]:
								kable.append(h)
								sygnal = np.uint16(np.append(sygnal, int(sygnal[j])|int(sygnal[j1])))
			elif linijka[1]=="LSHIFT":
				for j in range(len(kable)):
					if kable[j]==linijka[0]:
						kable.append(h)
						sygnal = np.uint16(np.append(sygnal, int(sygnal[j])<<int(linijka[2])))
			elif linijka[1]=="RSHIFT":
				for j in range(len(kable)):
					if kable[j]==linijka[0]:
						kable.append(h)
						sygnal = np.uint16(np.append(sygnal, int(sygnal[j])>>int(linijka[2])))
			elif linijka[0]=="NOT":
				for j in range(len(kable)):
					if kable[j]==linijka[1]:
						kable.append(h)
						sygnal = np.uint16(np.append(sygnal, ~int(sygnal[j])))
			else:
				if is_integer(linijka[0]):
					kable.append(h)
					sygnal = np.uint16(np.append(sygnal, int(linijka[0])))
				else:
					for x in range(len(kable)):
						if linijka[0]==kable[x]:
							kable.append(h)
							sygnal = np.uint16(np.append(sygnal, int(sygnal[x])))
	print kable
	for i in range(len(kable)):
		if kable[i]=="a":
			print kable
			print sygnal
			print sygnal[i]
			end+=1