def factorial_rec(n: int) -> int:
    """
    Compute n! (factorial) using recursion.

    Args:
        n: Non-negative integer.

    Returns:
        The factorial of n.

    Raises:
        ValueError: If n is negative.

    Examples:
        >>> factorial_rec(5)
        120
        >>> factorial_rec(0)
        1
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)


def factorial_iter(n: int) -> int:
    """
    Compute n! (factorial) iteratively.

    Args:
        n: Non-negative integer.

    Returns:
        The factorial of n.

    Raises:
        ValueError: If n is negative.

    Examples:
        >>> factorial_iter(5)
        120
        >>> factorial_iter(1)
        1
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


def fib_iter(n: int) -> int:
    """
    Compute the n-th Fibonacci number iteratively (0-indexed).

    Definition:
        F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n >= 2

    Args:
        n: Non-negative integer index.

    Returns:
        The n-th Fibonacci number.

    Raises:
        ValueError: If n is negative.

    Examples:
        >>> fib_iter(0)
        0
        >>> fib_iter(1)
        1
        >>> fib_iter(6)
        8
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b
