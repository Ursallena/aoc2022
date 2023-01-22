## Starting point = 83
## Goal = 69

class location():
	def __init__(self, x, y, height, parents = [], is_end_point = False):
		self.x = x
		self.y = y
		self.height = height
		self.parents = parents
		self.is_end_point = is_end_point

	def set_parent(self, parents):
		self.parents = parents

	def __repr__(self):
		return "[" + str(self.x) + ", " + str(self.y) + "]"

	def __str__(self):
		return "[" + str(self.x) + ", " + str(self.y) + "]"

data = []
location_list = []
location_mem = [] 
player_location = False
max_x = 0
max_y = 0

for line in open("data.txt", "r"):
	data.append(line.strip())

for i in range(0, len(data)):
	for c in range(0, len(data[i])):
		if ord(data[i][c]) == 83:
			location_list.append(location(c, i, 1))
			player_location = location_list[-1]

		elif ord(data[i][c]) == 69:
			location_list.append(location(c, i, 26, True))

		else:
			location_list.append(location(c, i, ord(data[i][c]) - 96))

		if max_x < c:
			max_x = int(c)

		if max_y < i:
			max_y = int(i)



for l in range(0, len(location_list)):
	x = location_list[l].x
	y = location_list[l].y
	temp = []
	parents = []

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
			parents.append(i)

	location_list[l].set_parent(parents)


print(player_location)









