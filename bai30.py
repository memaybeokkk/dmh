a=1
b=10
s=''
for i in range(a,b+1):
	s+=str(i)
for i in range(0,11):
	print(s.count(i),end=' ')
d=[0]*10
for i in range(a,b+1):
	s=str(i)
	for i in s:
		d[int(i)]+=1
for i in range(10):
	print( d[i])