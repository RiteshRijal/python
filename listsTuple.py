a=[1,2,3,4]
m=[[1,2],[3,4]]
a[0]
a[-1]
list =[0]*5
print(list)

list=[1,2]+[3,4]
print(list)

a, *rest=list
print(list)
print(a)

b,*rest,val=list
print(rest)
print(val)

list1=[1,2,3]
print(type(list1))

list2=1,2,3
print(type(list2))

tuple=(1,2,3)
print(type(tuple))