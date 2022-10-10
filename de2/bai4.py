f2=open('bai4,out','w')
with open('bai4.inp','r')as f1:
	n,m=[int(x) for x in f1.readline().split()]
	a=[int(x) for x in f1.readline().split()]
dmin=n
for i in range(n):
	d=0
	b=[0]*100000
	for j in range(i,n):
		
		if b[a[j]]==0:
			d+=1

			b[a[j]]=1
			if d==3: 
				if j-i+1<dmin:
					dmin=j-i+1
				break
f2.close()
print(dmin)