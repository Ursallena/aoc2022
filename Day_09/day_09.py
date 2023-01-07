## x = R/L
## y = U/D

class position():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.tail_touched = False

	def return_pos(self):
		return [self.x, self.y]

	def tail_touch(self):
		self.tail_touched = True

	def return_tail_touch(self):
		return self.tail_touched

	def __repr__(self):
		return str(self.x) + ", " + str(self.y)

## expecting head & tail to be [x, y]
def check_tail_pos(head, tail, pos_list):
	head = head.return_pos()
	tail = tail.return_pos()
	if head[0] - 1 > tail[0]:
		tail[0] += 1
	elif head[0] + 1 < tail[0]:
		tail[0] -= 1

	if head[1] - 1 > tail[1]:
		tail[1] += 1
	elif head[1] +1 < tail[1]:
		tail[1] -= 1

	for pos in pos_list:
		if pos.return_pos() == tail:
			tail = pos
			break

	if type(tail) == type([]):
		pos_list.append(position(tail[0], tail[1]))
		tail = pos_list[-1]


	for pos in pos_list:
		if pos.return_pos() == tail.return_pos():
			pos.tail_touch()
			break
	
	return tail, pos_list

def head_move(head, movement, pos_list):
	head_location = head.return_pos()

	if movement == "R":
		head_location[0] += 1
	elif movement == "L":
		head_location[0] -= 1
	elif movement == "U":
		head_location[1] += 1
	elif movement == "D":
		head_location [1] -= 1

	temp = False
	for pos in pos_list:
		if pos.return_pos() == head_location:
			temp = pos
			break

	if temp:
		head = temp
	else:
		pos_list.append(position(head_location[0], head_location[1]))
		head = pos_list[-1]

	return head


pos_list = [position(0, 0)]
head = pos_list[0]
tail = pos_list[0]
tail_locations = set([0, 0])

for line in open("data.txt", "r"):
	line = line.strip().split(" ")

	for i in range(0, int(line[1])):
		head = head_move(head, line[0], pos_list)
		tail, pos_list = check_tail_pos(head, tail, pos_list)


	print(line)
	print(head)
	print(tail)


counter = 0
for pos in pos_list:
	if pos.return_tail_touch():
		counter += 1

print(counter)
print(str(len(pos_list)))