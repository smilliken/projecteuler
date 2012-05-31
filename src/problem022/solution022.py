
def alphabetic_value(text):
    return sum([ord(char) - ord('A') + 1 for char in text.upper()])

def main():
    names = sorted([name.strip('"') for name in open('names.txt').read().split(',')])
    print(sum([(idx + 1) * alphabetic_value(name) for idx, name in enumerate(names)]))

if __name__ == '__main__':
    main()