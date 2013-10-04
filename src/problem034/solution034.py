def factorial(n):
    prod = 1
    for i in xrange(1, n + 1):
        prod *= i
    return prod

def main():
    print(sum([n for n in xrange(3, factorial(9))
        if sum([factorial(int(d)) for d in str(n)]) == n]))

if __name__ == '__main__':
    main()
