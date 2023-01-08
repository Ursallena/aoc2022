## x = R/L
## y = U/D

## expecting head & tail to be [x, y]
def check_tail_pos(tail, body_part):
	head = body_part
	if head[0] - 1 > tail[0]:
		if head[1] > tail[1]:
			tail[1] += 1
		elif head[1] < tail[1]:
			tail[1] -= 1

		tail[0] += 1

	elif head[0] + 1 < tail[0]:
		if head[1] > tail[1]:
			tail[1] += 1
		elif head[1] < tail[1]:
			tail[1] -= 1

		tail[0] -= 1

	elif head[1] - 1 > tail[1]:
		if head[0] < tail[0]:
			tail[0] -= 1
		elif head[0] > tail[0]:
			tail[0] += 1

		tail[1] += 1

	elif head[1] + 1 < tail[1]:
		if head[0] < tail[0]:
			tail[0] -= 1
		elif head[0] > tail[0]:
			tail[0] += 1

		tail[1] -= 1

	return tail

def head_move(head_location, movement):

	if movement == "R":
		head_location[0] += 1
	elif movement == "L":
		head_location[0] -= 1
	elif movement == "U":
		head_location[1] += 1
	elif movement == "D":
		head_location [1] -= 1

	return head

def move_body(head, body):
	for b in range(0, len(body)):
		i = body[b]
		if b == 0:
			temp = head
		else:
			temp = body[b - 1]
	
		if temp[0] - 1 > i[0]:
			if temp[1] > i[1]:
				i[1] += 1
			elif temp[1] < i[1]:
				i[1] -= 1

			i[0] += 1

		elif temp[0] + 1 < i[0]:
			if temp[1] > i[1]:
				i[1] += 1
			elif temp[1] < i[1]:
				i[1] -= 1

			i[0] -= 1

		elif temp[1] - 1 > i[1]:
			if temp[0] < i[0]:
				i[0] -= 1
			elif temp[0] > i[0]:
				i[0] += 1

			i[1] += 1

		elif temp[1] + 1 < i[1]:
			if temp[0] < i[0]:
				i[0] -= 1
			elif temp[0] > i[0]:
				i[0] += 1

			i[1] -= 1


		body[b] = i

	return body


head = [0, 0]
tail = [0, 0]
body_parts = []
tails_locations = [[0, 0]]
counter = 0

for i in range(0, 8):
	body_parts.append([0, 0])

for line in open("data.txt", "r"):
	line = line.strip().split(" ")

	for i in range(0, int(line[1])):
		head = head_move(head, line[0])
		body_parts = move_body(head, body_parts)
		tail = check_tail_pos(tail, body_parts[-1])

		in_counter = False
		for i in tails_locations:
			if i == str(tail):
				in_counter = True
				break

		if not in_counter:
			counter +=1
			tails_locations.append(str(tail))


print(counter)