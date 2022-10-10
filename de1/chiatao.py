n=int(input())
a=[int(x) for x in input().split()][:n]
s1=a.count(100)
if s1%2!=0:
	print('NO')
else:
	print('YES')
