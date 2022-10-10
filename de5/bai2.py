m,n=[int(x) for x in input().split()]
a=[int(x) for x in input().split()][:m]
b=[int(x) for x in input().split()][:n]

dem=0
a.sort(reverse=True)
b.sort(reverse=True)
print(a,b)
for j in b:
	for i in a:
		if i>j:
			dem+=1
			a.remove(i)
			break
print(dem)
