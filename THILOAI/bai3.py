n=input()
dem=0
def tang(n):
	l=[]
	n=str(n)
	for i in n:
		l.append(int(i))
	for i in range(0, len(l)-1):
		for j in range(i + 1, len(l)):
			if (l[i]> l[j]):
				tmp = l[i]
				l[i] = l[j]
				l[j] = tmp
	if l[0]==0:
		l.pop(0)
	return int("".join([str(char) for char in l]))
def giam(n):
	n=str(n)
	l=[]
	for i in n:
		l.append(int(i))
	for i in range(0, len(l)-1):
		for j in range(i + 1, len(l)):
			if (l[i]< l[j]):
				tmp = l[i]
				l[i] = l[j]
				l[j] = tmp
	return int("".join([str(char) for char in l]))
while n!=0 and n!=6174:
	n=giam(n)-tang(n)
	dem+=1
print(dem)