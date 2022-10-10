n=int(input())
fb=[1,1]
for i in range (0,n):
	
	if (fb[i]+fb[i+1])>n:
		break
	fb.append(fb[i]+fb[i+1])
a=[]
i=0
fb=fb[::-1]
fb.append(0)
def pt(n):
	global i,a
	if n-fb[i]<0:
		i+=1
		pt(n)
	else:
		a.append(fb[i])
		n-=fb[i]
		i+=1
		if n==0:
			print(a)
		pt(n)
		
	
print(pt(n))