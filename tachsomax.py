s1=input()
s=''
for i in s1:
	if '0'<=i<='9':
		s+=i 
d=0
print(s)
k=len(s)-5
while d<5 and k!=0:
	max=s[d]
	vt=d 
	for i in range(d+1,d+k+1):
		if s[i]>max:
			max=s[i]
			vt=i 
	s=s[:d]+s[vt:]
	k=k-vt+d 
	d+=1
if k>0:
	s=s[:d]
print(s)