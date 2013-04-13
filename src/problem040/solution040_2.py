def gen_digits():
    for i in xrange(1, 2**32):
        for char in str(i):
            yield int(char)


def main():
    indicies = set([10 ** i for i in xrange(7)])
    max_index = max(indicies)
    prod = 1
    for n, d in enumerate(gen_digits(), start=1):
        if n in indicies:
            prod *= d
        if n > max_index:
            break
    print(prod)

if __name__ == '__main__':
    main()
