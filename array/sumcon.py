n='202'
l=len(n)
a=[]
for i in range(l):
	for j in range(i,l):
		print(n[j:i+1])
		a.append(n[j:i+1])
print(a)