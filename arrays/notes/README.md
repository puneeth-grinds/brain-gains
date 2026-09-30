# Arrays

## What is an Array?
A collection of elements stored in a sequence where every element is identified by an **index** (its position).

```
Seat No →   1      2      3      4      5
          ┌──────┬──────┬──────┬──────┬──────┐
          │ John │ Mary │ Alex │  --  │ Sara │
          └──────┴──────┴──────┴──────┴──────┘
```

---

## How it Sits in Memory
- Every element sits **next to each other** in memory — contiguous, never scattered
- Each element takes up **equal space** in memory
- Because of this layout, the computer doesn't **search** for an element — it **calculates** the address directly and jumps there in one step → **O(1) access**

### Address Calculation Formula

```
Address of element at index i = Base Address + (i × size of each element)
```

**Example:**

```
Base Address = 1000 | Each element = 1 byte

Index 0 → 1000 + (0 × 1) = 1000
Index 3 → 1000 + (3 × 1) = 1003
Index 4 → 1000 + (4 × 1) = 1004
```

---

## Static vs Dynamic Arrays

| | Static | Dynamic |
|---|---|---|
| Size | Fixed at creation | Flexible, grows as needed |
| Flexibility |  Cannot resize |  Resizes automatically |
| Example | Arrays in C/Java | Lists in Python |

> Python lists are **dynamic arrays** under the hood — you never worry about size.

---

## Key Trade-off
> Arrays give you **speed of access O(1)** in exchange for **flexibility in the middle.**
> Since elements are contiguous in memory, inserting or deleting in the middle requires shifting all surrounding elements — which is expensive.

## Operations

### 1. Accessing / Reading
- Go to a specific index and read the value there
- Always **O(1)** — no matter which index, no matter how big the array
- This is the biggest strength of arrays

---

### 2. Traversal
- Visiting every element one by one — to read, compare, or do something with each
- Always **O(n)** — you visit every element once
- Most array problems involve traversal in some form

---

### 3. Insertion

| Where | What Happens | Cost |
|---|---|---|
| End | Just place in next empty slot — nothing shifts | O(1) |
| Middle | Shift every element after insertion point one step right, then insert | O(n) |
| Beginning | Shift every single element one step right, then insert | O(n) |

---

### 4. Deletion

| Where | What Happens | Cost |
|---|---|---|
| End | Just remove — nothing shifts | O(1) |
| Middle | Remove element, shift everything after it one step left to fill gap | O(n) |
| Beginning | Remove element, shift every single element one step left | O(n) |

---

### Summary Table

| Operation | Cost | Why |
|---|---|---|
| Access by index | O(1) | Direct address calculation — any index, always one step |
| Traversal | O(n) | Visit every element |
| Insert at end | O(1) | No shifting needed |
| Insert at middle/start | O(n) | Shifting required |
| Delete from end | O(1) | No shifting needed |
| Delete from middle/start | O(n) | Shifting required |

---

### Key Mental Model
> **End operations are cheap. Middle and start operations are expensive.**
> Because arrays are contiguous in memory — touching the middle or start means shifting neighbours.
> The end has no neighbours after it, so nothing shifts.

## Complexity

### What is Complexity?
> "As the input grows bigger, how does my operation's cost grow?"

It is never about exact time in seconds — it is about the **rate of growth.** That is what Big O measures.

---

### Time Complexity

**The One Rule to Internalize**
> The more elements you have to touch — the more expensive the operation.

| Complexity | Name | Meaning |
|---|---|---|
| O(1) | Constant | Cost stays the same no matter how big the input gets |
| O(n) | Linear | Cost grows as the input grows |

| Operation | Complexity | Why |
|---|---|---|
| Access by index | O(1) | One address calculation — always one step regardless of size |
| Traversal | O(n) | Every element is visited once |
| Insert at end | O(1) | Nothing shifts — doesn't matter if 2 or 2000 elements |
| Insert at middle/start | O(n) | Every element after insertion point must shift |
| Delete from end | O(1) | Nothing shifts — doesn't matter if 2 or 2000 elements |
| Delete from middle/start | O(n) | Every element after deletion point must shift |

---

### Space Complexity
> "How much **extra** memory does my operation need?"

The array itself does not count — only the additional memory created on top of the input.

| Complexity | Meaning | Example |
|---|---|---|
| O(1) | Extra memory stays flat regardless of input size | Using a single variable to track an index |
| O(n) | Extra memory grows with input size | Creating a full copy of the array |

