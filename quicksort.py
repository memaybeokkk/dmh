def quicksort(a,l,h):
	i=l
	j=h
	x=a[(i+j)//2]
	while i<=j:
		while a[i]<x:
			i+=1
		while a[j]>x:
			j-=1
		if i<=j:
			temp=a[i]
			a[i]=a[j]
			a[j]=temp
			i+=1
			j-=1
		if j>l:
			quicksort(a,l,j)
		if i<h:
			quicksort(a,i,h)
a=[1,2,6,9,3,13,25,13]
quicksort(a,0,len(a)-1)
print(a)