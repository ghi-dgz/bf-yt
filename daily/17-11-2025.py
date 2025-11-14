
def better_golfer(inp):
    print(ord(inp[0]) * "+" + ".", end="")
    curr = ord(inp[0])
    for i in range(1, len(inp)):
        count = ord(inp[i])
        diff = count - curr
        if diff >= 0:
            print("+" * diff, end="")
        else:
            print("-" * (-1 * diff), end="")
        print(".", end="")
        curr = count

better_golfer("uwu")