Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.


def a(v=100):
    return v

a()
100
a(9999)
9999
v
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    v
NameError: name 'v' is not defined
a()
100
a
<function a at 0x0000025CC12F8E00>


#wallet
# amount
# set get

class Wallet:
    def __init__(self, amount=0):
        self.set_amount(amount)
    def get_amount(self):
        return self.amount
    def set_amount(self, value):
        if value < 0:
            pass
        self._amount = value

        
class NegaAmount(Exception):
    """Balance negative"""
    pass

raise NegaAmount
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    raise NegaAmount
NegaAmount

class Wallet:
    def __init__(self, amount=0):
        self.set_amount(amount)
    def get_amount(self):
        return self.amount
    def set_amount(self, value):
        if value < 0:
            raise NegaAmount
        self._amount = value

        
user1 = Wallet()
user1.__dict__
{'_amount': 0}
user2 = Wallet(100)
user2.__dict__
{'_amount': 100}
user2.get.amount
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    user2.get.amount
AttributeError: 'Wallet' object has no attribute 'get'
class Wallet:
    def __init__(self, amount=0):
        self.set_amount(amount)
    def get_amount(self):
        return self._amount
    def set_amount(self, value):
        if value < 0:
            raise NegaAmount
        self._amount = value

        
user1.get_amount()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    user1.get_amount()
  File "<pyshell#33>", line 5, in get_amount
    return self.amount
AttributeError: 'Wallet' object has no attribute 'amount'. Did you mean: '_amount'?
class Wallet:
    def __init__(self, amount=0):
        self.set_amount(amount)
    def get_amount(self):
        return self._amount
    def set_amount(self, value):
        if value < 0:
            raise NegaAmount
        self._amount = value

        
user1 = Wallet()
user2 = Wallet(100)
user2.set_amount(1000)
user2.get_amount
<bound method Wallet.get_amount of <__main__.Wallet object at 0x0000025CC0DDBD90>>
user2.get_amount()
1000

class Wallet:
    def __init__(self, amount=0):
        self.set_amount(amount)
    def get_amount(self):
        return self._amount
    def set_amount(self, value):
        if value < 0:
            raise NegaAmount
        self._amount = value
    amount = property(get_amount, set_amount)

    
user1 = Wallet()
user2 = Wallet(100)
user2.amount
100
user2.amount = 100000
user2.amount
100000
user2.__dict__
{'_amount': 100000}


def summ(a, b)
SyntaxError: expected ':'
def summ(a, b):
    return a+b

summ(4,5)
9
summ(4,5,5)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    summ(4,5,5)
TypeError: summ() takes 2 positional arguments but 3 were given
def MyPrint(a,b,c)
SyntaxError: expected ':'
def MyPrint(a,b,c):
    print(a,b,c)

    
MyPrint(1,2,3)
1 2 3
help(print)
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.

def MyPrint(args):
    print(type(args))
    for val in args:
        print(val, end = "  ")

        
MyPrint(1,2,3,4)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    MyPrint(1,2,3,4)
TypeError: MyPrint() takes 1 positional argument but 4 were given
MyPrint([1,2,3,4])
<class 'list'>
1  2  3  4  


def MyPrint(args):
    print(type(args))
    for val in args:
        print(val, end = "  ")

        
MyPrint([1,2,3,4])
<class 'list'>
1  2  3  4  
def MyPrint(*args):
    print(type(args))
    for val in args:
        print(val, end = "  ")

        
MyPrint([1,2,3,4])
<class 'tuple'>
[1, 2, 3, 4]  

def MyPrint(*args):
    print(type(args))
    print(args)
    for val in args:
        print(val, end = "  ")

        
MyPrint([1,2,3,4])
<class 'tuple'>
([1, 2, 3, 4],)
[1, 2, 3, 4]  
MyPrint(1,2,3,4, [123, 4,5], True, .3)
<class 'tuple'>
(1, 2, 3, 4, [123, 4, 5], True, 0.3)
1  2  3  4  [123, 4, 5]  True  0.3  

d

def myPrint(*args, sep=' ', end='\n')
SyntaxError: expected ':'
for val in args
SyntaxError: expected ':'
def myPrint(*args, sep=' ', end='\n'):
    def val in args:
        
