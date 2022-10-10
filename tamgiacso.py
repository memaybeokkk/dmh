c=[0]*6
f=[0]*6
for i in range(6):
	c[i]=[0]*6
	f[i]=[0]*6
f1=open('tamgiacso.inp','r')
d=1
for k in f1:
	a=[0]+[int(x) for x in k.split()]
	for i in range(1,len(a)):
		c[d][i]=a[i]
	d+=1
f[1][1]=c[1][1]
for i in range(2,6):
	f[i][1]=f[i-1][1]+c[i][1]
for i in range(2,6):
	for j in range(2,6):
		if f[i-1][j]>f[i-1][j-1]:
			f[i][j]=f[i-1][j]+c[i][j]
		else:
			f[i][j]=f[i-1][j-1]+c[i][j]
max=0
for i in range(1,6):
	if f[5][i]>max:
		max=f[5][i]
		cs=i
print(max)
