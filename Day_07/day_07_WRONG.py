class files:
	def __init__(self, name, size):
		self.name = name
		self.size = int(size)

	def return_name(self):
		return self.name

	def return_size(self):
		return self.size

class directory:
	def __init__(self, name):
		self.name = name
		self.files = []
		self.internal_directorys = []

	def add_file(self, file):
		self.files.append(file)

	def add_directory(self, to_add):
		if not to_add in self.internal_directorys:
			self.internal_directorys.append(to_add)

	def return_total_size(self):
		total_sum = 0

		for file in self.files:
			total_sum += file.return_size()

		for directory in self.internal_directorys:
			total_sum += directory.return_total_size()

		return total_sum

	def return_name(self):
		return self.name

	def __repr__(self):
		return self.name

	def __str__(self):
		return self.name

	def return_directorys(self):
		return self.internal_directorys

def direct_tree(home):
	print(home.return_name(), home.return_total_size())
	for d in home.return_directorys():
		direct_tree_print(d, "")

def direct_tree_print(direct, to_print):
	print(to_print + "| " + direct.return_name() + " " + str(direct.return_total_size()))
	for d in direct.return_directorys():
		direct_tree_print(d, to_print + "|")


directory_list = [directory("/")]
current_location = [directory_list[0]]

for line in open("data.txt", "r"):
	line = line.strip().split(" ")
	if line[0] == "$":
		if line[1] == "cd":
			if line[-1] == "..":
				current_location.pop()
			elif line[-1] == "/":
				current_location = [current_location[0]]
			else:
				for d in directory_list:
					if d.return_name() == line[-1]:
						current_location.append(d)

	elif line[0] == "dir":
		directory_list.append(directory(line[1]))
		current_location[-1].add_directory(directory_list[-1])

	else:
		current_location[-1].add_file(files(line[1], line[0]))
		print(line)
		print(current_location[-1])

total_sum_of_dir = 0
for d in directory_list:
	size = d.return_total_size()
	if size < 100000:
		total_sum_of_dir += size

#direct_tree(directory_list[0])
print(total_sum_of_dir)