SyntaxError: expected '('
def myPrint(*args, sep=' ', end='\n'):
    for val in args:
        print(val, end = mySep
    print(end = myEnd)
              
SyntaxError: '(' was never closed
def myPrint(*args, sep=' ', end='\n'):
    for val in args:
        print(val, end = mySep)
    print(end = myEnd)

    
myPrint()
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    myPrint()
  File "<pyshell#102>", line 4, in myPrint
    print(end = myEnd)
NameError: name 'myEnd' is not defined
def myPrint(*args, mySep=' ', myEnd='\n'):
    for val in args:
        print(val, end = mySep)
    print(end = myEnd)

    
myPrint()

def summ(*args):
    res = 0
    for i in args:
        res += i
    return res

summ(1,2,3,436)
442


# *args  **kwargs

def family(**kwargs):
    print(kwargs)
    print(type(kwargs))

    
family(Nikola="dad", Mary="mom")
{'Nikola': 'dad', 'Mary': 'mom'}
<class 'dict'>
family(Nikola="dad", Mary="mom", sister = 11)
{'Nikola': 'dad', 'Mary': 'mom', 'sister': 11}
<class 'dict'>

# func (a,b,c, *args, **kwargs)

def func(a,b,*args):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))

    
func(1,2,3,4,5,6,6,79)
1 <class 'int'>
2 <class 'int'>
(3, 4, 5, 6, 6, 79) <class 'tuple'>

def func(*args, a,b):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))

    
func(1,2,3,4,5,6,6,79)
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    func(1,2,3,4,5,6,6,79)
TypeError: func() missing 2 required keyword-only arguments: 'a' and 'b'
def func(*args, a=100,b=2202):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))

    
func(1,2,3,4,5,6,6,79)
100 <class 'int'>
2202 <class 'int'>
(1, 2, 3, 4, 5, 6, 6, 79) <class 'tuple'>
def func(a=100,b=2202, *args):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))

    
func(1,2,3,4,5,6,6,79)
1 <class 'int'>
2 <class 'int'>
(3, 4, 5, 6, 6, 79) <class 'tuple'>


def func(a=100,b=2202, *args):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))
    print(kwargs, type(kwargs))

    
func(1,2)
1 <class 'int'>
2 <class 'int'>
() <class 'tuple'>
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    func(1,2)
  File "<pyshell#146>", line 5, in func
    print(kwargs, type(kwargs))
NameError: name 'kwargs' is not defined. Did you mean: 'args'?
print(args, type(args))NameError: name 'kwargs' is not defined. Did you mean: 'args'?
SyntaxError: invalid syntax
def func(a=100,b=2202, *args, **kwargs):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))
    print(kwargs, type(kwargs))

    
func(1,2)
1 <class 'int'>
2 <class 'int'>
() <class 'tuple'>
{} <class 'dict'>







































li1 = [1,2,3,4]
li2 = [3,4,5,6,7]
li3 = [li1, li2]
li3
[[1, 2, 3, 4], [3, 4, 5, 6, 7]]
li3 = [*li1, *li2]
li3
[1, 2, 3, 4, 3, 4, 5, 6, 7]


di1 = {1:11, 2:22}
di2 = {4:11, 5:22}
di3 = {**di1, **di2}
di3
{1: 11, 2: 22, 4: 11, 5: 22}


def converter(bitcoin):
    return bitcoin*100000

converter
<function converter at 0x0000025CC131D580>
b1 = 9
converter(b1)
900000

lambda bitcoin: bitcoin * 95000
<function <lambda> at 0x0000025CC131D300>
(lambda bitcoin: bitcoin * 95000) (b1)
855000


li = [1,2,3,4,5,6]



class Febo:
    def __init__(self, fn):
        self.fn = fn
        self.i = 0
        self.f1 = self.f2 = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.i += 1
        if self.i > self.fn:
            raise StopIteration
        if self.i == 1 or self.i == 2:
            return 1
        fret = self.f1 + self.f2
        self.f1, self.f2 = self.f2, fret

        
class Febo:
    def __init__(self, fn):
        self.fn = fn
        self.i = 0
        self.f1 = self.f2 = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.i += 1
        if self.i > self.fn:
            raise StopIteration
        if self.i == 1 or self.i == 2:
            return 1
        fret = self.f1 + self.f2
        self.f1, self.f2 = self.f2, fret
        return fret

    
febx = Febo(10)
for f in febx:
    print(f, end="  ")

    
1  1  2  3  5  8  13  21  34  55  


li = [i**2 for i in range 100]
SyntaxError: invalid syntax

li = [i**2 for i in range(100)]
li
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801]

gen = (i**2 for i in range(100))
gen
<generator object <genexpr> at 0x0000025CC12F4A00>
next(gen)
0
next(gen)
1
next(gen)
4
next(gen)
9
next(gen)
16
next(gen)
25
next(gen)
36
next(gen)
49
next(gen)
64
next(gen)
81
next(gen)
100

