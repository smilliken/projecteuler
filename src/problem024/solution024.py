import itertools


def main():
    print(''.join(sorted(itertools.permutations('0123456789', 10))[999999]))

if __name__ == '__main__':
    main()
