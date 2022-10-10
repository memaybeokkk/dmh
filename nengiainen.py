def nen(s):
	t=''
	i=0
	while i<len(s)-1:
		d=1
		while i<len(s)-1 and s[i]==s[i+1]   :
			i+=1
			d+=1
		if d!=1:
			t+=str(d)+s[i]
		else:
			t+=s[i]
		i+=1
		if i==len(s)-1 and s[i]!=s[i-1]:
			t+=s[i]
	return t
def giainen(s):
	t=''
	i=0
	while i<=len(s)-1:
		if '2'<=s[i]<='9':
			t+=s[i+1]*int(s[i])
			i+=2
		else:
			t+=s[i]
			i+=1
	return t
print(nen('aaaabbcd'))
print(giainen('ab3cd2e'))