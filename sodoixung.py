def doixung(i,j):
	s=a[i:j+1] 
	for i in range(len(s)//2+1):
		if s[i]!= s[len(s)-1-i]:
			return False
	return True
for n in range(0,1000000):
	n=int(n)
	N=n**2
	if doixung(n) and doixung(N):
		print(n,N,sep=' ')
