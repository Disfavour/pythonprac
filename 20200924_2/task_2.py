a = list(eval(input()))
nums = [i ** 2 % 100 for i in a]
swapped = True
while swapped:
    swapped = False
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            a[i], a[i + 1] = a[i + 1], a[i]
            swapped = True
print(a)

