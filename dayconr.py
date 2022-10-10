f2=open('daycon.out','w')
with open('daycon.inp','r') as f1:
	s=f1.readline()
	d2=f1.readline()
a=[int(i) for i in d2.split()]
s=s.split()
n=s[0]
d=s[1]
f=[0]*int(n)
dmax=0
f[0]=1
for i in range(0,int(n)-1):
	if a[i]+int(d)==a[i+1]:
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
	for j in range (i-dmax+1,i+1):
		f2.write(str(a[j])+' ')
	f2.write('\n')
f2.close()


