def main():
    print(sum([n for n in xrange(1, 1000001)
        if str(n) == str(n)[::-1] and bin(n)[2:] == bin(n)[2:][::-1]]))

if __name__ == '__main__':
    main()
