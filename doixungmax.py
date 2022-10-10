a='112103451543878'
max=0
def doixung(i,j):
	s=a[i:j+1] 
	for i in range(len(s)//2+1):
		if s[i]!= s[len(s)-1-i]:
			return False
	return True
n=len(a)
for i in range(n):
	for j in range(i,n):
		if doixung(i,j):
			if len(a[i:j+1])>max:
				max=len(a[i:j+1])
				vtd=i 
				vtc=j

print(max,a[vtd:vtc+1])