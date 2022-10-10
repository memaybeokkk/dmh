s1=input()
s2=input()

def ae(a,b):
	kt=True
	for i in a:
		if b.count(i)==0:
			kt=False
			return kt
	for i in b:
		if a.count(i)==0:
			kt=False
			return kt
	return kt
if ae(s1,s2)==True:
	print('YES')
else:
	print('NO')
