def add_x(x, value):
	return x + int(value)

def check_cycle(cycle, x_value, signal_strength, last_signal):
	if cycle == 20:
		return signal_strength + (x_value * cycle), 20
	elif cycle == (last_signal + 40):
		return signal_strength + (x_value * cycle), last_signal + 40
	else:
		return signal_strength, last_signal



cycle_counter = 1
x_value = 1
signal_strength = 0
last_signal = 0
for line in open("data.txt", "r"):
	line = line.strip().split(" ")

	if line[0] == "noop":
		cycle_counter += 1

	else:
		cycle_counter += 1
		signal_strength, last_signal = check_cycle(cycle_counter, x_value, signal_strength, last_signal)
		x_value = add_x(x_value, line[1])
		cycle_counter += 1

	signal_strength, last_signal = check_cycle(cycle_counter, x_value, signal_strength, last_signal)

print(signal_strength)