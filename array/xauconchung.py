s1='h19012304'
s2='h034012'
n=len(s2);m=len(s1)
l=[0]*n 
for i in range(n):
	l[i]=[0]*m 
for i in range(1,n):
	for j in range(1,m):
		if s2[i]==s1[j]:
			l[i][j]=l[i-1][j-1]+1
		else:
			l[i][j]=max(l[i-1][j],l[i][j-1])
cs=[]
for j in range(m):
	if l[n-1][j]==l[n-1][m-1]:
		cs.append(j)
max=0
print(cs)
for k in cs:
	i=n-1
	j=k
	c=''

	while i!=0 and j!=0:
		if s2[i]==s1[j]:
			c+=s2[i]
			i-=1
			j-=1
		elif l[i-1][j]==l[i][j]:
			i-=1
		else:
			j-=1
	print(c[::-1])
	if int(c[::-1])>max:
		max=int(c[::-1])
print(max)