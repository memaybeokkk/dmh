a,b=[x for x in input().split()]
A=a[::-1]
B=b[::-1]
if int(A)>int(B):
	print(int(A))
else:
	print(int(B))