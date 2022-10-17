a=[200,10,20,20,50,50,50,100,100]
a=['h']+a 
s1=390
n=len(a)
d=[0]*n
def xuli():
	global d,kt
	s=s1;tongmax=0;tmax=0;kt=False;l=[0]*(s1+1);l[0]=1
	for i in range(1,n):
		for st in range(tongmax,-1,-1):
			if st+a[i]<=s:
				if l[st+a[i]]==0 and l[st]!=0 and d[i]==0:
					l[st+a[i]]=i 
					if st+a[i]==s:
						kt=True
						break
					if tongmax<st+a[i]:
						tongmax=st+a[i]
	if kt==False:
		return ()
	while s>0:
		i=l[s]
		if i>=1:
			print(a[i],end=' ')
			d[i]=1 
			s-=a[i]
while True:
	xuli()
	print()
	if kt==False:
		break