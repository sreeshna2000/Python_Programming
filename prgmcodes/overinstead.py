list=int(input("enter the limit\n"))
i=0
list1=[]
while i<list:
    z=int(input("enter number"))
    if z>100:
        list1.append("over")
    else:
        list1.append(z)
    i=i+1
    print(list1)

