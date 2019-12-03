import numpy

def main():
    summa = 0
    gaga = 0
    f = open("List.txt", "r")
    for x in f:
        summa += int(int(x)/3)-2
        numba = int(int(x)/3)-2
        while numba >= 0:
            gaga += numba
            numba = int(int(numba)/3)-2

    print("First answer: {}" .format(summa))
    print("Second answer: {}" .format(gaga))

main()