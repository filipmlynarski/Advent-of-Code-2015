import hashlib
m = hashlib.md5()
i=-1
while m.hexdigest()[0:6]!="000000":
	m = hashlib.md5()
	i+=1
	save = m.update("yzbqklnj"+str(i))
print m.hexdigest()
print i