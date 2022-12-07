inp = open("input.txt", "r").read()
rows = inp.split("\n")

dirs = {}
current_dirs = []
indentation = 0
for row in rows:
    if row == "$ cd ..":
        current_dirs.pop()
    elif row[0:4] == "$ cd":
        current_dirs.append(row[5:])
    elif row[0:3] != "dir" and row != "$ ls":
        for di in range(len(current_dirs)):
            path = "/".join(current_dirs[:di + 1])
            if(path in dirs):
                dirs[path] += int(row.split(" ")[0])
            else:
                dirs[path] = int(row.split(" ")[0])
    #print()
    #print(current_dirs)
    #print(dirs)

total = 0       
for d in dirs:
    #print(d + ": " + str(dirs[d]))
    if dirs[d] > 1412830 and dirs[d] < 2412830:
        print(d + ": " + str(dirs[d]))

print(total)
