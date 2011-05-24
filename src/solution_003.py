"""
http://projecteuler.net/index.php?section=problems&id=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def solve():
    n = 600851475143
    p = 1
    while n > 1:
        p += 1
        while n % p == 0:
            n /= p
    print(p)

if __name__ == '__main__':
    solve()