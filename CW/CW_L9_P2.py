Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
class Client:
    def __init__(self, name, phone, email=None):
        self.name = name
        self.phone = phone
        self.email = email

        
for i in range (1, n+1)
SyntaxError: expected ':'
for i in range (1, n+1):
    print("client number is:", i)
    name = input("name:")
    phone = input("phone:")
    email = input("email:")
    client = Client(name, phone, email)
    cient_storage.append(client)

    
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    for i in range (1, n+1):
NameError: name 'n' is not defined

n = 4
for i in range (1, n+1):
    print("client number is:", i)
    name = input("name:")
    phone = input("phone:")
    email = input("email:")
    client = Client(name, phone, email)
    cient_storage.append(client)
    
SyntaxError: multiple statements found while compiling a single statement
n = 10
client.storage = []
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    client.storage = []
NameError: name 'client' is not defined. Did you mean: 'Client'?


class Client:
    def __init__(self, name, phone, email=None):
        self.name = name
        self.phone = phone
        self.email = email

        
client_storage = []

n = int(input("How much?:"))
How much?:1

for i in range (1, n+1):
    print("client number is:", i)
    name = input("name:")
    phone = input("phone:")
    email = input("email:")
    client = Client(name, phone, email)
    cient_storage.append(client)

    
client number is: 1
name:sdf
phone:sfsf
email:sfdf
Traceback (most recent call last):
  File "<pyshell#28>", line 7, in <module>
    cient_storage.append(client)
NameError: name 'cient_storage' is not defined. Did you mean: 'client_storage'?


class Client:
    class_variable = 0
    def __init__(self, name, phone, email=None):
        self.name = name
        self.phone = phone
        self.email = email

        

Client.class_variable
0

    class_variable = 0
    def __init__(self, name, phone, email=None):
        self.name = name
        self.phone = phone
        self.email = email
        
SyntaxError: unexpected indent
    class_variable = 0
    def __init__(self, name, phone, email=None):
        self.name = name
        self.phone = phone
        self.email = email

SyntaxError: unexpected indent
class Client:
    class_variable = 0
    def __init__(self, name, phone, email=None):
        self.name = name
        self.phone = phone
        self.email = email

        
client1 = Client("cl", 1)
client1
<__main__.Client object at 0x0000020C7BAB6900>
client1.name = "Pun"
client1
<__main__.Client object at 0x0000020C7BAB6900>
client1 = Client("fdfd", 133, "sgsg")
client1.name = "fff"
client1
<__main__.Client object at 0x0000020C7BAABC50>


class Task:
    counter = 1
    def __init__(self, name):
        self.task_id - Task.counter
        Task.counter += 1
        self.task_name = name
        self.task_status = False

        
t1 = Task("go")
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    t1 = Task("go")
  File "<pyshell#56>", line 4, in __init__
    self.task_id - Task.counter
AttributeError: 'Task' object has no attribute 'task_id'
class Task:
    counter = 1
    def __init__(self, name):
        self.task_id = Task.counter
        Task.counter += 1
        self.task_name = name
        self.task_status = False

        
t1 = Task("go")
t2 = Task("Run")
t3 = Task("sleep")
print(t1.task_id, t1.task_name, t1.task_status)
1 go False

Task.__dict__
mappingproxy({'__module__': '__main__', '__firstlineno__': 1, 'counter': 4, '__init__': <function Task.__init__ at 0x0000020C7BF9ACA0>, '__static_attributes__': ('task_id', 'task_name', 'task_status'), '__dict__': <attribute '__dict__' of 'Task' objects>, '__weakref__': <attribute '__weakref__' of 'Task' objects>, '__doc__': None})
t1.__dict__
{'task_id': 1, 'task_name': 'go', 'task_status': False}


class f:
    """sdsdgjsdgkhsdk"""
    a = 9
    def __init__(self):
        pass

    
f.__dict__
mappingproxy({'__module__': '__main__', '__firstlineno__': 1, '__doc__': 'sdsdgjsdgkhsdk', 'a': 9, '__init__': <function f.__init__ at 0x0000020C7BF9A480>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'f' objects>, '__weakref__': <attribute '__weakref__' of 'f' objects>})
help(f)
Help on class f in module __main__:

