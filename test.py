a=[2,57547547652,63654746867854,4365487553,6586573447,4375698766554,4676967746,4767857,354754]
s=10
import itertools
for i in range(1,len(a)):
	b=list(itertools.combinations(a,i))
	for j in b:
		if sum(j)==s:
			print(j)