for line in open("data.txt", "r"):
	for c in range(0, len(line)):
		temp = line[c:c + 4]
		temp = set(temp)
		if len(temp) == 4:
			print(c+4)
			break

