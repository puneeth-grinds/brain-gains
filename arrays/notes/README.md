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
| Flexibility | ❌ Cannot resize | ✅ Resizes automatically |
| Example | Arrays in C/Java | Lists in Python |

> Python lists are **dynamic arrays** under the hood — you never worry about size.

---

## Key Trade-off
> Arrays give you **speed of access O(1)** in exchange for **flexibility in the middle.**
> Since elements are contiguous in memory, inserting or deleting in the middle requires shifting all surrounding elements — which is expensive.