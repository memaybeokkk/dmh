def tpnp(x):
    a=''
    while x>0:
        a+=str(x%2)
        x=x//2
    return a[::-1]
def nptp(x):
    s=0
    for i in x:
        s=s*2+int(i)
    print(s)

def tphx(x):
    a=''
    while x>0:
        du=x%16 
        if du==10:
            a+='A'
        elif du==11:
            a+='B'
        elif du==12:
            a+='C'
        elif du==13:
            a+='D'
        elif du==14:
            a+='E'
        elif du==15:
            a+='F'
        else:
            a+=str(du)
        x=x//16
    return a[::-1]
print(tphx(int(input())))


    
