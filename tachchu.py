s=input()
b=''
i=0
s+='3'
while i<len(s)-1:
	d=1
	while s[i]==s[i+1] and i<len(s)-1:
		d=d+1
		i+=1
		if i==len(s)-1:
			break
	b=b+str(d)+s[i]
	i+=1
print(b)