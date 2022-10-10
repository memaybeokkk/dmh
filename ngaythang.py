d,m,y=[int(x) for x in input().split()]
n=int(input())
d1=d-n
m1=m 
y1=y 
def songay(m,y):
	if m in [1,3,5,7,8,10,12]:
		return 31
	elif m in [4,6,9,11]:
		return 30
	else:
		if (y%4==0 and y%100!=0) or y%400==0:
			return 29
	return 28
d=d+n 
while d>songay(m,y):
	if d> songay(m,y):
		d-=songay(m,y)
		m+=1
		if m>12:
			m=1
			y+=1
print(d,m,y,sep=' ')

 

while d1<=0:
	m1-=1
	d1+=songay(m1,y1)
	if m1==-1:
		m1=12
		y1-=1
print(d1,m1,y1,sep=' ')