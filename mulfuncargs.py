def product(*args):
    mul=1
    sum=0
    if len(args)<3:
        for i in args:
            mul=mul*i
            print(mul)
            
    if len(args)>=3:
        for i in args:
            sum=sum+i
            print(sum)


product(2,4)
product(2,3,4)



