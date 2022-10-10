from math import sqrt
a,b,c=[int(x) for x in input('nhap he so a b c: ').split()]
if a==0:
    if b!=0:
        print('nghiem cua pt la: ',-c/b)
    else:
        if c==0:
            print('pt vo so nghiem')
        else:
            print('pt vo nghiem')
else:
    d=b**2-4*a*c
    print(d)
    if d<0:
        print('pt vo nghiem')
    elif d ==0:
        print('pt co nghiem kep: ',-b/(2*a))
    else:
        print('pt co 2 nghiem x1: ',(-b-sqrt(d))/(2*a),',x2: ',(-b+sqrt(d))/(2*a))
