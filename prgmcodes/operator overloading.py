class A:
    def __init__(self,a):
        self.a=a
    def __add__(self,o):
        return self.a+o.a
obj1=A(1)
obj2=A(2)
print(obj1+obj2)
obj3=A("hello")
obj4=A("welcome")
print(obj3+obj4)