# gen expr
gen = (i**2 for i in range(100))

# func gen
def func(n):
    start = 0
    for i in range(n):
        start += 1
        return start

    
func(10)
1
func(11)
1
next(func)
Traceback (most recent call last):
  File "<pyshell#256>", line 1, in <module>
    next(func)
TypeError: 'function' object is not an iterator

# return - return
# помнила прошлое - yield
def func(n):
    start = 0
    for i in range(n):
        start += 1
        yield start

        
func(10)
<generator object func at 0x0000025CC12F4A00>

def func(n):
    start = 0
    for i in range(n):
        start += 1
        return start

    
func_gen = func(10)
def func(n):
    start = 0
    for i in range(n):
        start += 1
        yield start

        
func_gen = func(10)
func_gen
<generator object func at 0x0000025CC12F4930>

next(func_gen)
1
next(func_gen)
2
next(func_gen)
3
next(func_gen)
4
next(func_gen)
5
def func(n):
    start = 0
    for i in range(n):
        start += 1
        yield start

        
for i in func(10)
SyntaxError: expected ':'
for i in func(10):
    print(i)

    
1
2
3
4
5
6
7
8
9
10


# map
# filter
# zip

li = [1,2,3,4,4,5]
li2 = ["one", "two", "three"]
res_list = list(zip(li2, li))
res_list
[('one', 1), ('two', 2), ('three', 3)]


li = [1,2,3]
li2 = ["one", "two", "three"]
li3 = ["oOOne", "tWWwo", "tHHhree"]
res_list = list(zip(li2, li, li3))
res_list
[('one', 1, 'oOOne'), ('two', 2, 'tWWwo'), ('three', 3, 'tHHhree')]

li = [1,2,3,4,5,6,7,8,87]
li
[1, 2, 3, 4, 5, 6, 7, 8, 87]
m = map(lambda x: x**2/2, li)
m
<map object at 0x0000025CC1316F50>
li = list(m)
li
[0.5, 2.0, 4.5, 8.0, 12.5, 18.0, 24.5, 32.0, 3784.5]
m
<map object at 0x0000025CC1316F50>
for i in m.
SyntaxError: invalid syntax
5863
5863
for i in m:
    print(i)

    
m = map(lambda x: x**2/2, li)
for i in m:
    print(i)

    
0.125
2.0
10.125
32.0
78.125
162.0
300.125
512.0
7161220.125

for i in m:
    print(i)

    
help(filter)
Help on class filter in module builtins:

class filter(object)
 |  filter(function, iterable, /)
 |
 |  Return an iterator yielding those items of iterable for which function(item)
 |  is true. If function is None, return the items that are true.
 |
 |  Methods defined here:
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __next__(self, /)
 |      Implement next(self).
 |
 |  __reduce__(self, /)
 |      Return state information for pickling.
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.

for i in filter(lambda x: x%2 == 0, li)
SyntaxError: expected ':'
for i in filter(lambda x: x%2 == 0, li):
    print(i)

    
2.0
8.0
18.0
32.0
    print(i)
    
SyntaxError: unexpected indent
for i in filter(lambda x: x%2 == 0, li):
    SyntaxError: unexpected indent
    
SyntaxError: invalid syntax

def func():
    number = 10
    return number

func()
10

def func():
    number = 10
    def inner():
        value = 5 + number
        return value
    return number

func()
10
def func():
    number = 10
...     def inner():
...         value = 5 + number
...         return value
...     return inner
... 
>>> func()
<function func.<locals>.inner at 0x0000025CC1318540>
>>> result_inner_func = func()
4
>>> result_inner_func()
15
>>> 
>>> result_inner_func.__closure__
(<cell at 0x0000025CC1316EF0: int object at 0x00007FFA3EEA24C8>,)
>>> 
>>> dog = type("Dog", (object,), {"counter":1})
>>> dog
<class '__main__.Dog'>
>>> dog.__name__
'Dog'
>>> dog.__bases__
(<class 'object'>,)
>>> dog.__dict__
mappingproxy({'counter': 1, '__module__': '__main__', '__dict__': <attribute '__dict__' of 'Dog' objects>, '__weakref__': <attribute '__weakref__' of 'Dog' objects>, '__doc__': None})
>>> 
>>> class Dog1:
...     counter=1
... 
...     
>>> d1 = dog()
>>> d1
<__main__.Dog object at 0x0000025CC0DE67B0>
>>> d2 = Dog1()
>>> d2
<__main__.Dog1 object at 0x0000025CC0DE6BA0>
