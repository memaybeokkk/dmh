s='hhhoooccccssssinnnhh'
i=0
t=''
while i<len(s)-1:
	while i<len(s)-1 and s[i]==s[i+1]   :
		i+=1
	t+=s[i]
	i+=1
	if i==len(s)-1 and s[i]!=s[i-1]:
		t+=s[i]
print(t)