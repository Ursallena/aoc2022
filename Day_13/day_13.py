## if both integers, left should be lower
## if both lists, left should run out of items first
def return_type(input):
	if input == "[":
		return "List"
	elif input == "]":
		return "End_of_list"
	elif input == "," or input == " ":
		return "delete me!"
	else:
		return "Int"

def compare(left, right):
	inside_list = 0
	while not left == "" and not right == "":
		left_type = False
		right_type = False

		left_type = return_type(left[0])
		right_type = return_type(right[0])

		if left_type == "List" and right_type == "List":
			inside_list += 1

		if left_type == "List" and right_type == "Int":
			left = "[" + left
			right = "[[" + right[0] + "]" + right[1:]

		if left_type == "Int" and right_type == "List":
			right = "[" + right
			left = "[[" + left[0] + "]" + left[1:]

		if left_type == "Int" and right_type == "Int":
			if int(left[0]) < int(right[0]):
				return True

			elif int(left[0]) > int(right[0]):
				return False

		if inside_list > 0:
			if left_type == "End_of_list" and not right_type == "End_of_list":
				return True
			elif not left_type == "End_of_list" and right_type == "End_of_list":
				return False
			if left_type == "End_of_list" and right_type == "End_of_list":
				inside_list -= 1

		left = left[1:]
		right = right[1:]

	if left == "":
		return True
	else:
		return False
	

left = False
right = False
total_sum = 0
index = 1
for line in open("data.txt", "r"):
	line = line.strip()

	if not left:
		left = line

	elif not right:
		right = line

	if left and right:
		if compare(left, right):
			total_sum += index

		print(index, total_sum)
		
		index += 1

		left = False
		right = False



print(total_sum)