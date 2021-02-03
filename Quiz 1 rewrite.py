def fib(n):
    
    F0=0
    F1=1
    
    if n==1:
        print(F0)
    
    else:
        print(F0)
        print(F1)
    
        for i in range(2,n):
            F2=F0+F1
            F0=F1
            F1=F2
            print(F2)
    
fib(10)