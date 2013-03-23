
def main():
    n, b = 1, 1
    while n < 10 ** 12:
        n, b = (4 * b + 3 * n - 3, 3 * b + 2 * n - 2)
    print(b)

if __name__ == '__main__':
    main()
