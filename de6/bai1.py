from math import sqrt
x1=int(input())
y1=int(input())
r1=int(input())
x2=int(input())
y2=int(input())
r2=int(input())
l=sqrt((x1-x2)**2+(y1-y2)**2)
if l>r1+r2:
	print(l-r1-r2)
elif l==0:
	print(abs(r1-r2))
elif l<=r1+r2:
	if l>=r1 or l>=r2 or l==r1+r2:
		print(0)
	elif l<r1 :
		print(r1-l-r2)
	elif l<r2:
		print(r2-l-r1)

