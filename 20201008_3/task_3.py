def hz(count, M, lenght):
    if count > 1 and M < lenght * count + 3 * (count - 1):
        count -= 1
        return hz(count, M, lenght)
    else:
        return count


N, M = eval(input())

art = [[i, j, i * j] for i in range(1, N + 1) for j in range(1, N + 1)]

lenght = (len(str(N)) * 2 + len(str(N * N)) + 6)

count = M // lenght  # кол-во столбцов больших
count = hz(count, M, lenght)


if N % count == 0:
    hcount = N // count
else:
    hcount = N // count + 1  # кол-во строк больших

#print(len(str(N)) * 2 + len(str(N * N)) + 6, count, hcount)

сomponent = "{:>" + str(len(str(N))) + "}" + " * " + "{:<" + str(len(str(N))) + "}" + " = " + "{:<" + str(len(str(N * N))) + "}"

print("=" * M)
p = count
for hitem in range(hcount):
    index = 0
    for n in range(N):
        if N % count != 0 and hitem == hcount - 1:
            #print(n, N, count, hcount)
            count = N % p
        for item in range(count):
            if item != 0:
                print(" | ", end="")
            print(сomponent.format(*art[n + item * N]), end="")
        print()
    art = art[count * N:]
    print("=" * M)
