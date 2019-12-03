import numpy


def main():
    summa = 0

    f = open("List.txt", "r")
    for x in f:
        summa += int(int(x)/3)-2
    print(summa)

main()