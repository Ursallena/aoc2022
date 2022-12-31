import time
start_time = time.time()


def char_to_val(c):
	if c.isupper():
		return char_to_val(c.lower()) + 26
	else:
		return ord(c) - 96

total_sum = 0
temp = []
for line in open("data.txt", "r"):
	if "\n" == line[-1]:
		line = line[:-1]
	temp.append(set(line))

	if len(temp) == 3:
		for char in temp[0]:
			if char in temp[1] and char in temp[2]:
				total_sum += char_to_val(char)
				break
		temp = []


print(total_sum)


print("--- %s seconds ---" % (time.time() - start_time))