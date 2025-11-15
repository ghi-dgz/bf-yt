# shortbf.py
import pickle
import sys

with open("helpers/G_table.pkl", "rb") as f:
    G = pickle.load(f)

def generate(s):
    lastc = 0
    out = []
    for c in s:
        cv = ord(c)
        a = G[lastc][cv]
        b = G[0][cv]
        out.append(a if len(a) <= len(b) else ">" + b)
        out.append(".")
        lastc = cv
    print("".join(out))

def gen_file(path):
    with open(path, "rb") as f:
        data = f.read()
    s = ''.join(chr(b) for b in data if b != 0)
    generate(s)

if __name__ == "__main__":
    generate(input("> "))
