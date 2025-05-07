Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.



# user (vin volume body_type)
class Car:
    def __init__(self, vin, volume, body_type):
        self.vin = vin
        self.volume = volume
        self.body_type = body_type
    def __repr__(self):
        return f"Car({self.vin}, {self.volume}, {self.body_type})"

    
lada1 = Car("12312474", 1.67, "hatchback")
lada1
Car(12312474, 1.67, hatchback)
lada1.__dict__
{'vin': '12312474', 'volume': 1.67, 'body_type': 'hatchback'}
di = lada1.__dict++
SyntaxError: invalid syntax
di = lada1.__dict__
di
{'vin': '12312474', 'volume': 1.67, 'body_type': 'hatchback'}
lada2 = Car("1231596859", 1.95, "sedan")
lada2
Car(1231596859, 1.95, sedan)
li = [lada1, lada2]
for car_inst in li:
    print(car_inst.vin)
    print(car_inst.volume)
    print(car_inst.body_type)

    
12312474
1.67
hatchback
1231596859
1.95
sedan
for car_inst in li:
    print()
    for k, v in car_inst.__dict__.items():
        print(k, ":", v)

        

vin : 12312474
volume : 1.67
body_type : hatchback

vin : 1231596859
volume : 1.95
body_type : sedan




class Car:
    def __init__(pun, vin, volume, body_type):
        pun.vin = vin
        pun.volume = volume
        pun.body_type = body_type
    def __repr__(pun):
        return f"Car({pun.vin}, {pun.volume}, {pun.body_type})"

    
lada2
Car(1231596859, 1.95, sedan)
lada3 = Car("34647", 3, "punk")
lada3
Car(34647, 3, punk)
lada3.body_type = "coupe"
lada3
Car(34647, 3, coupe)
lada3.new_var = 131226346
lada3
Car(34647, 3, coupe)
lada3.__dict__
{'vin': '34647', 'volume': 3, 'body_type': 'coupe', 'new_var': 131226346}
Car.__dict__
mappingproxy({'__module__': '__main__', '__firstlineno__': 1, '__init__': <function Car.__init__ at 0x0000018239B5B9C0>, '__repr__': <function Car.__repr__ at 0x0000018239B5BA60>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None})
Car.__bases__
(<class 'object'>,)
class S:
    pass

fg = S()

class Car:
    def __init__(pun, vin, volume, body_type):
        pun.vin = vin
        pun.volume = volume
        pun.body_type = body_type
    def __repr__(pun):
        return f"Car({pun.vin}, {pun.volume}, {pun.body_type})"
    def move(self):
        print("move")
    def turn(self, direction):
        print("turn", direction)
    def stop(self):
        print("stop")

        
class SportCar(Car):
    def __init__(self):
        super().__init__(vin, volume, body_type, speed_limit=270, max_speed=300)
        self.speed_limit = speed_limit
        self.max_speed = max_speed
    def __repr__(self):
        super().__repr__()
        return f"SportCar({self.speed_limit}, {self.max_speed}, {self.body_type})"
    def race(self):
        print(f"race with {self.max_speed} km/h")

        
renault = SportCar("1214263", 3.5, "coupe")
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    renault = SportCar("1214263", 3.5, "coupe")
TypeError: SportCar.__init__() takes 1 positional argument but 4 were given

class Car:
    def __init__(self, vin, volume, body_type):
        self.vin = vin
        self.volume = volume
        self.body_type = body_type
    def __repr__(self):
        return f"Car({self.vin}, {self.volume}, {self.body_type})"
    def move(self):
        print("move")
    def turn(self, direction):
        print("turn", direction)
    def stop(self):
        print("stop")

        
class SportCar(Car):
    def __init__(self):
        super().__init__(vin, volume, body_type, speed_limit=270, max_speed=300)
        self.speed_limit = speed_limit
        self.max_speed = max_speed
    def __repr__(self):
        super().__repr__()
        return f"SportCar({self.speed_limit}, {self.max_speed}, {self.body_type})"
    def race(self):
        print(f"race with {self.max_speed} km/h")

        
renault = SportCar("1214263", 3.5, "coupe")
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    renault = SportCar("1214263", 3.5, "coupe")
TypeError: SportCar.__init__() takes 1 positional argument but 4 were given


class Stack:
    def__init__(self):
        self.__stack = []
        
SyntaxError: invalid syntax
class Stack:
    def__init__(self):
        self.__stack = []
        
SyntaxError: invalid syntax
class Stack:
    def __init__(self):
        self.__stack = []
    def push(self, value):
        self.__stack.append(value)
        print(value, "good")
    def pop(self):
        print(self.__stack.pop(), "gooood")

        
s1 = Stack()
4
s1
<__main__.Stack object at 0x0000018239A46BA0>
s1 = Stack()
class Stack:
    def __init__(self):
        self.__stack = []
        print("stack created")
    def push(self, value):
        self.__stack.append(value)
        print(value, "good")
    def pop(self):
        print(self.__stack.pop(), "gooood")

        
s1 = Stack()
stack created4
s1.pop()
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    s1.pop()
  File "<pyshell#91>", line 9, in pop
    print(self.__stack.pop(), "gooood")
IndexError: pop from empty list

class Stack:
    def __init__(self):
        self.__stack = []
        print("stack created")
    def push(self, value):
        self.__stack.append(value)
        print(value, "good")
    def pop(self):
        print(self.__stack.pop(), "gooood")
    def state(self)
    
SyntaxError: expected ':'

class Stack:
    def __init__(self):
        self.__stack = []
        print("stack created")
    def push(self, value):
        self.__stack.append(value)
        print(value, "good")
    def pop(self):
        try:
            print(self.__stack.pop(), "gooood")
        except:
            print("pusto")
    def state(self):
        print("now")
        print(self.__stack)

        
sq = Stack()
stack created
s1.state()
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    s1.state()
AttributeError: 'Stack' object has no attribute 'state'
sq.state()
now
[]
sq.pop()
pusto


class Stack:
    def __init__(self):
...         self.__stack = []
...         print("stack created")
...     def push(self, value):
...         self.__stack.append(value)
...         print(value, "good")
...     def pop(self):
...         try:
...             print(self.__stack.pop(), "gooood")
...         except:
...             print("pusto")
...     def state(self):
...         print("now")
...         print(self.__stack)
... 
...         
>>> class AddStackValues(Stack):
...     def __init__(self):
...         super().__init__()
...         self.__summa = 0
...     def push(self, value):
...         super().push(value)
...         self.__summa += value
...     def get_summa(self):
...         print(self.__summa)
... 
...         
>>> s2 = AddStackValues()
stack created
>>> s2.get_summa()
0
>>> s2.state()
now
[]
>>> s2.push(3)
3 good
>>> s2.state()
now
[3]
>>> s2.push(78)
78 good
>>> s2.state()
now
[3, 78]
>>> s2.get_summa()
81
>>> 
