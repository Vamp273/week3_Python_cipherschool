class A:
    def __init__(self):
        print("A init excuted")

class B(A):
    def __init__(self):
        print("B init executed")
        super().__init__()

abc = B()

""" MRO ( METHOD RESOLUTION ORDER ) """

class A1:
    x = 5

class B1(A1):
    x = 5

class C(B):
    pass

class D(A):
    x = 10

class E(C,D):
    pass

e = E()
print(e.x)

E.nro()

""" DFS
        if there is a loop solve branches diffenently """


"""
ITERATION PROTOCOL
for any object to be an iterable, it should have 2 dunders
1. __iter__
2. __next__

PORTABLE 
object's'__iter__' method should return an integer
operator's'__next__' method should return the new value on every call
1. if the iterator the end, it should raise an StopIteration exception
"""

a = range(5)
it = a.__iter__()
it
it.__next__()
next(it)

class myrange():
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return myrange_iterator(self)

class myrange_iterator:
    def __init__(self, myrange):
        self.myrange = myrange
        self.i = 0

    def __next__(self):
        ret = self.i
        self.i += 1

        if ret >= self.myrange.n:
            raise StopIteration

        return ret

for i in myrange(5):
    print(i)
    
a = myrange(5)
it = iter(a)

next(it)