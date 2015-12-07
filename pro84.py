from random import randint
pos = 0
cc_pos = 0
ch_pos = 0
rolls = 10000000
tiles = [0 for i in range(40)]


def CC():
    global pos
    global cc_pos
    if (cc_pos == 0): pos = 0
    if cc_pos == 1: pos = 10
    cc_pos += 1
    if cc_pos == 16: cc_pos = 0

def CH():
    global pos
    global ch_pos
    if (ch_pos == 0) : pos = 0 
    elif ch_pos == 1 : pos = 10
    elif ch_pos == 2 : pos = 11
    elif ch_pos == 3 : pos = 24
    elif ch_pos == 4 : pos = 39
    elif ch_pos == 5 : pos = 5
    elif ch_pos == 6 or ch_pos == 7:
        if (pos == 7) : pos = 15
	if (pos == 22) : pos = 25
	if (pos == 36) : pos = 5
    elif ch_pos == 8 : 
    	if (pos == 7) : pos = 12
	if (pos == 22) : pos = 28
	if (pos == 36) : pos = 12
    elif ch_pos == 9 : pos -= 3
    ch_pos += 1
    if ch_pos == 16: ch_pos = 0

double = 0
if __name__ == "__main__":
    for i in range(rolls):
        dice1 = randint(1, 4)
        dice2 = randint(1, 4)
	if (dice1 == dice2):
	    double += 1
	else :
	    double = 0
	if (double == 3):
	    double = 0
	    pos = 10
	    tiles[pos] += 1
	    continue

        pos = (dice1 + dice2 + pos) % 40
        if (pos == 2 or  pos == 17 or pos == 33) : CC()
	if (pos == 7 or pos == 22 or pos == 36) : CH()
	if (pos == 30): pos = 10
        tiles[pos] += 1
    print(tiles)
    tmp = sorted(tiles)
    print(tmp)
    for i in range(40):
    	if (tmp[39] == tiles[i]): print(tmp[39], i)
    	if (tmp[38] == tiles[i]): print(tmp[38], i)
    	if (tmp[37] == tiles[i]): print(tmp[37], i)



