lista = open("tekst")
allowed_chars=["a","e",'i','o','u']
pas = True
wynik_ostateczny=0
def check(x):
	wynik=0
	for j in x:
		for ij in allowed_chars:
			if j==ij:
				wynik+=1
	if wynik>=3:
		return True
	else:
		return False
def check2(x):
	wynik=0
	for j in range(len(x)-1):
		if x[j]==x[j+1]:
			return True
	return False
def check3(x):
	wynik=0
	for j in range(len(x)-1):
		if x[j:j+2]=="ab" or x[j:j+2]=="cd" or x[j:j+2]=="pq" or x[j:j+2]=="xy":
			return False
	return True
for i in lista:
	linia = i.split("\n")
	linia = linia[0]
	if check(linia):
		if check2(linia):
			if check3(linia):
				wynik_ostateczny+=1
print wynik_ostateczny