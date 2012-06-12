def lower_chars():
    for x in xrange(ord('a'), ord('z')):
        yield x

def decrypt(ciphertext, key):
    for idx, val in enumerate(ciphertext):
        yield(chr(val ^ key[idx % len(key)]))

def main():
    ciphertext = [int(char) for char in open('cipher1.txt').read().split(',')]
    keys = [(c1, c2, c3) for c1 in lower_chars() for c2 in lower_chars() for c3 in lower_chars()]
    plaintexts = [''.join(decrypt(ciphertext, key)) for key in keys]
    plaintext = max(plaintexts, key=lambda plain: plain.count(' and '))
    print(sum([ord(char) for char in plaintext]))

if __name__ == '__main__':
    main()