class f(builtins.object)
 |  sdsdgjsdgkhsdk
 |
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  a = 9


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"Hello! My name is {self.name} and I'm {self.age} old")

        
Cat.hello()
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    Cat.hello()
TypeError: Cat.hello() missing 1 required positional argument: 'self'
barsik = Cat("Barsik", 3)
barsik.hello()
Hello! My name is Barsik and I'm 3 old
barsik.age
3
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"Hello! My name is {self.name} and I'm {self.age} old")
    def say(self,msg):
        print(f"{self.name} says: {msg}!")

        
barsik.say("Meow")
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    barsik.say("Meow")
AttributeError: 'Cat' object has no attribute 'say'
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"Hello! My name is {self.name} and I'm {self.age} old")
    def say(self, msg):
        print(f"{self.name} says: {msg}!")

        
barsik.hello()
Hello! My name is Barsik and I'm 3 old
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"Hello! My name is {self.name} and I'm {self.age} old")
    def grow(self):
        self.age += 1

        
barsik = Cat("barsik", 3)
barsik.grow()

barsik.hello
<bound method Cat.hello of <__main__.Cat object at 0x0000020C7BAB6CF0>>
barsik.hello()
Hello! My name is barsik and I'm 4 old
print(barsik)
<__main__.Cat object at 0x0000020C7BAB6CF0>


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"Hello! My name is {self.name} and I'm {self.age} old")
    def grow(self):
        self.age += 1
    def __repr__(self):
        return f"cat info.\nname:{self.name} \nage{self.age}
    
SyntaxError: unterminated f-string literal (detected at line 10)
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"Hello! My name is {self.name} and I'm {self.age} old")
    def grow(self):
        self.age += 1
    def __repr__(self):
        return f"cat info.\nname:{self.name} \nage{self.age}"

    
barsik = Cat("barsik", 3)
barsik
cat info.
name:barsik 
age3
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"Hello! My name is {self.name} and I'm {self.age} old")
    def grow(self):
        self.age += 1
    def __repr__(self):
        return f"cat info.\nname:{self.name} \nage{self.age}"
    def __str__(self):
        return f"{self.name}  |  {self.age}"

    
print(barsik)
cat info.
name:barsik 
age3
barsik
cat info.
name:barsik 
age3
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"Hello! My name is {self.name} and I'm {self.age} old")
    def grow(self):
        self.age += 1
    def __repr__(self):
        return f"cat info.\nname:{self.name} \nage{self.age}"
    def __str__(self):
        return f"{self.name}  |  {self.age}"

    
barsik = Cat("barsik", 3)
barsik
cat info.
name:barsik 
age3
print(barsik)
barsik  |  3


help(Cat)
Help on class Cat in module __main__:

class Cat(builtins.object)
 |  Cat(name, age)
 |
 |  Methods defined here:
 |
 |  __init__(self, name, age)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __repr__(self)
 |      Return repr(self).
 |
 |  __str__(self)
 |      Return str(self).
 |
 |  grow(self)
 |
 |  hello(self)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object

help(int)
Help on class int in module builtins:

