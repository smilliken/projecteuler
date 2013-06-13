import itertools
from operator import mul


def main():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    print(len([
        1 for candidate in
        itertools.product(*[range(int(200 / coin) + 1) for coin in coins]) if
        sum(map(lambda x: mul(*x), itertools.izip(candidate, coins))) == 200]))

if __name__ == '__main__':
    main()
