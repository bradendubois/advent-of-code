from sys import stdin

l = []

for line in stdin:
    l.append(line.rstrip())

numbers = l[0].split(",")

nums = [int(x) for x in numbers]

occurrences = dict()

for i, x in enumerate(nums):
    occurrences[x] = [i + 1]

# Gross...
while len(nums) < 30000000:

    if len(nums) % 50000 == 0:
        print("{:.2f}%".format(len(nums) / 30000000 * 100), end="\r")

    last = nums[-1]

    if len(occurrences[last]) == 1:
        speak = 0

    else:
        speak = occurrences[last][0] - occurrences[last][1]
    
    nums.append(speak)

    if speak not in occurrences:
        occurrences[speak] = [len(nums)]
    else:
        occurrences[speak].insert(0, len(nums))

    if len(occurrences[speak]) > 2:
        occurrences[speak].pop(-1)


# Part One
print("\n", nums[2019])

# Part Two
print(nums[-1])
