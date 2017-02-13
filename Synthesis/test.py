def recur(index, item, smtbdd, nvars, bdd):
	if(smtbdd[index][0] == -1):
		while(len(item) < nvars+1):
			item.append('X')
		item.append(smtbdd[index][1])
		bdd.append(item)
		print bdd
		item = []
	else:
		left = smtbdd[index][1]
		right = smtbdd[index][2]
		v = smtbdd[index][0]
		recur_left(left, item, smtbdd, nvars, bdd, v)
		recur_right(right, item, smtbdd, nvars, bdd, v)

def recur_left(index, item, smtbdd, nvars, bdd, v):
	while(len(item) < 1+v):
		item.append('X')
	item.append(0)
	recur(index, item, smtbdd, nvars, bdd)

def recur_right(index, item, smtbdd, nvars, bdd, v):
	while(len(item) < 1+v):
		item.append('X')
	item.append(1)
	recur(index, item, smtbdd, nvars, bdd)

f = open("test.dfa")
flag = 0
smtbdd = []
for line in f.readlines():
	if(flag == 0):
		if "number of variables" in line:
			nvars = int(line.split(":")[1])
		if "states" in line:
			nstates = line.split(":")[1]
		if "initial" in line:
			init = line.split(":")[1]
		if "bdd nodes" in line:
			nodes = line.split(":")[1]
		if "final"in line:
			line = line.strip().split(" ")
			final = []
			i = 1
			while(i < len(line)):
				if(line[i] == '1'):
					final.append(i-1)
				i = i + 1
		if "behaviour" in line:
			line = line.split(" ")
			behaviour = []
			i = 1
			while(i < len(line)):
				behaviour.append(line[i])
				i = i + 1
		if "bdd:" in line:
			flag = 1
	else:
		if "end" in line:
			break
		line = line.strip().split(" ")
		item = []
		for it in line:
			item.append(int(it))
		smtbdd.append(item)

i = 0
while(i < 6):
	index = int(behaviour[i])
	bdd = []
	item = []
	item.append(i)
	recur(index, item, smtbdd, nvars, bdd)
	print bdd
	i = i + 1
