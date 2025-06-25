#String Wrap
def wrap_string(S, W):
    for i in range(0, len(S), W):
        print(S[i:i+W])
# Example 
S = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
W = 4
wrap_string(S, W)

#Alphabet Rangoli
import string
def print_rangoli(size):
    alpha = string.ascii_lowercase
    lines = []
    for i in range(size):
        left = alpha[size-1:i:-1]  # e.g., 'edc'
        center = alpha[i]          # e.g., 'b'
        right = alpha[i+1:size]    # e.g., 'cde'
        line = '-'.join(left + center + right)
        lines.append(line.center(4 * size - 3, '-'))
    for line in lines[::-1]:
        print(line)
    for line in lines[1:]:
        print(line)
print_rangoli(3)
print_rangoli(5)


#Find the Day from a Date
import calendar
def find_day(month, day, year):
    day_index = calendar.weekday(year, month, day)
    return calendar.day_name[day_index].upper()
#example
month, day, year = map(int, input().split())
print(find_day(month, day, year))


#Symmetric Difference of Two Sets
# Input
m = int(input())
set_m = set(map(int, input().split()))
n = int(input())
set_n = set(map(int, input().split()))

# Symmetric difference and output
result = sorted(set_m ^ set_n)
for num in result:
    print(num)
# ^ operator is used to compute symmetric difference between two sets in Python.

#reversing a string
# Accept input from the user
input_string = input("Enter a string: ")
reversed_string = input_string[::-1]
print(reversed_string)

# to print characters at even indexes from a string
input_string = input("Enter a string: ")
even_index_chars = input_string[::2]
print(even_index_chars)


#Intersection of Two Lists
list1 = [1, 3, 6, 78, 35, 55]
list2 = [12, 24, 35, 24, 88, 120, 155]
set1 = set(list1)
set2 = set(list2)
set1 &= set2
result = list(set1)
print(result) # output: [35]

#Class Inheritance (Person, Male, Female)
class Person:
    def getGender(self):
        return "Unknown"
class Male(Person):
    def getGender(self):
        return "Male"
class Female(Person):
    def getGender(self):
        return "Female"
m = Male()
f = Female()
print(m.getGender())  # Output: Male
print(f.getGender())  # Output: Female
