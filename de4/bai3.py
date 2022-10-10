n=10 
s=19
a=[5,1,3,5,10,7,4,9,2,8]

t=[0]*n
min=n
t[0]=a[0]

for i in range(1,n):
	t[i]=t[i-1]+a[i]
for i in range(1,n):

	for j in range(i,n):
		if t[j]-t[i-1]>=s:

			if j-i+1<min:
				min=j-i+1
				break
print(min)