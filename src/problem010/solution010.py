import math

def isprime(n):
	for a in xrange(2, int(math.sqrt(n))):
		if n % a == 0:
			return False
	return True

def solve():
	# TODO: would be much faster to just use a sieve and sum at the end.
	return sum((x for x in xrange(2000000) if isprime(x)))

if __name__ == '__main__':
	print(solve())
