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