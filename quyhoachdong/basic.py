a=['k', 1,0,2,5,3,2,1,4,3,6,8]
d=2
n=len(a)
l=[0]*(n+1)
t=[0]*(n+1)
l[1]=1
for i in range(2,n):
	lmax=0
	for j in range(1,i):
		if a[j]+2==a[i]:
			if l[j]>lmax:
				lmax=l[j]
				t[i]=j
	l[i]=lmax+1
print(a,l,t,sep='\n')
i=l.index(max(l))
p=[]
while True:
	p.append(a[i])
	i=t[i]
	if t[i]==0:
		p.append(a[i])
		break
print(' '.join(str(i) for i in p[::-1]))