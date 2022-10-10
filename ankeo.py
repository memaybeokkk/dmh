m,n=[int(x) for x in input().split()]
a=[]
p=[]
for i in range(m):
	inp=input().lstrip('*')
	print(inp)
	if int(inp.index('S'))>int(inp.index('G')):
		a.append(inp.count('*')+1)
a=sorted(a)
dem=0
while a!=[]:
	min=a[0]
	for i in a:
		if i-min==0:
			p.append(i)
	for i in p:
		a.pop(a.index(i))
	p=[]
	dem+=1
if dem!=0:
	print(dem)
else:
	print(-1)