def Fibonacci_num(m): 
    u = 'a'
    v = 'b'
    for i in range(2,m): 
        c = v + u
        u = v
        v = c 
    return v
print(Fibonacci_num(6))