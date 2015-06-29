import math

def calcFac(n):
	tmp = 0

	factorDict = dict()
	i = 2
	while i * i <= n:
		while n%i == 0:
			n = n / i
			if i in factorDict:
				factorDict[i] += 1
			else:
				factorDict[i] = 1
		i = i + 1
	if n != 1:
		if n in factorDict:
			factorDict[n] += 1
		else:
			factorDict[n] = 1
	print(factorDict)
	k = 1
	for i in factorDict:
		k *= (factorDict[i] + 1)
	return k

ans = 0;

for n in range(1, 10):
	k = 10**n;
	for i in range(n + 1):
		for j in range(n + 1):
			q = k/2**i/5**j + k
			ans += calcFac(q)
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			q = k/(2**i) + k/(5**j)
			ans += calcFac(q)

print(ans)


