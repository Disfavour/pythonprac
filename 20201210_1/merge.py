import random


Src = [random.randrange(10) for i in range(16)]
Tmp = Src.copy()
print(Src)


def merge(From1, To1, To2):
    #print(From1, To1, To2)
    i1, i2 = From1, To1
    for i in range(From1, To2):

        if i1 < To1 and i2 < To2:

            if Src[i1] < Src[i2]:
                Tmp[i] = Src[i1]
                i1 += 1
            else:
                Tmp[i] = Src[i2]
                i2 += 1

        elif i1 < To1:
            Tmp[i] = Src[i1]
            i1 += 1

        else:
            Tmp[i] = Src[i2]
            i2 += 1

    Src[From1:To2] = Tmp[From1: To2]
    #print(Src)



def main():

    for i in range(0, 16, 2):
        merge(i, i + 1, i + 2)

    for i in range(0, 16, 4):
        merge(i, i + 2, i + 4)

    for i in range(0, 16, 8):
        merge(i, i + 4, i + 8)

    merge(0, 8, 16)


main()
print(Src)
