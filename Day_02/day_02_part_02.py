## A = Rock
## B = Paper
## C = Scissors

## X = Lose
## Y = Draw
## Z = Win

## Rock = 1 Point
## Paper = 2 Points
## Scissors = 3 Points
## Lose = 0 Points
## Draw = 3 Points
## Win = 6 Points

def calculate_game(elf_move, outcome):
	temp_points = 0
	
	if outcome == "X":
		if elf_move == "A":
			temp_points += 3
		elif elf_move == "B":
			temp_points += 1
		else:
			temp_points += 2

	elif outcome == "Y":
		if elf_move == "A":
			temp_points += 1
		elif elf_move == "B":
			temp_points += 2
		else:
			temp_points += 3
		temp_points += 3

	else:
		if elf_move == "A":
			temp_points += 2
		elif elf_move == "B":
			temp_points += 3
		else: 
			temp_points += 1
		temp_points += 6

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