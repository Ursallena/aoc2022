
def char_to_val(c):
	if c.isupper():
		return char_to_val(c.lower()) + 26
	else:
		return ord(c) - 96

total_sum = 0
for line in open("data.txt", "r"):
	if "\n" == line[-1]:
		line = line[:-1]
	temp = []
	half_len = len(line) // 2
	
	temp.append(line[:half_len])
	temp.append(line[half_len:])


	for char in temp[0]:
		if char in temp[1]:
			total_sum += char_to_val(char)
			print(char)
			print(char_to_val(char))
			break

print(total_sum)
	
