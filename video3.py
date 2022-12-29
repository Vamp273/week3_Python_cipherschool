# GENERATORS

# def generate_aquaures(n):
#     a = []
#     for i in range(i,100):
#         a.append(i**2)

#     return a

# EAGER LOADING
def generate_squaures(n):
    return [ i**2 for i in range(1,n) ]

for x in generate_squaures(100):
    print(x)

from time import sleep

def func():
    print("started")
    yield
    sleep(5)
    # for i in range(100000000):
    #     pass
    print("ended")

print("hello")
it = iter(func())
next(it)
func()
print("world")

def func():
    print("Start")
    yield 1
    print("yielded 1")
    yield 2
    print("yielded 2")

it = iter(func())
next(it)

next(it)

# Lazy loading

def generate_squares(n):
    for i in range(1,n):
        yield i**2

a = generate_squares(10)
print(type(a))

it = iter(generate_squares(10))
next(it)

a = generate_squares(10)
next(a)

for i in generate_squares(10):
    print(i)

d = ( i**2 for i in range(10))
for i in a:
    print(i)

for i in d:
    print(i)