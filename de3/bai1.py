a,b,c,d,e,f=[int(x) for x in input().split()]
if a/d== b/e == c/f:
	print('TRUNG NHAU')
elif a/d == c/f != b/e:
	print('')
elif a/d ==b/e != c/f:
	print('SONG SONG')