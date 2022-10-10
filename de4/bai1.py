n=5
k=5
a=[0]*n
for i in range(n):
	a[i]=[0]*n
for i in range(n):
	for j in range(n):
		a[i][j]=(i+1)*(j+1)
		if a[i][j]==k:
			print(a)