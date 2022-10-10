a=[int(x) for x in input().split()]
n=a[0]
a[0]=0
t=[0]*(n+1)
t[0]=a[0]
for i in range(1,n+1):
	t[i]=t[i-1]+a[i]
min=t[-1]
for i in range(1,n+1):
	m=t[i]-(t[-1]-t[i])
	if m<0:
		m=-m
	if m<min:
		min=m
print(min)