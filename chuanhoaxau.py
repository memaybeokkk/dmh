f1=open('inp','r',encoding='utf')
def chuanhoa(s):
    dau=['.',',','?','!',';']
    while '  ' in s:
        s=s.replace('  ',' ')
    for i in dau:
        s=s.replace(' '+i+' ',i+' ')
        s=s.replace(' '+i,i+' ')
    s=s.replace('( ','(')
    s=s.replace(' )',')')
    return s  
for i in f1:
    print(chuanhoa(i))
f1.close() 