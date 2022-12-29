# OOPS CONCEPT

# Empty class
class A1:
    pass

b = A1.__call__()
b = A1()

def func():
    print("Hello")

a = 5
def func():
    pass

class A:
    name = "jatin"
    marks = 50


class A2:
    def __call__(self):
        print("You called me")

a = A2()
print(type(a))

a()

b = A.__call__(A)

for i in range(5):
    print(i)

d = {"name":"Jatin"}
print(d["name"])

a.__getitem__("name")


class Exponent:
    def __init__(self,n):
        self.n = n

    def __getitem__(self, x):
        return x**self.n

e = Exponent(3)
e[16]

class Person:
    name = "jatin"
    def __init__(self,n):
        self.n = n

y = Person(2)
y.name
y.n


class Dog:
    kind = "canine"

    def __init__(self, name):
        self.name = name

g = Dog("Maxx")
g.kind

class Dogs:
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_tricks(self, tricks):
        self.tricks.append(tricks)

d1 = Dogs("Maxx")
d1.add_tricks("fetch")
d1.add_tricks("talk")
d1.tricks

d2 = Dogs("Bella")
d2.tricks

a = []
b = a
b.append(1)
a