class column:
	def __init__(self):
		self.data = []

	def put_on_top(self, containers):
		self.data = self.data + containers

	def put_on_bottom(self, container):
		self.data.insert(0, container)

	def remove_from_top(self, amount):
		temp = self.data[len(self.data) - amount:]
		self.data = self.data[:len(self.data) - amount]
		return temp

	def return_data(self):
		return self.data

	def return_top_container(self):
		return self.data[-1]


column_list = []
for i in range(0, 9):
	column_list.append(column())

for line in open("data.txt", "r"):
	if "[" in line:
		for i in range(0, (len(line) // 4)):
			temp = line[i * 4:i * 4 + 3]

			if temp[0] == "[":
				column_list[i].put_on_bottom(temp)


	if line[0] == "m":
		temp = line.strip().split(" ")
		removed_containers = column_list[int(temp[3]) - 1].remove_from_top(int(temp[1]))
		column_list[int(temp[-1]) - 1].put_on_top(removed_containers)


for column in column_list:
	print(column.return_top_container())

