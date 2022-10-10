xa,ya=[int(x) for x in input().split()]
xc,yc=[int(x) for x in input().split()]
xm,ym=[int(x) for x in input().split()]
xn,yn=[int(x) for x in input().split()]

dem=0
if xa>xc and ya>yc:
	x1=xa
	y1=ya
	xa=xc
	ya=yc
	xc=x1
	yc=y1
elif xa>xc:
	x1=xa
	xa=xc
	xc=x1
elif ya>yc:
	y1=ya
	ya=yc
	yc=y1
if xa<xm<xc and ya<ym<yc:
	dem+=1
if xa<xn<xc and ya<yn<yc:
	dem+=1
print(dem)