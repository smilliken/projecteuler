"""
http://projecteuler.net/index.php?section=problems&id=2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def solve():
    total = 0
    n, m = 1, 2
    while n < 4000000:
        if n % 2 == 0:
            total += n
        n, m = m, n + m
    print(total)

if __name__ == '__main__':
    solve()