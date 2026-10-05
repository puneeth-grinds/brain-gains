# 🧠 Brain Gains — DSA Interview Prep

Structured DSA prep — concepts, patterns & LeetCode solutions organized by topic and difficulty.

**Target:** Product-based companies (non-FAANG)
**Language:** Python
**Approach:** Learn concept → Easy problems → Medium problems → Next topic

---

## 📁 Folder Structure

```
brain-gains/
│
├── arrays/
│   ├── theory/
│   │   ├── arrays_fundamentals.md
│   │   ├── arrays_operations.md
│   │   ├── arrays_complexity.md
│   │   ├── arrays_types.md
│   │   └── arrays_pros_cons.md
│   ├── easy/
│   │   ├── two_sum.py
│   │   ├── move_zeroes.py
│   │   ├── remove_duplicates.py
│   │   ├── remove_element.py
│   │   ├── merge_sorted_array.py
│   │   ├── best_time_to_buy_and_sell_stock.py
│   │   ├── single_number.py
│   │   └── plus_one.py
│   ├── medium/
│   │   ├── maximum_subarray.py
│   │   ├── container_with_most_water.py
│   │   ├── three_sum.py
│   │   ├── product_of_array_except_self.py
│   │   ├── maximum_product_subarray.py
│   │   └── find_minimum_in_rotated_sorted_array.py
│   └── notes.md
│
├── strings/
├── linked_lists/
├── stacks_and_queues/
├── trees/
├── graphs/
├── dynamic_programming/
│
└── README.md
```

---

## 📊 Progress Tracker

### Arrays

#### Theory ✅
| Block | Topic | Status |
|---|---|---|
| Block 1 | Fundamentals — what an array is, memory layout, static vs dynamic | ✅ Done |
| Block 2 | Operations — access, traversal, insertion, deletion | ✅ Done |
| Block 3 | Complexity — time and space for every operation | ✅ Done |
| Block 4 | Types — 1D, 2D, jagged arrays | ✅ Done |
| Block 5 | Pros, cons & when to use | ✅ Done |

#### Easy Problems ✅
| # | Problem | Pattern | Status |
|---|---|---|---|
| 1 | Two Sum | Nested loops | ✅ Solved |
| 283 | Move Zeroes | Position pointer | ✅ Solved |
| 26 | Remove Duplicates from Sorted Array | Position pointer | ✅ Solved |
| 27 | Remove Element | Position pointer | ✅ Solved |
| 88 | Merge Sorted Array | Three pointers from back | ✅ Solved |
| 121 | Best Time to Buy and Sell Stock | Running minimum | |
| 136 | Single Number | XOR | ✅ Solved |
| 66 | Plus One | Carry logic | ✅ Solved |

#### Medium Problems 🔄
| # | Problem | Pattern | Status |
|---|---|---|---|
| 53 | Maximum Subarray | Kadane's Algorithm |  ✅ Solved |
| 11 | Container With Most Water | Two Pointers | ⬜ Todo |
| 15 | 3Sum | Two Pointers + Sorting | ⬜ Todo |
| 238 | Product of Array Except Self | Prefix Sum | ⬜ Todo |
| 152 | Maximum Product Subarray | Kadane's Extended | ⬜ Todo |
| 153 | Find Minimum in Rotated Sorted Array | Binary Search | ⬜ Todo |

---

## 🔑 Key Patterns Learned So Far

| Pattern | Problems |
|---|---|
| Position Pointer | Move Zeroes, Remove Duplicates, Remove Element |
| Three Pointers | Merge Sorted Array |
| Running Minimum | Best Time to Buy and Sell Stock |
| XOR | Single Number |
| Carry Logic | Plus One |
| Kadane's Algorithm | Maximum Subarray |

---

## 📝 How Each Solution File is Structured

```
# Problem Title
# Difficulty | Link

# Problem Statement
# Examples + Constraints

# Approach — pattern used + complexity

# Solution

# Test Cases

# What I Learned
```