from math import sqrt
snt=[True]*1000002
snt[0]=snt[1]=False
for i in range(2,int(sqrt(1000002))+1):
	if snt[i]==True:
		for j in range(2,1000002//i):
			snt[i*j]=False
'''def ptich(n):
	dem=0
	for i in range(2,n+1):
		if snt[i]==True:
			while n%i==0:
				dem+=1
				n/=i
	return dem
n=9
dmax=max=0
for i in range(9,-1,-1):

	if ptich(i)>dmax:
		dmax=ptich(i)
		max=i

print(max)'''
n=300

b=[0]*(n+1)
t=''
for i in range(2,n+1):
	if snt[i]==True:
		while n%i==0:
			b[i]+=1
			n/=i
	if b[i]!=0:
		if b[i]!=1:
			t=t+str(i)+'^'+str(b[i])+'.'
		else:
			t=t+str(i)+'.'


print(t.rstrip('.'))



