class A:
    def __init__(self,a):
        self.a=a
    def __gt__(self,other):
        if(self.a>other.a):
            return True
        else:
            return False
obj1=A(2)
obj2=A(3)
if(obj1>obj2):
    print('obj1 is greater than obj2')
else:
    print('obj2 is greater than obj1')
