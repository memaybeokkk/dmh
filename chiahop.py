k,a,b,v=[int(x) for x in input().split()]
sn=(a-1)//v+1
sh=(sn-1)//k+1
if sn-sh<=b:
	print(sh)
else:
	print(sn-b)