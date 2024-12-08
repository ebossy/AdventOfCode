
def p2(f):
    lines = [[int(x) for x in line.split()] for line in f.read().splitlines()]
    ans = 0
    for real_nums in lines:
        for i in range(len(real_nums) + 1):
            nums = real_nums[:i] + real_nums[i + 1 :]
            if nums not in (sorted(nums), sorted(nums, reverse=True)):
                continue
            if not all(1 <= abs(b - a) <= 3 for a, b in zip(nums, nums[1:])):
                continue
            break
        else:
            continue
        ans += 1
    return ans

with open("2-1.txt", "r") as file:
    result = p2(file)
    print(result)