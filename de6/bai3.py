n=int(input())
a=[]
max=0
for i in range(n):
	a.append(int(input()))
print(a,n)
i=0
while i<len(a):
	dem=0
	while a[i]==0 and i<len(a):
		dem+=1
		i+=1
		if i>=len(a):
			break
	if dem>max:
		max=dem
	i+=1
	if i>=len(a):
		break
print(max)