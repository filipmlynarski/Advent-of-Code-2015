lista = open("tekst")
pas = True
wynik_ostateczny=0
def check(x):
	for j in range(len(x)-2):
		for v in range(len(x)):
			if(x[j:j+2]==x[v:v+2] and v!=j and v!=j-1 and v!=j+1):
				return True
	return False
def check2(x):
	wynik=0
	for j in range(len(x)-2):
		if x[j]==x[j+2]:
			return True
	return False
for i in lista:
	linia = i.split("\n")
	linia = linia[0]
	if check(linia):
		if check2(linia):
			wynik_ostateczny+=1
print wynik_ostateczny