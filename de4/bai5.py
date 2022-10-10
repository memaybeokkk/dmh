n=5
s=11
a=[9,2,3,4,1]
a=[0]+a
t=[0]*n 
t[0]=a[0]
min=n 
dem=0

for i in range(1,n):
	t[i]=t[i-1]+a[i]


print(t)
for i in range(1,n):
	for j in range(i,n):
		if t[j]-t[i-1]>=s:
			dem=j-i+1
			
			if dem<min:
				min=dem
print(min)