s=['2','20','004','66']
def qsp(s,l,h):
	i=l 
	j=h
	x=s[(i+j)//2]
	while i<=j:	
		while s[i]+x>x+s[i]:
			i+=1
		while s[j]+x<x+s[j]:
			j-=1
		if i<=j:
			temp=s[i]
			s[i]=s[j]
			s[j]=temp
			i+=1
			j-=1
		if j>l:
			qsp(s,l,j)
		if i<h:
			qsp(s,i,h)
qsp(s,0,len(s)-1)
print(s,s[::-1])