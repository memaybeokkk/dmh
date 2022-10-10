f2=open('5.out','w')
with open('5.inp','r') as f1:
	k=int(f1.readline())
	a=f1.readline()
dem=0
n=len(a)
for i in range(n):
	for j in range(i,n):
		if a[i:j+1].count('1')==k:
			dem+=1
f2.write(str(dem))