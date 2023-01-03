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

	def calc_if_visible(self, top, bottom, left, right):
		if top == [] or bottom == [] or left == [] or right == []:
			return False

		top_t = False
		bottom_t = False
		left_t = False
		right_t = False

		for t in top:
			if t.height >= self.height:
				top_t = True

		for t in bottom:
			if t.height >= self.height:
				bottom_t = True

		for t in left:
			if t.height >= self.height:
				left_t = True

		for t in right:
			if t.height >= self.height:
				right_t = True

		if top_t and bottom_t and left_t and right_t:
			return True

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

total_visible = 0
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
					t_top.append(t2)

			if t1_y == t2.return_y():
				if t1_x < t2.return_x():
					t_right.append(t2)
				else:
					t_left.append(t2)

	if not t1.calc_if_visible(t_top, t_bottom, t_left, t_right):
		total_visible += 1

print(total_visible)
