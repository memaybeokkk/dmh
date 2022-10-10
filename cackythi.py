x=9
d=[0]*x
k=3
for i in range(k):
	a=[int(x) for x in input().split()]
	if a[0]==1:
		d[a[1]]=d[a[2]]=1
	else:
		d[a[1]]=1
b=[]
for i in range(1,x):
	if d[i]==0:
		b.append(i)
d=len(b)
j=0
while j<len(b)-1:
	if b[j+1]-b[j]==1:
		d-=1
		j+=2
	j+=1
print(d,len(b))