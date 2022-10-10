from math import sqrt
n=int(input())
snt=[True]*(n+1)
snt[0]=snt[1]=False
snto=[]
s=[]
for i in range(2,int(sqrt(n))+1):
	if snt[i]==True:
		for j in range(2,n//i+1):
			snt[i*j]=False
for i in range(n):
	if snt[i]:
		snto.append(i)
for i in snto:
	while n%i==0 :
		n/=i 
		s.append(i)
		if n<=1:
			break 
s=set(s)
print(sum(s))