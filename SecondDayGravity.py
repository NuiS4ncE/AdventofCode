f = open("List2.txt", "r")
y = f.read().rstrip().split(",")
d = list(map(int, y))


def main():
    write(1, 12)
    write(2, 2)
    i = 0
    while i < len(d):
        if (d[i] == 1):
            opcode1(i)
        if (d[i] == 2):
            opcode2(i)
        if (d[i] == 99):
            break
        i = i + 4
    print(d[0])

def opcode1(i):
    a = d[i + 3]
    b = d[i + 1]
    c = d[i + 2]
    d[a] = d[b] + d[c]
    return


def opcode2(i):
    a = d[i + 3]
    b = d[i + 1]
    c = d[i + 2]
    d[a] = d[b] * d[c]
    return


def write(x, y):
    d[x] = y



main()
