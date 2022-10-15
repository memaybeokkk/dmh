f2=open('ggmap.out','w')
f1=open('ggmap.inp','r')
n=int(f1.readline())+1
max=999999
c=[[max]*n]

for i in f1:
	c.append([max]+[int(x) for x in i.split()])
import itertools
def SUM(i):
	return c[i[0]][i[1]]+c[i[1]][i[2]]+c[i[2]][i[3]]+c[i[3]][i[4]]+c[i[4]][i[0]]
d=list(itertools.permutations([2,3,4,5]))
b=[]
for i in d:
	b.append([1]+list(i))
dmin=max
min='a'
for i in b:
	if SUM(i)<dmin:
		dmin=SUM(i)
		min=' '.join(str(x) for x in i)
print(min)