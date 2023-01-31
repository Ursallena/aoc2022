#if both are integers, lower int should be first (or "left")
#if both are lists, compare lists. left should run out of items first
#if int vs list, make int a list with only that one value and compare lists

#ord 0-9 = 48-57
ord_list = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]

# Actually in python there's a really easy way to parse the input...
# ...perhaps you shoudl EVALuate your options...
## I'm committed to making things difficult for myself, so it stays!
def format_input(line_input):	
	temp = []
	list_depth = 0
	long_int = False

	for i in range(0, len(line_input)):
		c = line_input[i]
		if c == "[":
			temp.append([])
			in_last_list = True
			list_depth += 1

		elif ord(c) in ord_list and long_int == False:
			temp_int = ""
			loop_index = 1
			while not c in [",", "]"]:
				temp_int += c
				c = line_input[i + loop_index]
				loop_index += 1

			long_int = True
			temp[-1].append(int(temp_int))

		elif c == "]" and list_depth >= 2:
			temp[-2].append(temp[-1])
			temp.pop()
			list_depth -= 1
			long_int = False

		elif c == ",":
			long_int = False

	return temp

def compare_lists(left, right):
	list_type = type([])
	int_type = type(0)
	temp = "Null"

	if left == [] and right == []:
		return "Null"

	elif left == [] and not right == []:
		return True

	elif not left == [] and right == []:
		return False

	while not left == [] and not right == []:
		left_type = type(left[0])
		right_type = type(right[0])

		if left_type == list_type and right_type == list_type:
			temp = compare_lists(left[0], right[0])
			
		elif left_type == list_type and right_type == int_type:
			temp = compare_lists(left[0], [right[0]])

		elif left_type == int_type and right_type == list_type:
			temp = compare_lists([left[0]], right[0])

		else: #Should only get to this point if both are ints
			if left[0] < right[0]:
				return True

			elif left[0] > right[0]:
				return False

			else:
				return "Null"


		if not temp == "Null":
				return temp

	return "Null"




def compare_sides(left, right):
	left = format_input(left)
	right = format_input(right)
	
	return compare_lists(left, right)
	

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

		
