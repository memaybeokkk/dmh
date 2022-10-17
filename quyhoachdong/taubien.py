a=[4,2,1,3,4]
a=['j']+a
s1=6
n=len(a)
d=[0]*n 
Sl=0
def xuli():
	global d,Sl
	s=s1;tmax=0;tongmax=0;l=[0]*(s+1);l[0]=1
	for i in range(1,n):
		for st in range(tongmax,-1,-1):
			if st+a[i]<=s:
				if l[st+a[i]]==0 and l[st]!=0 and d[i]==0:
					l[st+a[i]]=i 
					if tongmax<st+a[i]:
						tongmax=st+a[i]
		if tongmax>tmax:
			tmax=tongmax
	s=tmax
	while s>0:
		i=l[s]
		if i>=1:
			print(a[i],end=' ')
			d[i]=1
			Sl+=1
			s-=a[i]
while Sl!=n-1:
	xuli()
	print()


