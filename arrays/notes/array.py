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
