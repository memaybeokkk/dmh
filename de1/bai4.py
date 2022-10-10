f2=open('bai4.out','w')
with open('bai4.inp','r') as f1:
	k=int(f1.readline())
	a=f1.readline()
n=int(len(a))
dem=0
for i in range(0,n):
	d=0
	for j in range(i,n):
		if a[j]=='1'and d<2:
			d+=1
			if d==2:
				dem+=1
			elif d>2:
				break
		if d==2 and a[j]=='0':
			dem+=1

	
f2.write(str(dem))
f2.close()