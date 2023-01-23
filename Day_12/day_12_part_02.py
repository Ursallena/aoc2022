class location():
	def __init__(self, x, y, height, is_end_point = False):
		self.x = x
		self.y = y
		self.height = height
		self.parents = []
		self.children = []
		self.is_end_point = is_end_point

	def set_parent(self, parents):
		self.parents = parents

	def set_children(self, children):
		self.children = children

	def __repr__(self):
		return "[" + str(self.x) + ", " + str(self.y) + "]"

	def __str__(self):
		return "[" + str(self.x) + ", " + str(self.y) + "]"

data = []
location_list = []
player_location = False
starting_options = []
max_x = 0
max_y = 0

for line in open("data.txt", "r"):
	data.append(line.strip())

for i in range(0, len(data)):
	for c in range(0, len(data[i])):
		if ord(data[i][c]) == 83:
			location_list.append(location(c, i, 1))
			player_location = location_list[-1]
			starting_options.append(location_list[-1])

		elif ord(data[i][c]) == 69:
			location_list.append(location(c, i, 26, True))

		else:
			location_list.append(location(c, i, ord(data[i][c]) - 96))

		if ord(data[i][c]) == 97:
			starting_options.append(location_list[-1])

		if max_x < c:
			max_x = int(c)

		if max_y < i:
			max_y = int(i)

for l in range(0, len(location_list)):
	x = location_list[l].x
	y = location_list[l].y
	temp = []
	children = []

	if not y == 0:
		temp.append([y - 1, x])

	if not x == 0:
		temp.append([y, x - 1])

	if not y == max_y:
		temp.append([y + 1, x])

	if not x == max_x:
		temp.append([y, x + 1])

	for i in location_list:
		if [i.y, i.x] in temp and location_list[l].height + 1 >= i.height:
			children.append(i)

	location_list[l].set_children(children)

fewest_steps = 0
for option in starting_options:
	bfs_queue = [option]
	bfs_visited = [option]

	for l in location_list:
		l.set_parent([])

	while True:
		if bfs_queue[0].is_end_point:
			break

		for c in bfs_queue[0].children:
			if not c in bfs_visited and c.parents == []:
				c.set_parent(bfs_queue[0])
				bfs_queue.append(c)

		bfs_queue.pop(0)
		if bfs_queue == []:
			break

		bfs_visited.append([bfs_queue[0].x, bfs_queue[0].y])

	if not bfs_queue == []:
		steps = 0
		parent = bfs_queue[0].parents
		while True:
			if not parent == []:
				parent = parent.parents
				steps += 1
			else:
				break

		print(steps)

		if fewest_steps == 0 or fewest_steps > steps:
			fewest_steps = steps
	else:
		print("Can't reach end point :c ")

print("Fewest steps: " + str(fewest_steps))
print("Total starting positions: " + str(len(starting_options)))