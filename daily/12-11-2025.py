"""
A is dividend 
B is divisor 
R is remainder 
Q is quotient

A = B * Q + R
"""

a = 25
b = 7
r = q = 0

print(a, b, q, r)

while a != 0:
    if b == 0:
        q += 1
        while r != 0:
            b += 1
            r -= 1
    else:
        a -= 1
        b -= 1
        r += 1
if b == 0:
    q += 1
    while r != 0:
        b += 1
        r -= 1
b = 0

print(a, b, q, r)