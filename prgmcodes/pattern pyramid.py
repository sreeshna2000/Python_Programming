s = int(input("Please enter the number of rows : "))  
for i in range(0, s):  
    for j in range(0, i + 1):  
        print("*", end=' ')  
    print(" ")  
for i in range(s + 1, 0, -1):  
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ")  
