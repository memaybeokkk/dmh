'''
so=2
n=2
d=1
while d<13:
	dem=0
	while True:
		if n%so==0:
			dem+=1
			d+=1
			if d==13:
				print(n)
				break
			if dem==so:
				break
		n+=1
	n+=1
	so+=1
'''
S=0
f2=open('test.out','w')
with open('test.inp','r') as f1:
	s=[int(x) for x in f1.readline().split()]
	n=s[0];k=s[1];j=s[2]
	a=[0]

	for i in f1:
		a.append(int(i.rstrip('\n')))
	j=j%5
	while k!=0:
		S+=a[j]
		k-=1
		j+=1
		if j>n:
			j=1

print(S)