f = open("test.txt", "w")


for i in range(0, 500):
	f.write("50-55,57-55\n")

f.close()