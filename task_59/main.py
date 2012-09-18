from itertools import cycle

ciphered = map(int, open('cipher1.txt', 'r').read().split(','))

key_range = range(ord('a'), ord('z') + 1)

possible_keys = [filter(lambda x: chr(x ^ c).isalpha(), key_range) for c in ciphered]

def intersect(a, b):
	return set(a).intersection(b)

possible_keys = [reduce(intersect, lst[1:], lst[0]) for lst in [filter(len, possible_keys[i::3]) for i in range(3)]]

print [map(chr, x) for x in possible_keys]
	
def decrypt(text, key):
	key = map(ord, list(key))
	return ''.join(map(lambda x: chr(x[0] ^ x[1]), zip(text, cycle(key))))
	
print decrypt(ciphered, 'god')