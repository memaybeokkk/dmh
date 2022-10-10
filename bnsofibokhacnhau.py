s=[int(x) for x in input().split()]
a=[1,1]
d=[0]*1000000
dem=0



for i in range (0,1000000):
	fb=a[i]+a[i+1]
	a.append(fb)
	if a[i+1]>= max(s) :
		break

print(a)
for i in a:
	if s.count(i)!=0 and d[i]==0:
		dem+=1
		d[i]=1
print(dem)