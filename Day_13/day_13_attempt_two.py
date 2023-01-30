#if both are integers, lower int should be first (or "left")
#if both are lists, compare lists. left should run out of items first
#if int vs list, make int a list with only that one value and compare lists

#ord 0-9 = 48-57
ord_list = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]


def format_input(line_input):	
	temp = []
	list_depth = 0

	for c in line_input:
		if c == "[":
			temp.append([])
			in_last_list = True
			list_depth += 1

		elif ord(c) in ord_list:
			c = int(c)
			temp[-1].append(c)

		elif c == "]" and list_depth >= 2:
			temp[-2].append(temp[-1])
			temp.pop()
			list_depth -= 1

	return temp

def compare_sides(left, right):
	left = format_input(left)
	right = format_input(right)
	
	

	

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

		print("Index: " + str(index) + " | Total Sum: " + str(total_sum))
		index += 1
		left = False
		right = False

		