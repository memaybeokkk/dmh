f2=open('dayconduong.out','w')
with open('dayconduong.inp','r') as f1:
	n=int(f1.readline())
	s=f1.readline()
a=[int(i) for i in s.split()]
f=[0]*n 
dmax=0
if a[0]>0:
	f[0]=1
else:
	f[0]=0
for i in range(1,n):
	if a[i]>0:
		f[i]=f[i-1]+1
	else:
		f[i]=0
	if f[i]>dmax:
		dmax=f[i]
		cs=[i]
	elif f[i]==dmax:
		cs.append(i)
if dmax==1:
	f2.write('0')
else:
	f2.write(str(dmax)+' '+str(len(cs)))
f2.write('\n')
for i in cs:
	for j in range(i-dmax+1,i+1):
		f2.write(str(a[j])+' ')
	f2.write('\n')
f2.close()