# 1. Creating an empty array

arr = []
print("Printing an empty array:", arr)

# 2. Array with elements

arr = [10, 20, 30, 40, 50]
print("Printing an array with elements:", arr)

# 3. From a range

arr = list(range(5))
print("Printing an range of arrays", arr)

# 4. 2D array
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Printing 2D array:", matrix[1][2])


# 5. Accessing elements
arr = [10, 20, 30, 40, 50]

# By index
print(arr[0])  # 10 → first element
print(arr[4])  # 50 → last element
print(arr[-1])  # 50 → last element (negative index)
print(arr[-2])  # 40 → second from last

# Slicing
print(arr[1:3])  # [20, 30] → index 1 up to (not including) 3
print(arr[:3])  # [10, 20, 30] → start to index 3
print(arr[2:])  # [30, 40, 50] → index 2 to end
print(arr[::-1])  # [50, 40, 30, 20, 10] → reversed

# 6. Traversal
arr = [10, 20, 30, 40, 50]

for num in arr:
    print("Pritning num value in traversal:", num)
    
for i, num in enumerate(arr):
    print("Printing num and i value is traversal:", i, num)
        
i = 0
while (i<len(arr)):
    print("While loop:", i)
    i = i+1

# 7. Insertion
arr = [10, 20, 30, 40, 50]

# Insert at end → O(1)
arr.append(60)
print("Print append:", arr)              # [10, 20, 30, 40, 50, 60]

# Insert at middle → O(n)
arr.insert(2, 99)       # index 2, value 99
print("Print append:", arr)              # [10, 20, 99, 30, 40, 50, 60]

# Insert at beginning → O(n)
arr.insert(0, 1)
print("Print append:", arr)              # [1, 10, 20, 99, 30, 40, 50, 60]


# 8. Deletion 
arr = [10, 20, 30, 40, 50]

# Delete from end → O(1)
arr.pop()
print(arr)              # [10, 20, 30, 40]

# Delete from middle by index → O(n)
arr.pop(1)              # removes index 1
print(arr)              # [10, 30, 40]

# Delete by value → O(n)
arr.remove(30)          # removes first occurrence of value 30
print(arr)              # [10, 40]

# Delete using del
arr = [10, 20, 30, 40, 50]
del arr[2]
print(arr)              # [10, 20, 40, 50]\
    
# 9. Updating

arr = [10, 20, 30, 40, 50]

arr[2] = 99
print("Updated array:", arr)

arr[0], arr[1] = arr[1], arr[0]
print("swapped array:", arr)
