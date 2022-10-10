n=int(input())
s=[int(x) for x in input().split()]
s=s[0:n]
d=[0]*10000000
max=0
dem=0
for i in s:
	d[i]+=1
	if d[i]>dem:
		dem=d[i]
		max=i
	elif d[i]==dem:
		if i<max:
			max=i
print(max,dem)