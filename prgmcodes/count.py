i=str(input("enter the line"))
word=str(input("enter the word:"))
list=i.split()
count=0
for w in list:
    if w==word:
        count=count+1
print("number of",count)

