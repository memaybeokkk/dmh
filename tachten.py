a=[]
while True:
	i=int(input())
	
	if i==0:
		break
	a.append(i)
t=[0]*len(a)
max=0
for i in a:
	t[i]+=1
	if t[i]>max:
		max=t[i]
print(t[max]+1,max)
