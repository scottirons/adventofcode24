from collections import defaultdict

class Solution:
    def __init__(self, source):
        with open(source, 'r') as f:
            self.grid = f.read().splitlines()
        self.part_a = 0
        self.part_b = 0
        self.key = '0123456789'
        self.visited = defaultdict(set)

    def is_next(self, next_char, prev_char):
        return self.key.index(next_char) == self.key.index(prev_char) + 1
    
    def is_valid(self, a, b):
        return 0 <= a < len(self.grid) and 0 <= b < len(self.grid[0])
    
    def find_paths(self, start, coords, prev_char):
        if prev_char == '9':
            self.part_b += 1
            if coords not in self.visited[start]:
                self.part_a += 1
            self.visited[start].add(coords)
            return
        for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ai, bi = coords[0] + a, coords[1] + b
            if self.is_valid(ai, bi) and self.is_next(self.grid[ai][bi], prev_char):
                self.find_paths(start, (ai, bi), self.grid[ai][bi])


    def solve(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == '0':
                    self.find_paths((i, j), (i, j), '0')
        return self.part_a, self.part_b


# part B is just what I did for part A lol (distinct hiking trails)
sol = Solution('input.txt')
a, b = sol.solve()
print(f"Part A: {a}")
print(f"Part B: {b}")
