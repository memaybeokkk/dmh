s1='307uv5x1y08mnp'
s=''
for i in s1:
	if '0'<=i<='9':
		s+=i

nk=4
k=len(s)-nk
d=0
while True:
	vt=d 
	max='999'
	for i in range(d+1,d+k+1):
		if s[i]<max:
			max=s[i]
			vt=i 
	s=s[:d]+s[vt:]
	k=k-vt+d 
	d+=1
	print(s)
	if d==nk or k==0:
		break
if k>0:
	s=s[:d+1]
print(s)
