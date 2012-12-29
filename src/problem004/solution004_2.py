def main():
    candidates = []
    for x in xrange(100, 999):
        for y in xrange(100, 999):
            if str(x * y) == str(x * y)[::-1]:
                candidates.append(x * y)
    return max(candidates)

if __name__ == '__main__':
    print(main())