n=6;s=98
a=[1,2,5,10,50,100]
n=len(a)
kq=[0]*(s+1)
l=[0]*(s+1)
b=[0]*(s+1)
for i in range(1,s+1):
	for j in range(n):
		if a[j]<i:
			if l[i]==0 or l[i-a[j]]+1<l[i]:
				l[i]==l[i-a[j]]
				kq[i]=j
while s>0:
	b[kq[s]]+=1
	s-=a[kq[s]]
for i in range(n):
	print(a[i],b[i],sep=':')
print(b)