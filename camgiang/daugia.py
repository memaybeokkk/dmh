from math import sqrt

a,b=[10,100000]
snt=[True]*100001
snt[0]=snt[1]=False
for i in range(2,int(sqrt(100001))+2):
	if snt[i]==True:
		for j in range(i**2,100001,i):
			snt[j]=False
def doixung(s):
	s=str(s)
	n=len(s)
	for i in range(n//2+1):
		if s[i]!=s[n-i-1]:
			return False
	return True
dem=0
for i in range(a,b+1):
	if snt[i]:
		if doixung(i):
			dem+=1
print(dem)
