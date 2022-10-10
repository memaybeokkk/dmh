a=[0,1,7,2,6,10,6,5,9]
d=4
l=[0]*(len(a)+1)
t=[0]*(len(a)+1)
l[0]=1
for i in range(1,len(a)):
	lmax=0
	for j in range(0,i):
		if a[i]==a[j]+d:
			if l[j]>=lmax:
				lmax=l[j]
				t[i]=j
	l[i]=lmax+1
max=0
m=[]
for i in range(len(l)):
	if l[i]>max:
		max=l[i]
		m=[i]
	elif l[i]==max:
		m.append(i)
print(m,a,l,t,sep='\n')
for i in m:	
	p=[]
	while t[i]!=0:
		p.append(a[i])
		i=t[i]
		if t[i]==0:
			p.append(a[i])
			break
	print(' '.join(str(i) for i in p[::-1]))