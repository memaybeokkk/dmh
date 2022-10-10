x=[0]*50
n=5;k=3
def tohop(i):
	for j in range(x[i-1]+1,n-k+i+1):
		x[i]=j 
		if i==k:
			for I in range(1,k+1):
				print(x[I],end=' ')
			print()
		else:
			tohop(i+1)
tohop(1)