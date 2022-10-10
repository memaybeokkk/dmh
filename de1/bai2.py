f2=open('bai2.out','w') 
with open('bai2.inp','r') as f1:
	k=f1.readline()
	for i in range(0,int(k)):

		s=f1.readline()
		n,x=[int(i) for i in s.split()]
		if n>x:
			f2.write('0')
			f2.write('\n')
		else:
			d=0
			for i in range(1,x//2+1):
				if n*i<=x:
					d+=1

		f2.write(str(d))
		f2.write('\n')
f2.close()