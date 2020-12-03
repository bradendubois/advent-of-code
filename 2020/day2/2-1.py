with open("2.txt") as f:

    valid = 0

    for line in f:

        l = line.split(":")

        password = l[1].strip()

        nums = l[0].split(" ")
        letter = nums[1]
        nums = nums[0]

        low, high = nums.split("-")
        low = int(low)
        high = int(high)

        if low <= password.count(letter) <= high:
            valid += 1

    print(valid)