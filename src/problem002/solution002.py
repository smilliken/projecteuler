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