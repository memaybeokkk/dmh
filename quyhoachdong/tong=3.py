a=[3,2,5,1,8,6,3]
a=[0]+a
s=sum(a)
l=[0]*(s+1)
n=len(a)
tongmax=0;l[0]=1
s=s//2
b=[0]*n
while s!=0:
	kt=False
	for i in range(1,n):
		for st in range(tongmax,-1,-1):
			if st+a[i]<=s:
				if l[st+a[i]]==0 and l[st]!=0:
					l[st+a[i]]=i
					if st+a[i]==s:
						kt=True
						break
						
					if st+a[i]>tongmax:
						tongmax=st+a[i]
	if kt==True:
		while s>0:
			if i>=1:
				i=l[s]
				print(a[i],end=' ')
				b[i]=1
				s=s-a[i]
		break
	s-=1
print()
for i in range(1,n):
	if b[i]==0:
		print(a[i],end=' ')