n=int(input())
maxx=maxy=0
minx=miny=9999999999999999999999
for i in range(n):
	x,y,r=[int(x) for x in input().split()]
	if x+r>maxx:
		maxx=x+r+5
	if y+r>maxy:
		maxy=y+r+5
	if x-r<minx:
		minx=x-r-5
	if y-r<miny:
		miny=y-r-5
print(minx,maxy)
print(maxx,miny)