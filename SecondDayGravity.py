from random import seed
from random import random

f = open("List2.txt", "r")
y = f.read().rstrip().split(",")
d = list(map(int, y))


def main(x):
    i = 0
    while i < len(d):
        if (x[i] == 1):
            opcode1(x, i)
        if (x[i] == 2):
            opcode2(x, i)
        if (x[i] == 99):
            break
        i = i + 4
    #print(d[0])


def opcode1(d, i):
    a = d[i + 3]
    b = d[i + 1]
    c = d[i + 2]
    d[a] = d[b] + d[c]
    return


def opcode2(d, i):
    a = d[i + 3]
    b = d[i + 1]
    c = d[i + 2]
    d[a] = d[b] * d[c]
    return


def write(x, y):
    d[x] = y

def findComb(x):
    for y in range(99):
        for z in range(99):
            e = [int(a) for a in d]
            e[1] = y
            e[2] = z
            try:
                main(e)
            except IndexError:
                pass
            if (e[0] == x):
                print(f"{e[0]} with numbers {y} and {z}. Thus 100 * ")

findComb(19690720)
