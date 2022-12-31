class elfs:
	def __init__(self):
		self.total_calories = 0

	def add_calories(self, calories):
		self.total_calories += int(calories)

	def return_calories(self):
		return self.total_calories

	def __str__(self):
		return str(self.total_calories)


elf_list = [elfs()]
for line in open("data.txt", "r"):
	line = line[:-1]
	
	if line == "":
		elf_list.append(elfs())
	else:
		elf_list[-1].add_calories(line)


highest_calories = 0
highest_calories_index = 0
index = 0
for elf in elf_list:
	if elf.return_calories() > highest_calories:
		highest_calories = elf.return_calories()
		highest_calories_index = index
	index += 1
	print(elf)

print(highest_calories)