# ============================================================
# ARRAYS - Operations in Python
# ============================================================


# ------------------------------------------------------------
# 1. CREATING ARRAYS
# ------------------------------------------------------------

arr = []
print("Empty array:", arr)

arr = [10, 20, 30, 40, 50]
print("Array with elements:", arr)

arr = [0] * 5
print("Same value repeated:", arr)

arr = list(range(5))
print("From range:", arr)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("2D array element at row 1, col 2:", matrix[1][2])


# ------------------------------------------------------------
# 2. ACCESSING ELEMENTS
# ------------------------------------------------------------

arr = [10, 20, 30, 40, 50]

print("First element:", arr[0])
print("Last element:", arr[-1])
print("Second from last:", arr[-2])
print("Slice [1:3]:", arr[1:3])
print("Slice [:3]:", arr[:3])
print("Slice [2:]:", arr[2:])
print("Reversed:", arr[::-1])


# ------------------------------------------------------------
# 3. TRAVERSAL
# ------------------------------------------------------------

arr = [10, 20, 30, 40, 50]

for num in arr:
    print("Basic loop:", num)

for i, num in enumerate(arr):
    print("With index:", i, num)

i = 0
while i < len(arr):
    print("While loop:", arr[i])
    i += 1

left, right = 0, len(arr) - 1
while left < right:
    print("Two pointer — left:", arr[left], "right:", arr[right])
    left += 1
    right -= 1


# ------------------------------------------------------------
# 4. INSERTION
# ------------------------------------------------------------

arr = [10, 20, 30, 40, 50]

arr.append(60)
print("After append:", arr)

arr.insert(2, 99)
print("After insert at middle:", arr)

arr.insert(0, 1)
print("After insert at beginning:", arr)


# ------------------------------------------------------------
# 5. DELETION
# ------------------------------------------------------------

arr = [10, 20, 30, 40, 50]

arr.pop()
print("After pop from end:", arr)

arr.pop(1)
print("After pop at index 1:", arr)

arr.remove(30)
print("After remove value 30:", arr)

arr = [10, 20, 30, 40, 50]
del arr[2]
print("After del at index 2:", arr)


# ------------------------------------------------------------
# 6. UPDATING
# ------------------------------------------------------------

arr = [10, 20, 30, 40, 50]

arr[2] = 99
print("After updating index 2:", arr)

arr[0], arr[4] = arr[4], arr[0]
print("After swapping index 0 and 4:", arr)


# ------------------------------------------------------------
# 7. USEFUL BUILT-INS
# ------------------------------------------------------------

arr = [40, 10, 50, 20, 30]

print("Length:", len(arr))
print("Min:", min(arr))
print("Max:", max(arr))
print("Sum:", sum(arr))
print("sorted():", sorted(arr))
arr.sort()
print("After .sort():", arr)
arr.sort(reverse=True)
print("After .sort(reverse=True):", arr)
print("30 in arr:", 30 in arr)

arr = [10, 20, 10, 30, 10]
print("Count of 10:", arr.count(10))


# ------------------------------------------------------------
# 8. THE COPY TRAP
# ------------------------------------------------------------

a = [1, 2, 3]
b = a
b[0] = 99
print("Wrong copy — a also changed:", a)

a = [1, 2, 3]
b = a.copy()
b[0] = 99
print("Right copy — a is safe:", a)