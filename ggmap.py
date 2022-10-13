f2=open('ggmap.out','w')
f1=open('ggmap.inp','r')
a=[int(x) for x in f1.readline().split()]
n=a[0]+1;m=a[1];s=a[2];f=5
c=[0]*n 
max=999999
for i in range(n):
	c[i]=[max]*n
for i in f1:
	a=[int(x) for x in i.split()]
	c[a[0]][a[1]]=a[2]
d=[max]*n 
fr=[0]*n 
truoc=[0]*n 
d[s]=0  
u=s 
while u!=f and u!=0:
	min=max 
	for v in range(1,n):
		if d[v]<min and fr[v]==0:
			min=d[v]
			u=v 
	fr[u]=1 
	for v in range(1,n):
		if d[v]>d[u]+c[u][v] and fr[v]==0:
			print(v,d[u]+c[u][v])
			d[v]=d[u]+c[u][v]
			truoc[v]=u 

di=[u]
while truoc[u]!=0:
	di.append(truoc[u])
	u=truoc[u]
print(di[::-1])
