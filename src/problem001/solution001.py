def solve():
    total = sum((i for i in xrange(1000) if i % 3 == 0 or i % 5 == 0))
    print(total)

if __name__ == '__main__':
    solve()