"""
class Student:
    #атрибуты
    name= 'name'
    age= 0
    def add_Name(self, x):
        self.name=x
    def add_Age(self, x):
        self.age=x
    def display(self):
        print('Name: {} \nAge: {}'
              .format(self.name, self.age))
#объекты
newObject=Student()
newObject.add_Name(input('Name: '))
newObject.add_Age(input('Age: '))
newObject.display()
"""
"""
class Student2:
    name=school='name'
    age=0
    def __init__(self,x,y,c):
        self.name=x
        self.age=y
        self.school=c
    def display(self):
        print('Name: {} \nAge: {} \nSchool {}'
              .format(self.name,self.age,self.school))
newObject=Student2(input('Name: '), input('Age: '), input('School: '))
newObject.display()
"""
class Cars:
    car_Brand=car_Color='value'
    car_Year=car_Price=max_Speed=0
    def __init__(self,b,c,y,p,m):
        self.car_Brand=b
        self.car_Color=c
        self.car_Price=p
        self.car_Year=y
        self.max_Speed=m
    def display (self,d):
        self.display=d
        print('Brand {}: {}, Color: {}, Year: {}, Max speed: {} \nPrice: {} \n'
              .format(self.display,self.car_Brand,self.car_Color,self.car_Year,self.max_Speed,self.car_Price))
newCar1=Cars('Honda','Red',2003,2000,180)
newCar1.display(1)
newCar2=Cars('Subaru','Blue',1998,10000,240)
newCar2.display(2)