
def primes():
	ps = []
	i = 2
	
	while i < 2e3:
		for p in (p for p in ps if p <= i**.5):
			if not i % p:
				break
		else:
			ps.append(i)
			print(i)
		i += 1

primes()
