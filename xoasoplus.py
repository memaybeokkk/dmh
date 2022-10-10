from math import sqrt
snt=[True]*100000
a=''
dem=0
n=5
k=4
for i in range(2,int(sqrt(100000)+1)):
	if snt[i]==True:
		a=a+str(i)
		dem+=1

		if dem==n:

			break
		for j in range(i,int(100000/i)):
			snt[i*j]=False
d=-1
print(a)
while True:
	d+=1
	max=a[d]
	vt=d
	for i in range(d+1,d+1+k):
		if a[i]>max:
			max=a[i]
			vt=i
	if d==0:
		a=a[vt:]
		print(a)
	else:
		a=a[:d]+a[vt:]
	k=k-vt+d
	if k==0 or d+1==len(a)-k:
		break
if k>0:
	a=a[:d]

print(a)