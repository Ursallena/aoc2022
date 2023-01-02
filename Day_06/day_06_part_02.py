for line in open("data.txt", "r"):
	for c in range(0, len(line)):
		temp = line[c:c + 14]
		temp = set(temp)
		if len(temp) == 14:
			print(c+14)
			break

