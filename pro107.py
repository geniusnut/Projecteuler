import math

data = open('p107_network.txt', 'r')
n = 40
list = []

list_sum = 0
for line in data.readlines():
	arr = line[0:-1].split(',')
	print(arr)
	for i in range(n):
		if arr[i] == '-':
			arr[i] = 100000
		else:
			arr[i] = int(arr[i])
			list_sum += arr[i]
	list.append(arr)
list_sum = list_sum / 2
print(list_sum)
e = []
ans = 0
k = 100000
for i in range(0, n):
	for j in range(0 ,n):
		if k > list[i][j]:
			k = list[i][j]
			q = i
			p = j
e.append(p)
e.append(q)
ans += k
while len(e) < n:
	k = 100000
	for v in e:
		for i in range(n):
			if i in e:
				continue
			if k > list[v][i]:
				k = list[v][i]
				q = i
	ans += k
	e.append(q)
	#print(k, q)
print(list_sum - ans, e)