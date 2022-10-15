t=2
n=[5,7]
def tpnp(x):
    a=''
    while x>0:
        a+=str(x%2)
        x//=2
    return a[::-1]
# vd vs n=5
n=15
i=1
dem=1
while len(tpnp(i))<=n:
    a=tpnp(i%1000000007)
    if a.find('111')==-1:
        dem+=1

    i+=1
print(dem)
