f2=open('bai3.out','w')
with open('bai3.inp','r') as f1:
	n=int(f1.readline())
	s=f1.readline()
a=[int(i) for i in s.split()]
t=[0]*n
t[0]=a[0]
dmax=0
for i in range(1,n):
	t[i]=t[i-1]+a[i]
for i in range(1,n):
	for j in range(i,n):
		if t[j]-t[i-1]==0:
			if j-i+1>dmax:
				dmax=j-i+1
f2.write(str(dmax))
f2.close()

