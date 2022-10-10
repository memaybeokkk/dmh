s=[int(x) for x in input().split()]
a = s[0]
b= s[1]
c=s[2]
if a>b and a>c:
    print('AN')
elif b>c and b>a:
    print('VINH')
elif c>b and c>a:
    print('QUANG')
else:
    print('BAU LAI')