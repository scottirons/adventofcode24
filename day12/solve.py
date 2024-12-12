class Solution:
    def __init__(self, source):
        with open(source, 'r') as f:
            self.grid = f.read().splitlines()
        self.visited = set()
        self.part_a = 0
        self.part_b = 0
        self.curr_set = set()

    def is_valid(self, a, b):
        return 0 <= a < len(self.grid) and 0 <= b < len(self.grid[0])

    def find_corners(self):
        total = 0
        for a, b in self.curr_set:
            if (a + 1, b) not in self.curr_set and (a, b + 1) not in self.curr_set:
                total += 1
            if (a + 1, b) not in self.curr_set and (a, b - 1) not in self.curr_set:
                total += 1
            if (a - 1, b) not in self.curr_set and (a, b + 1) not in self.curr_set:
                total += 1
            if (a - 1, b) not in self.curr_set and (a, b - 1) not in self.curr_set:
                total += 1

            if (a + 1, b) in self.curr_set and (a, b + 1) in self.curr_set and (a + 1, b + 1) not in self.curr_set:
                total += 1
            if (a + 1, b) in self.curr_set and (a, b - 1) in self.curr_set and (a + 1, b - 1) not in self.curr_set:
                total += 1
            if (a - 1, b) in self.curr_set and (a, b + 1) in self.curr_set and (a - 1, b + 1) not in self.curr_set:
                total += 1
            if (a - 1, b) in self.curr_set and (a, b - 1) in self.curr_set and (a - 1, b - 1) not in self.curr_set:
                total += 1
        return total

    def search(self, curr, a, b):
        if not self.is_valid(a, b):
            return 0, 1
        elif self.grid[a][b] != curr:
            return 0, 1
        elif (a, b) in self.visited:
            return 0, 0
        else:
            self.visited.add((a, b))
            self.curr_set.add((a, b))
            area = 1
            perimeter = 0
            for ii, jj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                add_a, add_p = self.search(curr, a + ii, b + jj)
                area += add_a
                perimeter += add_p
            return area, perimeter


    def solve(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if (i, j) not in self.visited:
                    area = 1
                    perimeter = 0
                    c = self.grid[i][j]
                    self.visited.add((i, j))
                    self.curr_set.add((i, j))
                    for ii, jj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        add_a, add_p = self.search(c, i + ii, j + jj)
                        area += add_a
                        perimeter += add_p
                    self.part_a += area * perimeter
                    # print(f"Plot of char: {c} with area: {area} and perimeter: {perimeter}")
                    self.part_b += self.find_corners() * len(self.curr_set)
                    self.curr_set = set()
        return self.part_a, self.part_b

sol = Solution("input.txt")
a, b = sol.solve()
print(f'Part A: {a}')
print(f'Part B: {b}')
