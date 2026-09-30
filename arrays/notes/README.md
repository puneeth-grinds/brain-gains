## Array - Fundamentals

- Array is a collection of elements stored in a sequence and is identified by an index
```
- Seat No →   1      2      3      4      5
          ┌──────┬──────┬──────┬──────┬──────┐
          │ John │ Mary │ Alex │  --  │ Sara │
          └──────┴──────┴──────┴──────┴──────┘
```
- each element sits next to each other in the memory and are not scattered and this gives you O(1) 
- Computer does not search for the number instead calculcates the address and goes there in one step
- Example: 
Address of element at index i = Base Address + (i × size of each element)

Example:

Base address = 1000
Each element = 1 byte

Index 0 → 1000 + (0 × 1) = 1000  
Index 3 → 1000 + (3 × 1) = 1003  
Index 4 → 1000 + (4 × 1) = 1004  