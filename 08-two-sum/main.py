nums = [2, 7, 11, 7]

target = 9

output = []

output = [
    [i, j]
    for i, num1 in enumerate(nums)
    for j, num2 in enumerate(nums[i + 1 :], start=i + 1)
    if num1 + num2 == target
]

print(output[0])
