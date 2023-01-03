class files:
	def __init__(self, name, size):
		self.name = name
		self.size = int(size)

	def return_name(self):
		return self.name

	def return_size(self):
		return self.size

class directory:
	def __init__(self, name, path):
		self.name = name
		self.path = path
		self.files = []
		self.folders = []

	def add_file(self, file):
		self.files.append(file)

	def return_files(self):
		if self.files == []:
			return False
		return self.files

	def add_folder(self, folder):
		self.folders.append(folder)

	def return_folders(self):
		if self.folders == []:
			return False
		return self.folders

	def total_size(self):
		total_sum = 0

		for file in self.files:
			total_sum += file.return_size()

		for folder in self.folders:
			total_sum += folder.total_size()

		return total_sum

	def return_path(self):
		return self.path

	def return_location(self):
		if not self.name == "/":
			return self.path + "\\" + self.name
		return self.path + self.name

	def return_parent_folder(self, d_list):
		for d in d_list:
			if self.return_path() == d.return_location():
				return d

	def return_name(self):
		return self.name

	def __repr__(self):
		return self.return_location()

directory_list = [directory("/", "~")]
current_location = directory_list[-1]

for line in open("data.txt", "r"):
	line = line.strip().split(" ")
	
	if line[0] == "$":
		if line[1] == "cd":
			if line[2] == "..":
				current_location = current_location.return_parent_folder(directory_list)
			elif line[2] == "/":
				pass
			else:
				for d in current_location.return_folders():
					if d.return_name() == line[2]:
						current_location = d

	elif line[0] == "dir":
		directory_list.append(directory(line[1], current_location.return_location()))
		current_location.add_folder(directory_list[-1])

	else:
		current_location.add_file(files(line[1], line[0]))

total_system_size = 70000000 ## 70 million
required_space = 30000000 ## 30 million
used_space = directory_list[0].total_size()
free_space = total_system_size - used_space
space_difference = required_space - free_space ## how much we need to free

d_to_delete = [] ## potential directories that would free up enough space

for d in directory_list:
	if d.total_size() > space_difference:
		d_to_delete.append(d)

smallest_to_delete = d_to_delete[0].total_size()
for d in d_to_delete:
	if d.total_size() < smallest_to_delete:
		smallest_to_delete = d.total_size()

print(smallest_to_delete)
