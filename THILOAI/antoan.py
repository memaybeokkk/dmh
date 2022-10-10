s='Hgd4resFwefR82sdghtFJHBK0123456789abqwertyuiopasdfghjklzxcvbnmQƯERTYUIOPASDFGHJKLZXCVBNM FWHFBUIFBIQUWBFKWBQFIWUBFJKSB FWFIubbgwlfnuewibjkgbskdubgklbsjdbvuisyvguibegegwegbeijogehggewbguh8o3hf8oeg7hdvbkebguhfg8ohwg7iwguewhgoehgowhgudjgbuwih33qg8hiwiug3wigi3gwg3glnw3kngw3giuwbkdjgbwuigb3ui2093432r3f'
def antoan(s):
	s=set(s)
	d1=d2=d3=0
	for i in s:
		if 'a'<=i<='z':
			d1+=1
		elif 'A'<=i<='Z':
			d2+=1
		elif '0'<=i<='9':
			d3+=1
		if d1>=2 and d2>=2 and d3>=2:
			return 2
	if d1>=1 and d2>=1 and d3>=1:
		return 1
s2=	set(s)
d1=d2=d3=0
for i in s2:
	if 'a'<=i<='z':
		d1+=1
	elif 'A'<=i<='Z':
		d2+=1
	elif '0'<=i<='9':
		d3+=1
print(d2,d1,d3)
min1=min2=9999999
for i in range(len(s)-6):
	for j in range(i+5,len(s)):
		if antoan(s[i:j+1])==1 and j-i+1<min1:
			
			min1=j-i+1
			i1=i;j1=j 
		if antoan(s[i:j+1])==2 and j-i+1<min2:
			
			min2=j-i+1
			i2=i;j2=j 
print(s[i1:j1+1],2)
print(s[i2:j2+1],2)
print(len(s))