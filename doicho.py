f1=open('doicho.inp','r')
n=f1.readline()
a=[]
b=[0]*int(n)
for i in range(int(n)):
	a.append(int(f1.readline()))
for i in range(len(a)):
	if (a[i]%2==0 and i%2!=0) or (a[i]%2!=0 and i%2==0):
	
		b[i]=True
	else:
		b[i]=False
f1.close()	
dem=0
for i in b:
	if i==False:
		dem+=1
if dem%2!=0:
	print(-1)
else:
	print(dem//2)
	d=0
	i=0
	while i<len(b):
		if b[i]==False:
			print(a[i],end=' ')
			i+=1
			while b[i]==True:
					i+=1
			print(a[i])
		i+=1
