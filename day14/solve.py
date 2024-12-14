import re
from time import sleep
from collections import deque

height = 103
width = 101
mid_i = height // 2
mid_j = width // 2

with open("input.txt", 'r') as f:
    lines = f.read().split('\n')

first, second, third, fourth = 0, 0, 0, 0

all_robots = deque()


for line in lines:
    data = re.findall(r'-?\d+', line)
    j, i, right, down = [int(val) for val in data]
    all_robots.append([i, j, down, right])
robot_count = len(all_robots)

for robot in all_robots:
    i, j, down, right = robot
    final_j = (j + (100 * right)) % width
    final_i = (i + (100 * down)) % height
    if final_i < mid_i:
        if final_j < mid_j:
            first += 1
        if final_j > mid_j:
            second += 1
    elif final_i > mid_i:
        if final_j < mid_j:
            third += 1
        elif final_j > mid_j:
            fourth += 1

# part 2
# I had no clue how to intuit how large or filled-in the tree was, so I just looked at reddit for a tip.
# guessing that the tree would be where there was a clump of robots was a solid enough thing to work into my
# existing solution (without scrolling through thousands of printouts)
trial = 0
printed = False
while not printed:
    trial += 1
    print_set = set()
    for r in range(robot_count):
        i, j, down, right = all_robots.popleft()
        i = (i + down) % height
        j = (j + right) % width
        print_set.add((i, j))
        all_robots.append([i, j, down, right])
    for robot in print_set:
        a, b = robot
        if (a + 1, b) in print_set and (a + 1, b - 1) in print_set and (a + 1, b + 1) in print_set and (a, b + 1) in print_set \
            and (a, b - 1) in print_set and (a - 1, b) in print_set and (a - 1, b - 1) in print_set and (a - 1, b + 1) in print_set:
            print(f"STEP {trial}")
            for i in range(height):
                for j in range(width):
                    if (i, j) in print_set:
                        print("#", end='')
                    else:
                        print(' ', end='')
                print()
            printed = True
            break


print(first * second * third * fourth)