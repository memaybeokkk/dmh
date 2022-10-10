f2=open('ggmap.out','w')
f1=open('ggmap.inp','r')
a=[int(x) for x in f1.readline().split()]
n=a[0];m=a[1];S=int(a[2]);f=a[3]
c=[0]*(n+1)
max=999
for i in range(n+1):
	c[i]=[0]*(n+1)
for i in range(n+1):
	for j in range(n+1):
		c[i][j]=max
for i in f1:
	s=[int(x) for x in i.split()]
	u=s[0]
	v=s[1]
	c[u][v]=s[2]
d=[0]*(n+1)
fr=[0]*(n+1)
truoc=[0]*(n+1)

for i in range(n+1):
	d[i]=max 
d[S]=0
while u!=f and u!=0:
	u=0
	min=max 
	for v in range(1,n+1):
		if d[v]<min and fr[v]==0:

			min=d[v]

			u=v

	fr[u]=1 
	for v in range(n+1):
		if d[v]>d[u]+c[u][v] and fr[v]==0:
			d[v]=d[u]+c[u][v]
			truoc[v]=u 

          
f=u 
print(f)
while truoc[f]!=0:
	print(truoc[f])
	f=truoc[f]



f2.close()