from functools import cache
from time import perf_counter

class Solution:
    def __init__(self, source):
        with open(source, 'r') as f:
            shirts, patterns = f.read().split('\n\n')
        self.shirts = shirts.split(', ')
        self.max = max(len(shirt) for shirt in self.shirts)
        self.patterns = patterns.split('\n')

    @cache
    def is_valid(self, pattern):
        if not pattern:
            return 1

        total_combinations = 0
        curr = ""
        for i in range(len(pattern)):
            curr = curr + pattern[i]
            if len(curr) > self.max:
                break
            if curr in self.shirts:
                total_combinations += self.is_valid(pattern[i + 1:])
        return total_combinations


    def solve(self):
        part_a = 0
        part_b = 0
        for i, pattern in enumerate(self.patterns):
            # print(f"Dealing with pattern {i + 1} out of {length}")
            result = self.is_valid(pattern)
            part_b += result
            if result:
                part_a += 1
        return part_a, part_b

start = perf_counter()
sol = Solution('input.txt')
a, b = sol.solve()
print(f"Part A: {a}")
print(f"Part B: {b}")
print(f"Total Time: {perf_counter() - start}")