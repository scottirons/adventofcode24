import re

def evaluate(line):
    nums = re.findall("[0-9]+", line)
    return int(nums[0]) * int(nums[1])

def solve(source):
    all_mults = []
    all_mults_b = []
    with open(source, "r") as f:
        lines = f.readlines()
        for line in lines:
            all_mults_b += re.findall(r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)", line)
    for m in all_mults_b:
        if m[0] == "m":
            all_mults.append(m)

    part_a = sum(evaluate(l) for l in all_mults)
    part_b = 0
    mult = True
    for m in all_mults_b:
        if m[0] == "m" and mult:
            part_b += evaluate(m)
        elif m == "do()":
            mult = True
        elif m == "don't()":
            mult = False
    return part_a, part_b

part1, part2 = solve("input.txt")
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")