class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
 |
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating-point
 |  numbers, this truncates towards zero.
 |
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |
 |  Built-in subclasses:
 |      bool
 |
 |  Methods defined here:
 |
 |  __abs__(self, /)
 |      abs(self)
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __and__(self, value, /)
 |      Return self&value.
 |
 |  __bool__(self, /)
 |      True if self else False
 |
 |  __ceil__(self, /)
 |      Ceiling of an Integral returns itself.
 |
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __float__(self, /)
 |      float(self)
 |
 |  __floor__(self, /)
 |      Flooring an Integral returns itself.
 |
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |
 |  __format__(self, format_spec, /)
 |      Convert to a string according to format_spec.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __getnewargs__(self, /)
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __hash__(self, /)
 |      Return hash(self).
 |
 |  __index__(self, /)
 |      Return self converted to an integer, if self is suitable for use as an index into a list.
 |
 |  __int__(self, /)
 |      int(self)
 |
 |  __invert__(self, /)
 |      ~self
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __lshift__(self, value, /)
 |      Return self<<value.
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __mod__(self, value, /)
 |      Return self%value.
 |
 |  __mul__(self, value, /)
 |      Return self*value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __neg__(self, /)
 |      -self
 |
 |  __or__(self, value, /)
 |      Return self|value.
 |
 |  __pos__(self, /)
 |      +self
 |
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |
 |  __radd__(self, value, /)
 |      Return value+self.
 |
 |  __rand__(self, value, /)
 |      Return value&self.
 |
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |
 |  __rlshift__(self, value, /)
 |      Return value<<self.
 |
 |  __rmod__(self, value, /)
 |      Return value%self.
 |
 |  __rmul__(self, value, /)
 |      Return value*self.
 |
 |  __ror__(self, value, /)
 |      Return value|self.
 |
 |  __round__(self, ndigits=<unrepresentable>, /)
 |      Rounding an Integral returns itself.
 |
 |      Rounding with an ndigits argument also returns an integer.
 |
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |
 |  __rrshift__(self, value, /)
 |      Return value>>self.
 |
 |  __rshift__(self, value, /)
 |      Return self>>value.
 |
 |  __rsub__(self, value, /)
 |      Return value-self.
 |
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |
 |  __rxor__(self, value, /)
 |      Return value^self.
 |
 |  __sizeof__(self, /)
 |      Returns size in memory, in bytes.
 |
 |  __sub__(self, value, /)
 |      Return self-value.
 |
 |  __truediv__(self, value, /)
 |      Return self/value.
 |
 |  __trunc__(self, /)
 |      Truncating an Integral returns itself.
 |
 |  __xor__(self, value, /)
 |      Return self^value.
 |
 |  as_integer_ratio(self, /)
 |      Return a pair of integers, whose ratio is equal to the original int.
 |
 |      The ratio is in lowest terms and has a positive denominator.
 |
 |      >>> (10).as_integer_ratio()
 |      (10, 1)
 |      >>> (-10).as_integer_ratio()
 |      (-10, 1)
 |      >>> (0).as_integer_ratio()
 |      (0, 1)
 |
 |  bit_count(self, /)
 |      Number of ones in the binary representation of the absolute value of self.
 |
 |      Also known as the population count.
 |
 |      >>> bin(13)
 |      '0b1101'
 |      >>> (13).bit_count()
 |      3
 |
 |  bit_length(self, /)
 |      Number of bits necessary to represent self in binary.
 |
 |      >>> bin(37)
 |      '0b100101'
 |      >>> (37).bit_length()
 |      6
 |
 |  conjugate(self, /)
 |      Returns self, the complex conjugate of any int.
 |
 |  is_integer(self, /)
 |      Returns True. Exists for duck type compatibility with float.is_integer.
 |
 |  to_bytes(self, /, length=1, byteorder='big', *, signed=False)
 |      Return an array of bytes representing an integer.
 |
 |      length
 |        Length of bytes object to use.  An OverflowError is raised if the
 |        integer is not representable with the given number of bytes.  Default
 |        is length 1.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        sys.byteorder as the byte order value.  Default is to use 'big'.
 |      signed
 |        Determines whether two's complement is used to represent the integer.
 |        If signed is False and a negative integer is given, an OverflowError
 |        is raised.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  from_bytes(bytes, byteorder='big', *, signed=False)
 |      Return the integer represented by the given array of bytes.
 |
 |      bytes
 |        Holds the array of bytes to convert.  The argument must either
 |        support the buffer protocol or be an iterable object producing bytes.
 |        Bytes and bytearray are examples of built-in objects that support the
 |        buffer protocol.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        sys.byteorder as the byte order value.  Default is to use 'big'.
 |      signed
 |        Indicates whether two's complement is used to represent the integer.
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  denominator
 |      the denominator of a rational number in lowest terms
 |
 |  imag
 |      the imaginary part of a complex number
 |
 |  numerator
 |      the numerator of a rational number in lowest terms
 |
 |  real
 |      the real part of a complex number

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"Hello! My name is {self.name} and I'm {self.age} old")
    def grow(self):
        self.age += 1
    def __repr__(self):
        return f"cat info.\nname:{self.name} \nage{self.age}"
    def __str__(self):
        return f"{self.name}  |  {self.age}"

    
