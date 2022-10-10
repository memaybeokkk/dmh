n=4
x=1000000
a=[True]*x
a[0]=a[1]=False
for i in range(2,x):
	if a[i]==True:
		if i*i==n:
			print('YES')
			break
		for j in range(i*i,x,i):
			a[j]=False
