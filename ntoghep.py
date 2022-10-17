from math import sqrt
snt=[True]*1000000
snt[0]=snt[1]=False
for i in range(2,int(sqrt(1000000)+1)):
	if snt[i]:
		for j in range(i*i,1000000,i):
			snt[j]=False
a=[]
b=[]
for i in range(1000000):
	if snt[i]:
		a.append(i)
for i in range(0,len(a)//1000,2):
	if snt[int(str(a[i])+str(a[i+1]))]:
		b.append(int(str(a[i])+str(a[i+1])))
print(b)