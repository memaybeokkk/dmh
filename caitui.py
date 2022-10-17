w=[0,1,3,4,5];v=[0,1,4,5,7];n=4;M=7
l=[0]*(n+1)
for i in range(n+1):
	l[i]=[0]*(M+1)
for i in range(1,n+1):
	for j in range(1,M+1):
		l[i][j]=l[i-1][j]
		if j>=w[i] and l[i][j]<l[i-1][j-w[i]]+v[i]:
			l[i][j]=l[i-1][j-w[i]]+v[i]
print(l[n][M])
while n!=1:
	if l[n][M]!=l[n-1][M]:
		print(w[n],v[n],sep=' ')
		M-=w[n]
	n-=1