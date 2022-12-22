

def mul(a=1,b=1,c=1):
    return a*b*c
    
def sum(a=0,b=0,c=0):
    return a+b+c
#sum(1,2);

print(mul(3));

print(sum(4,3));

def multiply(*args):
    print(args)

multiply(1,2)