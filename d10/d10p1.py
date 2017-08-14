tekst = "1113222113"
new = ""
save=1
b=1
for i in range(50):
	for x in range(len(tekst)):
		if x==len(tekst)-1:
			new+=str(save)+tekst[x]
			save=1
		elif tekst[x]==tekst[x+1]:
			save+=1
		else:
			new+=str(save)+tekst[x]
			save=1
	tekst=new
	new=""
print len(tekst)