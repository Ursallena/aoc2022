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

	return temp[0]

def compare_lists(left, right):
	list_type = type([])
	int_type = type(0)
	temp = "Null"
	#print("Comparing: " + str(left) + str(right))

	if left == [] and right == []:
		#print("List ended, nothing happened")
		return "Null"

	elif left == [] and not right == []:
		#print("True because left empty")
		return True

	elif not left == [] and right == []:
		#print("False because right empty")
		return False

	smallest_len = len(left)
	if len(right) < smallest_len:
		smallest_len = len(right)

	#print("~~~~~~~~" + str(smallest_len) + "~~~~~~~")

	for i in range(0, smallest_len):
		left_type = type(left[i])
		right_type = type(right[i])
		#print(left, right, left_type, left[i], right_type, right[i], len(left), len(right))

		if left_type == list_type and right_type == list_type:
			temp = compare_lists(left[i], right[i])

		elif left_type == list_type and right_type == int_type:
			temp = compare_lists(left[i], [right[i]])

		elif left_type == int_type and right_type == list_type:
			temp = compare_lists([left[i]], right[i])

		else:
			if left[i] < right[i]:
				#print("True because left smaller than right")
				return True

			elif left[i] > right[i]:
				#print("False because left larger than right")
				return False

			elif i == smallest_len:
				return "Null"

		if not temp == "Null":
			return temp

	if smallest_len == len(left) and smallest_len == len(right):
		#print("Returned Null because both lists ended")
		return "Null"

	elif smallest_len == len(left) and not smallest_len == len(right):
		#print("True because left ran out of items first")
		return True
	else:
		#print("False because right ran out of items first")
		return False



def compare_sides(left, right):
	left = format_input(left)
	right = format_input(right)
	
	temp = compare_lists(left, right)
	#print(temp)
	return temp

if __name__ == "__main__":
	#print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	left = False
	right = False
	index = 1
	total_sum = 0
	input_sorted_list = []
	for line in open("data.txt", "r"):
		line = line.strip()
		
		if not line == "":
			#print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
			#print(input_sorted_list)
			line = format_input(line)

			if input_sorted_list == []:
				input_sorted_list.append(line)
			else:

				for i in range(0, len(input_sorted_list)):
					if compare_lists(line, input_sorted_list[i]):
						input_sorted_list.insert(i, line)
						break

				if not line in input_sorted_list:
					input_sorted_list.append(line)


	divider_packets = [[[2]], [[6]]]
	for d_p in divider_packets:
		temp = d_p
		for i in range(0, len(input_sorted_list)):
			if compare_lists(temp, input_sorted_list[i]):
				input_sorted_list.insert(i, temp)
				break

		if not temp in input_sorted_list:
			input_sorted_list.append(temp)

	for i in range(0, len(input_sorted_list)):
		print(str(i + 1) + ": " + str(input_sorted_list[i]))


	decoder_2_index = 0
	decoder_6_index = 0

	for i in range(0, len(input_sorted_list)):
		if input_sorted_list[i] == divider_packets[0]:
			decoder_2_index = i + 1
		elif input_sorted_list[i] == divider_packets[1]:
			decoder_6_index = i + 1

	print(str(decoder_2_index * decoder_6_index))