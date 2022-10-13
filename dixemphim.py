a=[1,0,0,0,0,0,1,0,0,0,0,1]
a=[1]+a+[1]
i=1
dem=0
min=9999999
while i<len(a):
	if a[i]==0:	
		dem=0
		while a[i]==0:
			dem+=1
			i+=1
		if dem<min:
			min=dem
		

	i+=1
print(min)