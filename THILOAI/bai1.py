a,d=[float(x) for x in input().split()]
n=int(input())
x=y=0
for i in range(n):
	if 0<x<a :
		if y==0:
			if x+d>a:
				y=x+d-a
				x=a
			else:
				x+=d 
		elif y==a:
			if x-d<0:
				y=a+x-d
				x=0
			else:
				x-=d 
	elif 0<y<a:
		if x==0:
			if y-d<0:
				x=d-y
				y=0
			else:
				y-=d
		elif x==a:
			if y+d>a:
				x=a-(y+d-a)
				y=a 
			else:
				y+=d 
	elif x==y==0:
		x+=d 
	elif x==0 and y==a:
		y=a-d
	elif x==a and y==0:
		y+=d 
	elif x==y==a:
		x-=d

	print("{:.4f}".format(x), "{:.4f}".format(y))