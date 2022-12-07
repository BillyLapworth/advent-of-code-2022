inp = list(open("input.txt", "r").read())

for i in range(13, len(inp)):
    last_four = inp[i-14:i]
    if len(last_four) == len(set(last_four)):
        print(last_four)
        print(i)
