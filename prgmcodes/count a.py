list=["anu","aleena","manu","ammu"]
count=0
print(list)
a=input("enter the letter\n")
for n in list:
    for f in n:
        if f==a:
            count=count+1
print("number of",a,"is",count)
