number_of_files = open("input.txt", "r")
line = number_of_files.readline()
total = 0
numoflines = 0

while line!= "":
    numoflines += 1
    total += int(line)
    line = num_of_files.readline()
    
avg = total/numoflines
print(avg)