tekst = "hepxcrrq"
alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
x=0
def swap(str1,index,changer):
	strong = ""
	for x in range(len(str1)):
		if x==index:
			strong+=changer
		else:
			strong+=str1[x]
	return strong
def change(y):
	global tekst
	for j in range(len(alphabet)):
		if tekst[y]==alphabet[j] and tekst[y]!="z":
			tekst = swap(tekst,y,alphabet[j+1])
			return tekst
		elif tekst[y]==alphabet[j] and tekst[y]=="z":
			tekst = swap(tekst,y,alphabet[0])
			change(y-1)
def check1():
	for i in range(len(tekst)-3):
		for j in range(len(alphabet)-2):
			if tekst[i]==alphabet[j] and tekst[i+1]==alphabet[j+1] and tekst[i+2]==alphabet[j+2]:
				return True
	return False
def check2():
	for i in range(len(tekst)):
		if tekst[i]=="i" or tekst[i]=="o" or tekst[i]=="l":
			return False
	return True
def check3():
	for i in range(len(tekst)-1):
		if tekst[i]==tekst[i+1]:
			for j in range(i+2,len(tekst)-1):
				if tekst[j]==tekst[j+1]:
					return True
	return False
while x<2:
	change(len(tekst)-1)
	if check1():
		if check2():
			if check3():
				print tekst
				x+=1