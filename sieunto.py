from math import sqrt


b=[7,2333,2334,4,58]
a=[True]*3000000
a[0]=a[1]=False
for i in range(2, int(sqrt(3000000)+1)):  
    if a[i]== True:
        for j in range(2,3000000//i):
            a[i*j]=False


def sieunto(x):

	global a
	kt=True
	while x>1:
		if not a[x]:
			kt=False
			break
		x=x//10
	return kt
for i in b:
	print(sieunto(i))



