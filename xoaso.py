s1='307uv5x1y08mnp'
s=''
for i in s1:
	if '0'<=i<='9':
		s+=i
s='35421'
nk=3
k=len(s)-nk
d=0
while True:
	vt=d 
	max=s[d]
	for i in range(d+1,d+k+1):
		if s[i]>max:
			max=s[i]
			vt=i 
	print(s,vt)
	s=s[:d]+s[vt:]
	k=k-vt+d 
	d+=1
	if d==nk or k==0:
		break
if k>0:
	s=s[:d]
print(s)
