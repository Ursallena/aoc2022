class directory:
	def __init__(self, name):
		self.name = name
		self.file_sizes = 0
		self.internal_directorys = []

	def add_file(self, file_size):
		self.file_sizes += int(file_size)

	def add_directory(self, to_add):
		if not to_add in self.internal_directorys:
			self.internal_directorys.append(to_add)

	def return_total_size(self):
		return self.file_sizes

	def return_name(self):
		return self.name

	def __repr__(self):
		return self.name

	def __str__(self):
		return self.name

	def return_directorys(self):
		return (self.internal_directorys)

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
				temp_debug = current_location[-1]

				for d in directory_list:
					if d.return_name() == line[-1]:
						current_location.append(d)

	elif line[0] == "dir":
		directory_list.append(directory(line[1]))
		current_location[-1].add_directory(directory_list[-1])

	elif not line[0] == "$":
		for l in current_location:
			l.add_file(line[0])

total_sum_of_dir = 0
for d in directory_list:
	size = d.return_total_size()
	if size < 100000:
		total_sum_of_dir += size	

print(total_sum_of_dir)
