#in list we dont use *args instead we use args
def input (args):
    positiveList=[]
    print(args)
    for i in args:
      if i>0:
        positiveList.append(i)
        
    return positiveList
    

print(input([-2,-1,0,1,2,3]))

