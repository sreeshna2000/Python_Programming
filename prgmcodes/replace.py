n=str(input("enter a sring with repeated string:"))
print("original  string is:",n)
k="$"
res=n[0]+n[1:].replace(n[0],k)
print(res)
