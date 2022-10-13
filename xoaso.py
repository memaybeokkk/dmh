s1='307uv5x1y08mnp'
s=''
for i in s1:
	if '0'<=i<='9':
		s+=i
print(s,len(s))
nk=4
k=len(s)-nk
d=0
while True:
	vt=d 
	max='0'
	for i in range(d,d+k+1):
		if s[i]>max:
			max=s[i]
			vt=i 
	print(s,vt)
	s=s[:d]+s[vt:]
	print(s)
	k=k-vt+d 
	d+=1
	if d==nk or k==0:
		break
if k>0:
	s=s[:d]
print(s)
