s='OOOOOOOOOOOO'
d=0
l=[]
def kt(a,b):
	
	for j in range(b):
		kt=True
		for i in range(1,a+1):
			if s[(i-1)*b+j]=='O':
				kt= False
				break
		if kt== True:
			return kt
	return kt
for a in range(1,13):
	if 12%a==0:
		b=12//a
		if kt(a,b):
			d+=1
			l.append(a)
			l.append(b)
print(d,end=' ')
for i in range(0,len(l),2):
	print(str(l[i])+'x'+str(l[i+1]), end=' ')