class Solution:
    def __init__(self, source):
        with open(source, 'r') as f:
            self.grid = f.read().splitlines()
        self.visited = set()
        self.part_a = 0

    def is_valid(self, a, b):
        return 0 <= a < len(self.grid) and 0 <= b < len(self.grid[0])

    def search(self, curr, a, b):
        if not self.is_valid(a, b):
            return 0, 1
        elif self.grid[a][b] != curr:
            return 0, 1
        elif (a, b) in self.visited:
            return 0, 0
        else:
            self.visited.add((a, b))
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
                    for ii, jj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        add_a, add_p = self.search(c, i + ii, j + jj)
                        area += add_a
                        perimeter += add_p
                    self.part_a += area * perimeter
                    # print(f"Plot of char: {c} with area: {area} and perimeter: {perimeter}")
        return self.part_a

sol = Solution("input.txt")
a = sol.solve()
print(f'Part A: {a}')
