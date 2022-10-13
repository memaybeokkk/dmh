a=[chr(i) for i in range(ord('a'),ord('z')+1)]
A=[chr(i) for i in range(ord('A'),ord('Z')+1)]
s='HEAL THE WORLD'
s1=''
for i in s:
    
    if i!=' ':

        if i in A:
            s1+=  A[(A.index(i)+5)%26]
        else:
            s1+= a[(a.index(i)+5)%26]
    else :
        s1+=' '
print(s1)