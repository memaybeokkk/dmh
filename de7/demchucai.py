s=input()
s=s.lower()
s=''.join(s.split())
d=[0]*150
for i in s:
	d[ord(i)]+=1
for i in range(97,123):
	if d[i]!=0:
		print(chr(i),d[i])