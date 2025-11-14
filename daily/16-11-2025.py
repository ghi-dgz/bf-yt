# GOLFER

def naive_golfer(strig):
    outp = ""
    for char in strig:
        count = ord(char)
        outp += count * "+"
        outp += ".>"
    return outp
