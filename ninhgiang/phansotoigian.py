def ucln(a,b):
	if a%b==0:
		return b 
	return ucln(b,a%b)
n=20
dem=0
for i in range(1,20):
	if ucln(i,20)==1:
		dem+=1
print(dem)