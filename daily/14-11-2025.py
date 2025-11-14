a = 3
b = 5
c = 1
d = 0

while c != 0:
    a -= 1
    b -= 1
    d += 1
    if a == 0 or b == 0:
        c = 0

if a != 0:
    c = a
else:
    c = b

print(c)