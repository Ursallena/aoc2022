
cycle_counter = 1
data = []
output = []
adding_to_x = False
x = 1

def print_data(sprite, out):
	out = len(out)
	while out > 39:
		out -= 40
	
	if sprite - 1 <= out and sprite + 1 >= out:
		return "#"
	return "."
	

def print_output(output):
	for i in range(0, 6):
		to_print = ""
		for x in output[(i * 40):(i * 40 + 40)]:
			to_print += x

		print("->" + to_print + "<-")



for line in open("data.txt", "r"):
	data.append(line.strip().split(" "))

while(cycle_counter < 241):
	output.append(print_data(x, output))

	if "addx" in data[0]:
		if adding_to_x:
			x += int(data[0][1])
			adding_to_x = False
		else:
			adding_to_x = True

	if not adding_to_x:
		data.pop(0)

	cycle_counter += 1


print_output(output)