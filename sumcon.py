s=input()
l=len(s)
a=[]
for i in range(l):
	for j in range(i,l):
		a.append(int(s[i:j+1]))
a=set(a)
print(sum(a),a)