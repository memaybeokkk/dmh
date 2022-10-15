a=[3,5,1,7,9,0,9,-3,10]
min1=99999
min2=99999
max1=0
max2=0
max3=0
for i in a:
	if i>max1:
		temp1=max1
		temp2=max2
		max1=i 
		max2=temp1
		max3=temp2
	elif i>max2:
		temp=max2
		max2=i 
		max3=temp
	elif i>max3:
		max3=i 
	if i<min1:
		temp=min1
		min1=i 
		min2=temp
	elif i<min2:
		min2=i 
print(max(max1*max2*max3,max1*min1*min2))