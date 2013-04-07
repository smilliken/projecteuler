def is_lychrel(n):
    for i in xrange(49):
        n += int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            return False
    return True


def main():
    print(len([n for n in xrange(1, 10000) if is_lychrel(n)]))

if __name__ == '__main__':
    main()
