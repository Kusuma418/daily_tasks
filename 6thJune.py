# Custom exception
class ineligible(Exception):
    pass
age = int(input("Enter age = "))
if age >= 18:
    print("Eligible to vote")
else:
    try:
        raise ineligible("not eligible to vote")
    except ineligible as e:
        print(e)
        
# Decorator
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper
@decorator
def say_hello():
    print("Hello, Remya Mam!")
say_hello()


# Mutable Default Argument
def append_to_list(value, lst=[]):
    lst.append(value)
    return lst
print(append_to_list(1))
print(append_to_list(2))
print(append_to_list(3))

# the output
# [1]
# [1, 2]
# [1, 2, 3]

#to Avoid This Shared Mutable Default Argument
def append_to_list(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst


# == when you care if values are equal.
# is when you care if two variables refer to the exact same object.
x = 1000
y = 1000
print(x == y)  # True – values are equal
print(x is y)  # False – may be False because integers > 256 are not cached


# 1,2,5,6,9,0,0,0 -----output should be
a = [1, 0, 5, 0, 6, 2, 0, 9]
n = len(a)
k = 0  
for i in range(n):
    if a[i] != 0:
        a[k] = a[i]
        k += 1
for i in range(k, n):
    a[i] = 0
for i in range(k):
    for j in range(0, k - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]  
print(a)


# Inner Class implementation
# An inner class (also called a nested class) is a class defined inside another class. It is typically used when the inner class is logically dependent on the outer class.
class Outer:
    class Inner:
        def display(self):
            print("This is the Inner class")
# Accessing the inner class
inner_obj = Outer.Inner()
inner_obj.display()

# Why use Inner Classes?
# To logically group classes that are only used in one place.
# To keep your code clean and encapsulated.
# To model "has-a" relationships, like Laptop has a Battery.


# shallow copy
import copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
shallow[0][0] = 100
print("Original:", original)  # [[100, 2], [3, 4]]
print("Shallow:", shallow)    # [[100, 2], [3, 4]]

#deep copy
import copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 999
print("Original:", original)  # [[1, 2], [3, 4]]
print("Deep:", deep)          # [[999, 2], [3, 4]]


#non local example
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
        print("Inner:", x)
    inner()
    print("Outer:", x)
outer()   #Inner: 15 Outer: 15

#Example Without nonlocal:
def outer():
    x = 10
    def inner():
        x += 5  
        print("Inner:", x)
    inner()
    print("Outer:", x)  #UnboundLocalError: local variable 'x' referenced before assignment
