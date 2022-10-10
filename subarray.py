a=[1,2,1,2]
dem=0
def ktra(a):
	b=[0]*(max(a)+1)
	for i in a:
		b[i]+=1
		if b[i]==2:
			return True
	return False

for i in range(len(a)):
	kt=False
	for j in range(i+1,len(a)):
		if ktra(a[i:j+1]):
			dem+=1
print(dem)