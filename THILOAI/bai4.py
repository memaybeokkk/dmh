from math import sqrt


m=int(input())
a=[True]*30000
a[0]=a[1]=False
for i in range(2, int(sqrt(30000)+1)):  
    if a[i]== True:
        for j in range(2,30000//i):
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

print(sieunto(m))