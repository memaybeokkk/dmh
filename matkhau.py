from math import sqrt
s='nsivunsevunivne232432njnknj45435kjnbdjkb'
p=''
snt=[True]*100000
snt[0]=snt[1]=False
for i in range(2,int(sqrt(100000))):
	if snt[i]==True:
		for j in range(i,100000//i):
			snt[i*j]=False
for i in s:
	if '0'<=i<='9':    
		p+=i
max=0
for i in range(len(p)):
	for j in range(i,+5):
		if snt[int(p[i:j+1])]:
			if int(p[i:j+1])>max:
				max=int(p[i:j+1])
print(max)