from collections import deque
from time import perf_counter

class Solution:
    def __init__(self, source):
        with open(source, 'r') as f:
            c = f.read().split('\n')
        self.data = [tuple(map(int, item.split(','))) for item in c]
        self.bad = set(self.data[0:(1024 if source == 'input.txt' else 12)])
        self.bad_2_electric_boogaloo = set()
        self.max = 70 if source == 'input.txt' else 6
        self.curr = (0, 0)
        self.target = (self.max, self.max)

    def is_valid(self, i, j):
        return 0 <= i <= self.max and 0 <= j <= self.max

    def solve(self, part_b=False):
        source = self.bad if not part_b else self.bad_2_electric_boogaloo
        q = deque()
        q.append((0, 0, 0))
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = {(0, 0)}
        while q:
            steps, i, j = q.popleft()
            if (i, j) == self.target:
                return steps
            for a, b in dirs:
                ii, jj = i + a, j + b
                if self.is_valid(ii, jj) and (ii, jj) not in source and (ii, jj) not in visited:
                    q.append((steps + 1, ii, jj))
                    visited.add((ii, jj))
        return -1

    def part_b(self):
        for i in range(len(self.data)):
            self.bad_2_electric_boogaloo.add((self.data[i]))
            if self.solve(True) == -1:
                return self.data[i]

    def part_b_fancy_schmancy_binary_search_or_something_idk_it_should_be_faster(self):
        mid = int(len(self.data) / 2)
        low = 0
        high = len(self.data) - 1
        while low != high:
            self.bad_2_electric_boogaloo = set()
            for i in range(mid):
                self.bad_2_electric_boogaloo.add(self.data[i])
            if self.solve(True) == -1:
                high = mid
                mid = int((high - low) / 2 + low)
            else:
                low = mid + 1
                mid = int((high - low) / 2 + low)
        return self.data[low - 1] # idk why I have to return -1 oh well fogettaboutit


start = perf_counter()
sol = Solution('input.txt')
a = sol.solve()
print(f"Part A: {a}")
b = sol.part_b()
print(f"Part B: {b}")
print(f"Total time without binary search part B: {perf_counter() - start}")

start_2 = perf_counter()
sol = Solution('input.txt')
a = sol.solve()
print(f"Part A: {a}")
b = sol.part_b_fancy_schmancy_binary_search_or_something_idk_it_should_be_faster()
print(f"Part B: {b}")
print(f"Total time with binary search part B: {perf_counter() - start_2}")