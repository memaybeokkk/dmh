for i in range(1000,9999):
    for j in range(0,4):
        i=str(i)
        I=i.replace(i[j],'')
        if int(I)==int(i)/9:
            print(i)
            break