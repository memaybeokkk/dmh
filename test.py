a=[1,2,2,3,2,4,5,2,6,7,6]
b=[0]*1000000000
max=vt=0
for i in a:
	b[i]+=1
	if b[i]>max:
		max=b[i]
		vt=i
	elif b[i]==max and i<cs:
		cs=i
print(i,b[i],b)