---

### The In-Place Constraint
When an interviewer says **"solve it in-place"** they mean:
> Do not create a new array or copy. Work directly on the existing array.
> This means your solution must use **O(1) space.**

---

### The Two Questions to Ask For Every Solution

```
1. How does TIME grow as input grows?
   → Count how many elements you are touching

2. How does SPACE grow as input grows?
   → Count what extra memory you are creating
```

## Types of Arrays

### 1. One-Dimensional Array (1D)
A single row of elements. One index to locate any element.

```
[10, 20, 30, 40, 50]
  ↑                ↑
index 0          index 4
```

---

### 2. Two-Dimensional Array (2D) / Matrix
An array of arrays — rows and columns, like a grid or spreadsheet.

```
        Col 0  Col 1  Col 2
Row 0 → [  1,    2,    3  ]
Row 1 → [  4,    5,    6  ]
Row 2 → [  7,    8,    9  ]
```

- Two indices needed to locate any element — **row** and **column**
- Element at Row 1, Col 2 → 6

**How it sits in memory:**
Even though it looks like a grid, memory is one long flat line.
A 2D array gets flattened **row by row** into memory — this is called **row-major order.**

```
Matrix:          In Memory (flattened):
[ 1, 2, 3 ]
[ 4, 5, 6 ]  →  [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
[ 7, 8, 9 ]       ↑─ Row 0 ─↑─ Row 1 ─↑─ Row 2 ─↑
```

Access is still **O(1)** — just an extended formula:
```
Address = Base + (row × number of columns + column) × element size
```

**Where you'll see 2D arrays in problems:**
- Grid traversal (islands, mazes)
- Dynamic Programming (DP tables)
- Graphs (adjacency matrix)
- Game boards (chess, minesweeper)

---

### 3. Jagged Array
A 2D array where each row can have a **different number of columns** — unlike a regular matrix where every row is the same length.

```
Regular Matrix (uniform):       Jagged Array (uneven):
[ 1, 2, 3 ]                     [ 1, 2 ]
[ 4, 5, 6 ]                     [ 3, 4, 5, 6 ]
[ 7, 8, 9 ]                     [ 7 ]
```

> Just be aware this exists — you will occasionally see it in problems involving triangles or variable length rows.

---

### Quick Reference

| Type | Indices Needed | Structure |
|---|---|---|
| 1D Array | 1 (index) | Single row |
| 2D Array | 2 (row, column) | Grid — uniform row lengths |
| Jagged Array | 2 (row, column) | Grid — uneven row lengths |

## Pros, Cons & When to Use

### Where Arrays Shine 

| Strength | Why |
|---|---|
| Fast Access | Know the index → get the element instantly in O(1) |
| Cache Friendly | Elements are contiguous in memory — CPU loads chunks at once, making traversal fast |
| Simple & Lightweight | No extra pointers or overhead — just elements side by side |
| Great for Iteration | Most natural and efficient structure for visiting every element in order |

---

### Where Arrays Fall Apart 

| Weakness | Why |
|---|---|
| Expensive middle insertions/deletions | Shifting elements is O(n) |
| Fixed size (static arrays) | Must know size upfront — over/under allocation is painful |
| Wasted memory | Dynamic arrays reserve extra space for future growth |
| Slow search on unsorted arrays | Finding a value without sorting is always O(n) |

---

### When to Pick an Array

```
 Use an array when:
   - You need fast access by index
   - You know the size upfront or it grows from the end
   - You are iterating through all elements
   - Order of elements matters
   - Memory efficiency matters

 Avoid an array when:
   - You are frequently inserting or deleting from the middle
   - You need to search by value constantly → use HashMap
   - You need FIFO order → use a Queue
   - You need LIFO order → use a Stack
   - Size is highly unpredictable and changes a lot
```

---

### How Arrays Compare to What Comes Next

| Situation | Better Choice | Why |
|---|---|---|
| Frequent middle insertions/deletions | Linked List | No shifting — just re-link pointers |
| Search by value in O(1) | HashMap | Direct key-value lookup |
| Last in first out (LIFO) | Stack | Built for this pattern |
| First in first out (FIFO) | Queue | Built for this pattern |
| Hierarchical data | Tree | Parent-child relationships |

---

### The Big Picture
> Every data structure you learn from here is solving a **weakness of the previous one.**
> Arrays are fast at access but slow at insertion → Linked Lists fix that.
> Linked Lists are slow at access → HashMaps fix that.
> And so on.