import math


def is_pentagonal(num):
    idx = (1 + math.sqrt(1 + 24 * num)) / 6
    return idx >= 0 and int(idx) == idx


def pentagonal(idx):
    return idx * (3 * idx - 1) / 2


def main():
    for k in xrange(2, 2 ** 16):
        for j in xrange(k - 1, 1, -1):
            p_k = pentagonal(k)
            p_j = pentagonal(j)
            if is_pentagonal(p_k - p_j) and is_pentagonal(p_k + p_j):
                print(p_k - p_j)
                return

if __name__ == '__main__':
    main()
