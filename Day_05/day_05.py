class column:
	def __init__(self):
		self.data = []


column_list = []
for i in range(0, 9):
	column_list.append(column())

for line in open("data.txt", "r"):
	row = []
	for i in range(0, (len(line) // 4)):
		row.append(line[i * 4:i * 4 + 3])

	print(row)


