s1=input()
s2=input()
vtd=vtc=[]
max=0
if len(s1)<=len(s2):
	n=len(s1)
else:
	n=len(s2)
for i in range(n):
	for j in range(i,n):
		if s1[i:j+1] in s2:
			if j-i+1>max:
				max=j-i+1
				vtd=[i]
				vtc=[j]
			elif j-i+1==max:
				vtd.append(i)
				vtc.append(j)
for i in range(len(vtd)):
	for j in range(vtd[i],vtc[i]+1):
		print(s1[j],end='')