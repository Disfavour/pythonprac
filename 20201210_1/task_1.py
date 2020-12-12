import asyncio
import random
import sys


d = {}


async def merge(From1, To1, To2):
    d[From1, To2] = asyncio.Future()

    if To1 - From1 > 1:
        await d[From1, To1]
    if To2 - To1 > 1:
        await d[To1, To2]

    #await asyncio.sleep(sec)

    i1, i2 = From1, To1
    for i in range(From1, To2):

        await asyncio.sleep(0)

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
    d[From1, To2].set_result("qq")


async def main():

    tasks = []

    for i in range(0, 16, 2):
        tasks.append(asyncio.create_task(merge(i, i + 1, i + 2)))
    await asyncio.gather(*tasks)
    tasks = []

    for i in range(0, 16, 4):
        tasks.append(asyncio.create_task(merge(i, i + 2, i + 4)))
    await asyncio.gather(*tasks)
    tasks = []

    for i in range(0, 16, 8):
        tasks.append(asyncio.create_task(merge(i, i + 4, i + 8)))
    await asyncio.gather(*tasks)
    tasks = []

    tasks.append(asyncio.create_task(merge(0, 8, 16)))
    await asyncio.gather(*tasks)


Src = eval(sys.stdin.read())
Tmp = Src.copy()
asyncio.run(main())
print(Src)
