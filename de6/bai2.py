a=int(input())
b=int(input())
c=int(input())
d=int(input())
tu=a*d+b*c
mau=b*d
def ucln(a,b):
	if a%b==0:
		return b
	return ucln(b,a%b)
u=ucln(tu,mau)
while u!=1:
	u=ucln(tu,mau)
	tu/=u
	mau/=u
print(int(tu),int(mau))