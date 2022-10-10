a=int(input())
b=int(input())
def ucln(a,b):
    if a%b==0:
        return b
    return ucln(b,a%b)
    
print(ucln(a,b))