class DoG:
    pass
DoG.__bases
SyntaxError: invalid syntax
DoG.__bases__
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    DoG.__bases__
NameError: name 'DoG' is not defined
class Dog:
    pass

Dog.__bases__
(<class 'object'>,)

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"Hello! My name is {self.name} and I'm {self.age} old")
    def grow(self):
        self.age += 1
    def __repr__(self):
        return f"cat info.\nname:{self.name} \nage{self.age}"
    def __str__(self):
        return f"{self.name}  |  {self.age}"

    
class SwimmingCat(Cat):
    def swim(self):
        print("I can swim")

        
sadik = SwimmingCat("sadik", 2)
sadik
cat info.
name:sadik 
age2
print(sadik)
sadik  |  2
sadik.swim()
I can swim
type(sadik)
<class '__main__.SwimmingCat'>
sadik.grow()
sadik.hello()
Hello! My name is sadik and I'm 3 old

class SwimmingCat(Cat):
    def swim(self):
        print("I can swim")
    def __str__(self):
        return f"SwimmingCat:{self.name}  |  {self.age}"

    
sadik = SwimmingCat("sadik", 2)
print(sadik)
SwimmingCat:sadik  |  2

class SwimmingCat(Cat):
    def __init__(self, name, age, color):
        super().__init__(name,age)
        self.color = color
    def swim(self):
        print("I can swim")
    def __str__(self):
        return f"SwimmingCat:{self.name}  |  {self.age}"

    
sadik = SwimmingCat("sadik", 2, "RED")
sadik.__dict__
{'name': 'sadik', 'age': 2, 'color': 'RED'}


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"Hello! My name is {self.name} and I'm {self.age} old")
    def grow(self):
        self.age += 1
    def __str__(self):
        return f"{self.name}  |  {self.age}"

    
c1 = Cat("jojo", 1)
c1.hello
<bound method Cat.hello of <__main__.Cat object at 0x0000020C7BAB6F90>>
c1.hello()
Hello! My name is jojo and I'm 1 old
c1.name = "noname"
c1.hello()
Hello! My name is noname and I'm 1 old

class Cat:
    def __init__(self, name, age):
        self.__name = name
        self.age = age
    def hello(self):
        print(f"Hello! My name is {self.name} and I'm {self.age} old")
    def grow(self):
        self.age += 1
    def __str__(self):
        return f"{self.name}  |  {self.age}"

    
c1.name()
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    c1.name()
TypeError: 'str' object is not callable
c1.name
'noname'
class Cat:
    def __init__(self, name, age):
...         self.__name = name
...         self.age = age
...     def hello(self):
...         print(f"Hello! My name is {self.__name} and I'm {self.age} old")
...     def grow(self):
...         self.age += 1
...     def __str__(self):
...         return f"{self.__name}  |  {self.age}"
... 
...     
>>> c1.name
'noname'
>>> class Cat:
...     def __init__(self, name, age):
...         self.__name = name
...         self.age = age
...     def hello(self):
...         print(f"Hello! My name is {self.__name} and I'm {self.age} old")
...     def grow(self):
...         self.age += 1
...     def __str__(self):
...         return f"{self.__name}  |  {self.age}"
...     def change.name(self, name):
...         
SyntaxError: expected '('
>>> class Cat:
...     def __init__(self, name, age):
...         self.__name = name
...         self.age = age
...     def hello(self):
...         print(f"Hello! My name is {self.__name} and I'm {self.age} old")
...     def grow(self):
...         self.age += 1
...     def __str__(self):
...         return f"{self.__name}  |  {self.age}"
...     def change_name(self, name):
...         pass
... 
...     
