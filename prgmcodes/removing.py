List = [11, 22, 31, 44, 51, 65, 71, 82, 91,88]
print("List Items = ",List)
for ev in List:
    if (ev % 2 == 0):
        List.remove(ev)
print("List Items after removing even Items = ",List)
