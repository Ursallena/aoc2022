#if both are integers, lower int should be first (or "left")
#if both are lists, compare lists. left should run out of items first
#if int vs list, make int a list with only that one value and compare lists

#ord 0-9 = 48-57
ord_list = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]

def format_input(line_input):
	temp = False
	list_depth = 0
	list_index = 0

	for c in line_input:
		print(temp)
		if c == "[":
			if temp == False:
				temp = []
			elif list_depth >= 2:
				temp[list_depth - 2].append([])
			else:
				temp.append([])

			list_depth += 1

		elif ord(c) in ord_list:
			c = int(c)
			if temp == False:
				temp = c
			elif list_depth >= 2:
				temp[list_depth - 2].append(c)
			else:
				temp.append(c)

		elif c == "]":
			list_depth -= 1

	return temp


def compare_sides(left, right):
	left = format_input(left)
	right = format_input(right)
	print(left)
	print(right)

left = False
right = False
index = 1
total_sum = 0
for line in open("data.txt", "r"):

	if line == "":
		pass
	elif not left:
		left = line.strip()
	elif not right:
		right = line.strip()
	
	if left and right:
		if compare_sides(left, right):
			total_sum += index
		index += 1
		left = False
		right = False

		print("Index: " + str(index) + " | " + str(total_sum))