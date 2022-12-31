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


highest_calories_list = [0, 0, 0]
for elf in elf_list:
	if elf.return_calories() > highest_calories_list[0]:
		highest_calories_list[2] = highest_calories_list[1]
		highest_calories_list[1] = highest_calories_list[0]
		highest_calories_list[0] = elf.return_calories()
	elif elf.return_calories() > highest_calories_list[1]:
		highest_calories_list[2] = highest_calories_list[1]
		highest_calories_list[1] = elf.return_calories()
	elif elf.return_calories() > highest_calories_list[2]:
		highest_calories_list[2] = elf.return_calories()

sum_of_calories = 0
for i in highest_calories_list:
	sum_of_calories += i


print(sum_of_calories)