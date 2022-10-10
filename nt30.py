f2=open('bt30.out','w')
with open('bt30.inp','r') as f1:
	for i in f1:
		c=[int(x) for x in i.split()]
		d=[0]*10
		if c[0]==c[1]==0:
			break
		for i in range(c[0],c[1]+1):
			s=str(i)
			for i in s:
				d[int(i)]+=1
		for i in range(9):
			f2.write(str(d[i])+' ')
		f2.write('\n')
f2.close()
