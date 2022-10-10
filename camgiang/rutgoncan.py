from math import sqrt
f1=open('4.inp','r')
n=int(f1.readline())
f2=open('4.out','w')
for i in range(n):
	x=int(f1.readline())
	c=int(sqrt(x))
	if x%(c**2)==0:
		a=int(c)
		b=int(x/a**2)
	else:
		a=1
		b=x
	f2.write(str(a)+ ' '+str(b))
	f2.write('\n')




f1.close()

f2.close()