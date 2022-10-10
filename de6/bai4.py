
n=int(input())
t=[0]*n
t[1]=1
for i in range(1,n):
	t[i]=t[i-1]+i
for i in range(n):
	for j in range(i,n):
		if t[j]-t[i-1]==n:
			print(str(n)+'=',end='')
			for k in range(i,j):
				print(str(k)+'+',end='')
			print(k+1)
		