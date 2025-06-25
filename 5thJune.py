# optimizing codes
def most_frequent(lst):
    max_count = 0
    most_common = None
    for x in lst:
        count = lst.count(x)
        if count > max_count:
            max_count = count
            most_common = x
    return most_common
# the above is in O(n²)

#optimize it to O(n) by building your own frequency dictionary.
def most_frequent(lst):
    if not lst:
        return None  # handle empty list
    freq = {}
    max_count = 0
    most_common = None
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
        if freq[item] > max_count:
            max_count = freq[item]
            most_common = item
    return most_common

# Sum of Pairs Equal to Target 
# optimized code with O(n)
def pairs_target(lst,target):
    seen=set()
    for n in lst:
        if target-n in seen:
            return (target-n,n)
        seen.add(n)
    return None

# sorting an array with only one loop
arr = [5, 2, 9, 1, 3]
i = 0
while i < len(arr) - 1:
    if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        i = 0
    else:
        i += 1
print(arr)


#Python Code to Call Stored Procedure
import mysql.connector
# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)
cursor = conn.cursor()
# Call the stored procedure
min_salary = 48000
cursor.callproc("GetHighEarners", [min_salary])
# Fetch and print the results
for result in cursor.stored_results():
    rows = result.fetchall()
    for row in rows:
        print(row)
cursor.close()
conn.close()


