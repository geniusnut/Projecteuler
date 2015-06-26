import math

def calcFac(n):
	tmp = 0
	int mid = math.sqrt(n) + 1
	for i in range (2, mid):
		if 
	return tmp

ans = 0;

for n in range(1, 2):
	k = 10**n;
	for i in range(n + 1):
		for j in range(n + 1):
			q = k/2**i/5**j + k
			ans += calcFac(q)
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			q = k/2**i + k/5**i
			ans += calcFac(q)

print(ans)


