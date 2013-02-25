
def main():
    total = sum([i ** i for i in xrange(1, 1001)])
    print(str(total)[-10:])

if __name__ == '__main__':
    main()
