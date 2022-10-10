n=int(input())
a=[int(x) for x in input().split()][:n]
t=[0]*n 
t[0]=a[0]

for i in range(1,n):
	t[i]=t[i-1]+a[i]
t=[0]+t
print(t)
for i in range(1,n+1):
	for j in range(i,n+1):
		if t[j]-t[i-1]>0:
			print(i,j)