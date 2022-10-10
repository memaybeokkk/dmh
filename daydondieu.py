f2=open('daydondieu.out','w')
with open('daydondieu.inp','r') as f1:
	n=int(f1.readline())
	s=f1.readline()
a=[int(i) for i in s.split()]
f=[0]*n
dmax=0
f[0]=1
for i in range(0,n-1):
	if a[i]<a[i+1]:
		f[i+1]=f[i]+1
	else:
		f[i+1]=1
	if f[i+1]>dmax:
		dmax=f[i+1]
		cs=[i+1]
	elif f[i+1]==dmax:
		cs.append(i+1)
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