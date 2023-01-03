class tree:
	def __init__(self, x, y, height):
		self.x = x
		self.y = y
		self.height = height

	def return_x(self):
		return self.x

	def return_y(self):
		return self.y

	def return_height(self):
		return self.height

	def calc_scenic_score(self, top, bottom, left, right):
		top_score = 0
		bottom_score = 0
		left_score = 0
		right_score = 0

		for t in top:
			top_score += 1
			if t.return_height() >= self.return_height():
				break

		for t in bottom:
			bottom_score += 1
			if t.return_height() >= self.return_height():
				break

		for t in left:
			left_score += 1
			if t.return_height() >= self.return_height():
				break

		for t in right:
			right_score += 1
			if t.return_height() >= self.return_height():
				break

		return top_score * bottom_score * left_score * right_score

	def __repr__(self):
		return self.height


tree_list = []
y_axis = 0
for line in open("data.txt", "r"):
	if line[-1] == "\n":
		line = line[:-1]

	for c in range(0, len(line)):
		tree_list.append(tree(c, y_axis, line[c]))

	y_axis += 1
	x_axis = len(line)

top_score = 0
for t1 in tree_list:
	t_top = []
	t_bottom = []
	t_left = []
	t_right = []

	t1_x = t1.return_x()
	t1_y = t1.return_y()

	for t2 in tree_list:
		if not t2 == t1:
			if t1_x == t2.return_x():
				if t1_y < t2.return_y():
					t_bottom.append(t2)
				else:
					t_top.insert(0, t2)

			if t1_y == t2.return_y():
				if t1_x < t2.return_x():
					t_right.append(t2)
				else:
					t_left.insert(0, t2)

	temp = t1.calc_scenic_score(t_top, t_bottom, t_left, t_right)
	if temp > top_score:
		top_score = temp

print(top_score)