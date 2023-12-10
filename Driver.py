import En_Cipher as en_Cipher
import De_Cipher as de_Cipher

import random
from collections import Counter
from math import log

chunk_size_chr = 3
primes = []
ent_threshold_chr = 0.95
min_pool_size = 10
chunk_size_key = 9
ent_threshold_key = 0.95
crx_pt = 5

def primesUpto(n):
	for i in range(2, n + 1):
		is_prime = True
		for j in range(2, int(i/2) + 1):
			if(i%j==0):
				is_prime = False
				break
		if is_prime:
		    primes.append(i)

def get_bin(N):
	"""
	generate binary form of N
	upto bit_len places
	"""
	return _get_bin(N, 9)

def _get_bin(N, R):
	"""
	generate binary form of N
	upto R places
	"""
	if type(N) == str:
		N = ord(N[0])
	return format(N, 'b').zfill(R)

def _generate_pool():
	"""
	generates an initial pool
	of bit_len bits children
	"""
	rnd_chars = [get_bin(int(random.random()*26)) for _ in range(16)]
	rnd_primes = []
	for _ in range(16):
		rnd_primes.append(get_bin(primes[int(random.random()*len(primes))]))
	rnd_crx_pt = [int(1 + random.random()*(8)) for _ in range(16)]	
	crx_pool = []
	for parent1, parent2, crx_pt in zip(rnd_chars, rnd_primes, rnd_crx_pt):
		child1 = parent1[:crx_pt] + parent2[crx_pt:]
		child2 = parent2[:crx_pt] + parent1[crx_pt:]
		crx_pool.extend([child1, child2])
	for idx in range(len(crx_pool)):
		crx_pool_el = list(crx_pool[idx])
		crx_pool_el[0], crx_pool_el[8] = crx_pool_el[8], crx_pool_el[0]
		crx_pool[idx] = ''.join(crx_pool_el)
	return crx_pool

def ss_entr_chr(chromosome):
	"""
	computes symbolized shannon entropy
	for a chromosome.
	"""
	def chunks(input, chunk_size_chr):
		return [input[i:i+chunk_size_chr] for i in range(0, len(input), chunk_size_chr)]

	chunks_split = chunks(chromosome, chunk_size_chr)
	chunks_ctr = Counter(chunks_split)
	N = len(chunks_split)
	H = -1/log(N)
	et = 0
	for el in chunks_ctr:
		val = chunks_ctr[el]
		p = val/N
		et += p*log(p)
	H *= et
	return H


def ss_pool(pool):
	"""
	computes symbolized shannon entropy
	for the entire pool
	"""
	ent_pool = []
	for chromosome in pool:
		ent_pool.append(ss_entr_chr(chromosome))
	return ent_pool

def filter_pool(pool):
	"""
	filters pool by selecting chromosomes
	above the entropy value of ent_threshold_chr
	"""
	fltr_pool = []
	for chromosome in pool:
		if ss_entr_chr(chromosome) > ent_threshold_chr:
			fltr_pool.append(chromosome)
	if len(fltr_pool) < min_pool_size:
		return None
	return fltr_pool

def chunks(input, chunk_size_key):
		return [input[i:i+chunk_size_key] for i in range(0, len(input), chunk_size_key)]

def ss_ent_key(key):
	"""
	computes symbolized shannon entropy
	for a key.
	"""
	chunks_split = chunks(key, chunk_size_key)
	chunks_ctr = Counter(chunks_split)
	N = len(chunks_split)
	H = -1/log(N)
	et = 0
	for el in chunks_ctr:
		_, val = el, chunks_ctr[el]
		p = val/N
		et += p*log(p)
	H *= et
	return H


def form_key(pool):
	"""
	merges the individual chromosome
	to form a key
	"""
	return ''.join(pool)

def cvt_key(key):
	"""
	converts binary key into
	letters
	"""
	
	key_chunks = chunks(key, chunk_size_key)
	return ''.join([chr(int(el, 2)) for el in key_chunks])
	

def create_key():
	primesUpto(100)
	ent_val = 0
	while ent_val < ent_threshold_key:		
		pool = _generate_pool()
		pool = filter_pool(pool)
		if pool == None:
			continue
		key = form_key(pool)
		ent_val = ss_ent_key(key)
	print("Key in binary -> {}".format(key))
	print("Entropy Value -> {}".format(ent_val))
	return key, cvt_key(key)

Text = "newton"
print("x---------------------------------------------KeyGeneration------------------------------------------------------x")
key, fmt_key = create_key()
Key = list(fmt_key)
print("key ->" + fmt_key)
re_Fact = 2
print(f"Original Plain Text:\n{Text}")
print()
print("x---------------------------------------------Encryption------------------------------------------------------x")
Cipher = en_Cipher.encrypt(Text, re_Fact, Key)
print(f"\nThe Cipher text is:\n{Cipher}")
print("x---------------------------------------------Decryption------------------------------------------------------x")
Plain = de_Cipher.decrypt(Cipher, Key)
print(f"\nThe Original Plain text is:\n{Plain}")
