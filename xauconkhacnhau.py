n=int(input())
t=[0]*(n+1)
t[0]=0
csd=[]
csc=[]
for i in range(1,n):
	t[i]=t[i-1]+i
for i in range(1,n):
	for j in range(i+1,n):
		if t[j]-t[i-1]==n:
			csd.append(i)
			csc.append(j)
for i in range(len(csd)):
	print('9 =',end=' ')
	for j in range(csd[i],csc[i]):
		
		print(j,'+',end=' ')
	print(csc[i],end='')
	print()
		
	