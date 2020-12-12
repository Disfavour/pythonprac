import asyncio


async def merge_sort(data):
    #await asyncio.sleep(1)
    count = len(data)
    if count > 2:
        #part_1 = merge_sort(data[:count // 2])
        part_1 = asyncio.create_task(merge_sort(data[:count // 2]))
        #part_2 = merge_sort(data[count // 2:])
        part_2 = asyncio.create_task(merge_sort(data[count // 2:]))
        await asyncio.gather(part_1, part_2)
        #print(part_1.result(), part_2.result(), count)
        part_1 = part_1.result()
        part_2 = part_2.result()
        data = part_1 + part_2
        last_index = len(data) - 1

        for i in range(last_index):
            min_value = data[i]
            min_index = i

            for j in range(i + 1, last_index + 1):
                if min_value > data[j]:
                    min_value = data[j]
                    min_index = j

            if min_index != i:
                data[i], data[min_index] = data[min_index], data[i]

    elif len(data) > 1 and data[0] > data[1]:
        data[0], data[1] = data[1], data[0]

    return data


print(asyncio.run(merge_sort(eval(input()))))
