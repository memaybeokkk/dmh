f2=open('DACSAN.OUT','w')
with open('DACSAN.INP','r') as f1:
	s=f1.readline()
a,b,c=[int(x) for x in s.split()]
dem=0
while a>0 and b>0 and c>0:
	a-=1
	b-=1
	c-=1
	dem+=1

if a==0:
	while b>=3 or c>=3:
		b-=3
		c-=3
		if b<0 or c<0:
			dem+=1
		else:
			dem+=2

elif b==0:
	while a>=3 or c>=3:
		a-=3
		c-=3
		if b<0 or c<0:
			dem+=1
		else:
			dem+=2
elif c==0:
	while b>=3 or a>=3:
		b-=3
		a-=3
		if b<0 or c<0:
			dem+=1
		else:
			dem+=2
f2.write(str(dem))
f2.close()