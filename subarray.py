a=[1,2,1,2]
dem=0

for i in range(len(a)):
	b=[0]*1000000000
	for j in range(i,len(a)):
		b[j]+=1
		if b[j]==2:
			dem+=1
print(dem)