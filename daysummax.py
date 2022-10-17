f2=open('daysummax.out','w')
with open('daysummax.inp','r') as f1:
	n=int(f1.readline())+1
	s=f1.readline()
a=[0]+[int(i) for i in s.split()]
#[0, 12, -34, 14, 11, 9, -8, 15, 11, -7, -56, 17, 16, 19]

T=[0]*n
T[0]=a[0]
for i in range(1,n):
	T[i]=T[i-1]+a[i]
#[0, 12, -22, -8, 3, 12, 4, 19, 30, 23, -33, -16, 0, 19]
dmax=0
csd=csc=[]
out=''

print(sum(a))
for i in range(1,n):
	for j in range(i,n):

		if (T[j]-T[i-1])%3==0 and j-i+1>dmax:
			dmax=j-i+1
			csd=[i]
			csc=[j]
		elif (T[j]-T[i-1])%3==0 and j-i+1==dmax:
			csd.append(i)
			csc.append(j)
print(csd,csc)
f2.write(str(dmax)+' '+str(len(csc)))
f2.write('\n')
for i in range(len(csc)):

	for j in range(csd[i],csc[i]+1):
		out=out+str(a[j])+' '
		

	f2.write(out.rstrip(' '))
	print(out.rstrip(' '))
	f2.write('\n')
	out=''
f2.close()

