with open('bt1.inp','r')as f1:
	n=f1.readline()
	s1=f1.readline()
	a=[int(x) for x in s1.split()]
d=0
for i in a:
	if i<0:
		d+=1


with open('bt1.out','w')as f2:
	f2.write(str(d))