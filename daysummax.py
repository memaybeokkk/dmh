f2=open('daysummax.out','w')
with open('daysummax.inp','r') as f1:
	n=int(f1.readline())
	s=f1.readline()
a=[int(i) for i in s.split()]
T=[0]*n
T[0]=a[0]
dmax=0
csd=csc=[]
out=''
for i in range(1,n):
	T[i]=T[i-1]+a[i]

for i in range(1,n):
	for j in range(i,n):
		if T[j]-T[i-1]>dmax:
			dmax=T[j]-T[i-1]
			csd=[i]
			csc=[j]
		elif T[j]-T[i-1]==dmax:
			csd.append(i)
			csc.append(j)
f2.write(str(dmax)+' '+str(len(csc)))
f2.write('\n')
for i in range(len(csc)):
	for j in range(csd[i],csc[i]+1):
		out=out+str(a[j])+' '
		

	f2.write(out.rstrip(' '))
	f2.write('\n')
	out=''
f2.close()

