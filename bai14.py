n=input();vtd=vtc=[]
max=0
def doixung(s):
	s=str(s)
	for i in range(len(s)//2+1):
		if s[i]!= s[len(s)-1-i]:
			return False
	return True
for i in range(len(n)):
	for j in range(i,len(n)):
		if doixung(n[i:j+1]):
			if j-i+1>max:
				max=j-i+1
				vtd=[i]
				vtc=[j]
			elif j-i+1==max:
				vtd.append(i)
				vtc.append(j)
for i in range(len(vtd)):
	for j in range(vtd[i],vtc[i]+1):
		print(n[j],end='')
	print('\n')