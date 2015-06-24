import math;

n = 51;
total = 0;

def calc(xq,yq,xp,yp):
	xpq = xq - xp;
	ypq = yq - yp;
	sum1 = xpq*xp + ypq*yp;
	sum2 = xpq*xq + ypq*yq;
	return sum1*sum2 == 0;
for xq in range(0, n):
	for yq in range(0, n):
		if (xq==0) and (yq==0):
			continue;
		for xp in range(0, n):
			for yp in range(0, n):
				if (xp==0) and (yp==0):
					continue;
				if (xp == xq) and (yp == yq):
					continue;
				if calc(xq,yq,xp,yp):
					#print(xq,yq, xp,yp)
					total += 1

print(total /2+ (n-1)**2)				
