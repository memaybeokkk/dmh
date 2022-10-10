from math import sqrt
xa,ya=[int(x) for x in input().split()]
xb,yb=[int(x) for x in input().split()]
xc,yc=[int(x) for x in input().split()]
xd,yd=[int(x) for x in input().split()]
def dientich(xa,xb,xc,ya,yb,yc):
	ab=sqrt((xa-xb)**2+(ya-yb)**2)
	bc=sqrt((xc-xb)**2+(yc-yb)**2)
	ac=sqrt((xa-xc)**2+(ya-yc)**2)
	p=(ab+bc+ac)/2
	s=sqrt(p*(p-ab)*(p-ac)*(p-bc))
	return s
if  dientich(xa,xb,xd,ya,yb,yd)+ dientich(xa,xc,xd,ya,yc,yd)+ dientich(xb,xc,xd,yb,yc,yd)>dientich(xa,xb,xc,ya,yb,yc):
	print(0)
else:
	print(1)