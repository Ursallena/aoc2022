## A = Rock
## B = Paper
## C = Scissors

## X = Rock
## Y = Paper
## Z = Scissors

## Rock = 1 Point
## Paper = 2 Points
## Scissors = 3 Points
## Lose = 0 Points
## Draw = 3 Points
## Win = 6 Points

def calculate_game(elf_move, your_move):
	temp_points = 0
	if your_move == "X":
		temp_points += 1
		if elf_move == "A":
			temp_points += 3
		elif elf_move == "C":
			temp_points += 6

	elif your_move == "Y":
		temp_points += 2
		if elf_move == "A":
			temp_points += 6
		elif elf_move == "B": 
			temp_points += 3

	elif your_move == "Z":
		temp_points += 3
		if elf_move == "B":
			temp_points += 6
		elif elf_move == "C":
			temp_points += 3

	return temp_points


strategy = []
for line in open("data.txt", "r"):
	if "\n" in line:
		line = line[:-1]
	strategy.append(line)

total_points = 0
for line in strategy:
	line = line.split(" ")
	total_points += calculate_game(line[0], line[1])

print(total_points)