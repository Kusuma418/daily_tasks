# concat list using array 
import array
a=array.array('i', [1, 2, 3])
b=array.array('i', [4, 5, 6])
c=a+b
print(c)

# leap year program
year=int(input("enter a year:"))
if (year%4==0 and year%100!=0) or year%400==0:
    print("leap year")
else:
    print("not")
    
# transpose of a 2x2 NumPy array is equal to the original array
import numpy as np
arr=np.array([[1,1],[1,1]])
arr2=np.zeros([2,2])
for i in range(2):
    for j in range(2):
        arr2[j,i]=arr[i,j]
if np.array_equal(arr,arr2):
    print("same")
else:
    print("not")
    
# converting a decimal (base-10) number to its binary (base-2) equivalent
n=int(input())
b=""
while n>0:
    b=str(n%2)+b
    n=n//2
print("Binary: "+b)

# longest common prefix
def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for word in strs[1:]:
        while word[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Regular Expression Matching problem
import re
def isMatch(s: str, p: str) -> bool:
    return re.fullmatch(p, s) is not None

# Minimum Absolute Difference problem in arrays
def minimumAbsDifference(arr):
    arr.sort()  
    min_diff = float('inf')  # Start with a large value
    result = []
    # Step 3: Find the minimum difference
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        if diff < min_diff:
            min_diff = diff
            result = [[arr[i - 1], arr[i]]]
        elif diff == min_diff:
            result.append([arr[i - 1], arr[i]])
    return result

# Finds pairs with fixed difference
num=[1,2,3,4,5,6,3,7,2,7]
a=len(num)
for i in range(a):
    for j in range(i+1,a):
        d=[]
        if num[j]-num[i]==6:
            d.append(num[i])
            d.append(num[j])
            print(d)
            
# subtracting product and sum from given number
def subtractProductAndSum(n):
    product = 1
    total_sum = 0
    for digit in str(n):
        d = int(digit)
        product *= d
        total_sum += d
    return product - total_sum

# Divide Array in Sets of K Consecutive Numbers problem
def isPossibleDivide(nums, k):
    if len(nums) % k != 0:
        return False  # Cannot divide evenly
    nums.sort()
    while nums:
        first = nums[0]
        # Try to remove k consecutive numbers starting from the smallest
        for i in range(k):
            if first + i not in nums:
                return False
            nums.remove(first + i)  # Remove one occurrence
    return True


