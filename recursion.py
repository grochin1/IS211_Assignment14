
def fibonacci(n):
	if n < 3:
		return 1
	return fibonacci(n-1) + fibonacci(n-2)

def gcd(a, b):
	if not a:
		return b
	if not b:
		return a
	if a < b:
		a, b = b, a
	return gcd(a%b, b)

def compareTo(s1, s2):
	if not s1:
		return -1 if s2 else 0
	if not s2:
		return 1 if s1 else 0
	if s1[0] < s2[0]:
		return -1
	if s1[0] > s2[0]:
		return 1
	return compareTo(s1[1:], s2[1:])
