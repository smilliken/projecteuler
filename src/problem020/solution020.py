import operator

def main():
    print(sum([int(char) for char in str(reduce(operator.mul, range(1, 100)))]))

if __name__ == '__main__':
    main()