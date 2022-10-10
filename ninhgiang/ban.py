N=int(input())
a=[int(x) for x in input().split()][:N]
b=[0]*4
dem=0
a1=0
a2=0
for i in a:
	b[i]+=1
for i in range(len(b)):
	if i==3:
		dem+=b[i]
	elif i==1:
		a1=b[i]
	elif i==2:
		a2=b[i]
if a1==a2:
	print(dem+a1)
else:
	print(dem+max(a1,a2))



