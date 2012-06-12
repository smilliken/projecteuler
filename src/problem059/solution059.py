import itertools
import string

def decrypt(ciphertext, key):
    for idx, val in enumerate(ciphertext):
        yield(chr(val ^ ord(key[idx % len(key)])))

def main():
    ciphertext = [int(char) for char in open('cipher1.txt').read().split(',')]
    keys = itertools.product(string.ascii_lowercase, repeat=3)
    plaintexts = [''.join(decrypt(ciphertext, key)) for key in keys]
    plaintext = max(plaintexts, key=lambda plain: plain.count(' and '))
    print(sum([ord(char) for char in plaintext]))

if __name__ == '__main__':
    main()