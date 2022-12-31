def format_elf(e):
	if e[1] < e[0]:
		temp = e[0]
		e[0] = e[1]
		e[1] = temp
		return e
	else:
		return e

def compare_elfs(e1, e2):
	if e1[0] >= e2[0] and e1[1] <= e2[1]:
		return True
	elif e1[0] <= e2[0] and e1[1] >= e2[1]:
		return True
	else:
		return False


total_overlap = 0
for line in open("data.txt", "r"):
	if "\n" == line[-1]:
		line = line[:-1]


	line = line.split(",")
	first_elf = format_elf(line[0].split("-"))
	second_elf = format_elf(line[1].split("-"))
	first_elf[0] = int(first_elf[0])
	first_elf[1] = int(first_elf[1])
	second_elf[0] = int(second_elf[0])
	second_elf[1] = int(second_elf[1])

	if compare_elfs(first_elf, second_elf):
		total_overlap += 1


print(total_overlap)