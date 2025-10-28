def sum_linear(n: int) -> int:
    # O(n)
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_formula(n: int) -> int:
    # O(1)
    return n * (n + 1) // 2