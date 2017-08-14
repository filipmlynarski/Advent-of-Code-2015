tekst = open("tekst")
citys, amout, amout2, wyniki= [""] ,"", "", []
def check(x):
	for i in citys:
		if x==i:
			return False
	return True
for x in tekst:
	x = x.split(" ")
	if check(x[0]):
		citys.append(x[0])
	if check(x[2]):
		citys.append(x[2])
for i in range(1,len(citys)):
	amout+=str(i)
	amout2+=str(len(citys)-i)
def allowed(x):
	for v in range(len(amout)):
		if x==amout[v]:
			return False
	return True
def check2():
	for j in range(len(str(i))):
		for j1 in range(len(str(i))):
			if (j!=j1 and str(i)[j]==str(i)[j1]) or (allowed(str(i)[j1])):
				return False
	return True
def take(x):
	ret = 0
	for y in range(len(x)-1):
		tekst = open("tekst")
		for y1 in tekst:
			y1 = y1.split("\n")
			y1 = y1[0]
			y1 = y1.split(" ")
			if (y1[0]==citys[int(x[y])] and y1[2]==citys[int(x[y+1])]) or (y1[2]==citys[int(x[y])] and y1[0]==citys[int(x[y+1])]):
				ret+=int(y1[4])
	return ret
test=0
for i in range(int(amout),int(amout2)+1):
	if check2():
		wyniki.append(take(str(i)))
		test+=1
final = wyniki[0]
for x in wyniki:
	final = max(final,x)
print final