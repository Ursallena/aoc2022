class monkey():
	def __init__(self):
		self.items = []
	
	def add_data(self, operation, operation_type, test, if_true, if_false):
		self.operation = int(operation)
		self.operation_type = operation_type
		self.test = int(test)
		self.if_true = int(if_true)
		self.if_false = int(if_false)
		self.inspection_counter = 0

	def add_items(self, item):
		if type(item) == type(""):
			if item[-1] == ",":
				item = item[:-1]
		self.items.append(int(item))

	def print_items(self):
		data = ""
		for i in self.items:
			data += str(i) + ", "

		return data[:-2]

	def operation_on_item(self, modulo_number):
		if self.operation_type == "Multiply":
			self.items[0] = self.items[0] * self.operation
		elif self.operation_type == "Square":
			self.items[0] = self.items[0] * self.items[0]
		elif self.operation_type == "Add":
			self.items[0] = self.items[0] + self.operation

		
		self.items[0] = self.items[0] % modulo_number
		
		self.inspection_counter += 1


	def inspect_item(self, monkey_list):
		if self.items[0] % self.test == 0:
			monkey_list[self.if_true].add_items(self.items.pop(0))
		else:
			monkey_list[self.if_false].add_items(self.items.pop(0))

	def return_items(self):
		return self.items

	def return_inspection_counter(self):
		return self.inspection_counter


	def __repr__(self):
		return self.print_items()

	def __str__(self):
		return self.print_items()


monkey_list = [monkey()]
data = [False, False, False, False, False]

for line in open("data.txt", "r"):
	line = line.strip().split(" ")

	if line[0] == "":
		continue		

	elif line[0] == "Starting":
		for i in range(2, len(line)):
			monkey_list[-1].add_items(line[i])

	elif line[0] == "Operation:":
		if line[-1] == "old":
			data[0] = 0
			data[1] = "Square"
		else:
			data[0] = line[-1]
			if line[-2] == "*":
				data[1] = "Multiply"
			elif line[-2] == "+":
				data[1] = "Add"

	elif line[0] == "Test:":
		data[2] = line[-1]

	elif line[1] == "true:":
		data[3] = line[-1]

	elif line[1] == "false:":
		data[4] = line[-1]
		
		monkey_list[-1].add_data(data[0], data[1], data[2], data[3], data[4])

		monkey_list.append(monkey())
		data = [False, False, False, False, False]

modulo_number = 1
for m in range(0, len(monkey_list) - 1):
	print(str(m) + ". " + str(monkey_list[m]))
	modulo_number = modulo_number * monkey_list[m].test


for i in range(0, 10000):
	print("~~~~~~~~~~~~~~~~~")
	for m in range(0, len(monkey_list) - 1):
		while not monkey_list[m].return_items() == []:
			monkey_list[m].operation_on_item(modulo_number)
			monkey_list[m].inspect_item(monkey_list)

		
	for m in range(0, len(monkey_list) - 1):
		print(str(m) + ". " + str(monkey_list[m]))

print("~~~~~~~~~~~~~~~~~")
largest_inspect = 0
second_largest_inspect = 0
for m in range(0, len(monkey_list) - 1):
	temp = monkey_list[m].return_inspection_counter()

	if temp > largest_inspect:
		second_largest_inspect = largest_inspect
		largest_inspect = temp
	elif temp > second_largest_inspect:
		second_largest_inspect = temp

	print(str(temp))

print("~~~~~~~~~~~~~~~~~")
print(str(largest_inspect * second_largest_inspect))