class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
class Employee(person):
    def __init__(self,name,age,empno,address):
        super().__init__(name,age)
        self.empno=empno
        self.address=address
    def display(self):
        super().display()
        print("empno:",self.empno)
        print("address:",self.address)
e1=Employee("sreeshna",16,111,"thrissur")
e1.display()
        
