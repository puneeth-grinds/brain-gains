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