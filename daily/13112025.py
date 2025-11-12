def euclid_division(a, b):
    q = r = 0
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
    return q, r

orig = 999
q_0, r_0 = euclid_division(orig, 10)
q_1, r_1 = euclid_division(q_0, 10)
q_2, r_2 = euclid_division(q_1, 10)

print(r_2, r_1, r_0)