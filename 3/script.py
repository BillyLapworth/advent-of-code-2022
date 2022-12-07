inp = open("input.txt", "r").read()
inp = inp.split("\n")

total = 0
for i in range(0, len(inp), 3):
    char = list(set(inp[i]) & set(inp[i+1]) & set(inp[i+2]))
    pri = ord(char[0])
    if pri < 91:
        pri -= 64 - 26
    else:
        pri -= 96
    print(char)
    print(pri)
    print()
    total += pri

print(total)
