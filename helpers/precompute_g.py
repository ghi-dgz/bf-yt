# precompute_G.py
import pickle

def repeat(s, n):
    return s * n

G = [["" for _ in range(256)] for _ in range(256)]

# initial +/-
for x in range(256):
    for y in range(256):
        delta = (y - x + 128) & 255
        if delta >= 128:
            delta -= 256
        if delta >= 0:
            G[x][y] = "+" * delta
        else:
            G[x][y] = "-" * (-delta)

changed = True
while changed:
    changed = False

    # multiplier schemes
    for x in range(256):
        for n in range(1, 40):
            for d in range(1, 40):

                # case 1
                j = x
                y = 0
                for _ in range(256):
                    if j == 0: break
                    j = (j - d) & 255
                    y = (y + n) & 255

                if j == 0:
                    s = "[" + "-"*d + ">" + "+"*n + "<]>"
                    if len(s) < len(G[x][y]):
                        G[x][y] = s
                        changed = True

                # case 2
                j = x
                y = 0
                for _ in range(256):
                    if j == 0: break
                    j = (j + d) & 255
                    y = (y - n) & 255

                if j == 0:
                    s = "[" + "+"*d + ">" + "-"*n + "<]>"
                    if len(s) < len(G[x][y]):
                        G[x][y] = s
                        changed = True

    # combination
    for x in range(256):
        for y in range(256):
            gxy = G[x][y]
            for z in range(256):
                cand = G[x][z] + G[z][y]
                if len(cand) < len(gxy):
                    gxy = cand
                    changed = True
            G[x][y] = gxy

# save to disk
with open("helpers/G_table.pkl", "wb") as f:
    pickle.dump(G, f)

print("Saved optimized G_table.pkl")
