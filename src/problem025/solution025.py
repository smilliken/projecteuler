def fibs():
    n, m = 1, 1
    while True:
        yield n
        n, m = m, n + m


def main():
    for n, fib in enumerate(fibs(), 1):
        if fib >= 10 ** 999:
            print(n)
            break

if __name__ == '__main__':
    main()
