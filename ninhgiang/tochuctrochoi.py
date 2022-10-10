s='bggbgbgbgbgbgbgbgbgbggbgbgbgbgbgbgbgbgbgb'
i=0
dem=0
d=0
while i<len(s)-1:
	if s[i]!=s[i+1]:
		dem+=1
		i+=1
	i+=1
s=s[-1]+s 
s=s[:len(s)-1]
i=0
while i<len(s)-1:
	if s[i]!=s[i+1]:
		d+=1
		i+=1
	i+=1
print(max(d,dem))