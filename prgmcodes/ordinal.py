string=input("enter a string:")
list=[]
for i in range(len(string)):
    ucode=ord(string[i])
    list.append(ucode)
print(list)
