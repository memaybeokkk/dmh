h,m,s=[7,23,48]
s+=199
while s>=60:
	m+=1
	s-=60
	if m>=60:
		h+=1
		m-=60
print(h,m,s)