# Big-O Cheatsheet (Practical)

- Avoid nested scans over 1e5+ unless necessary
- Watch hidden sorts: any `.sort()` turns to O(n log n)
- Prefer maps/sets for membership over lists (O(1) vs O(n))
- Heap for top-K when K << N
