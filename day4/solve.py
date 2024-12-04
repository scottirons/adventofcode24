class Solution:
    def __init__(self, input):
        self.data = None
        with open(input, "r") as f:
            self.data = f.read().split()
        self.rows = len(self.data)
        self.cols = len(self.data[0])
        self.part_a = 0
        self.part_b = 0
    
    # def is_valid(self, coords):
    #     r, c = coords
    #     return r < 0 or r >= len(self.data) or c < 0 or c >= len(self.data[0])
    def check_path(self, coords_list):
        r1, c1 = coords_list[0]
        r2, c2 = coords_list[1]
        r3, c3 = coords_list[2]
        return self.data[r1][c1] == "M" and self.data[r2][c2] == "A" and self.data[r3][c3] == "S"
    
    def solve_b(self, coords):
        r, c = coords
        return {self.data[r - 1][c - 1], self.data[r + 1][c + 1]} == {self.data[r - 1][c + 1], self.data[r + 1][c - 1]} == {"M", "S"}

    def find_words(self, coords):
        r, c = coords
        # left and up-left and down-left
        if c >= 3:
            # left-up
            if r >= 3:
                self.part_a += self.check_path([(r - 1, c - 1), (r - 2, c - 2), (r - 3, c - 3)])
            # left-down
            if self.rows - r >= 4:
                self.part_a += self.check_path([(r + 1, c - 1), (r + 2, c - 2), (r + 3, c - 3)])
            # left
            self.part_a += self.check_path([(r, c - 1), (r, c - 2), (r, c - 3)])
        # right and up-right and down-right
        if self.cols - c >= 4:
            # right-up
            if r >= 3:
                self.part_a += self.check_path([(r - 1, c + 1), (r - 2, c + 2), (r - 3, c + 3)])
            # right-down
            if self.rows - r >= 4:
                self.part_a += self.check_path([(r + 1, c + 1), (r + 2, c + 2), (r + 3, c + 3)])
            # right
            self.part_a += self.check_path([(r, c + 1), (r, c + 2), (r, c + 3)])
        # up
        if r >= 3:
            self.part_a += self.check_path([(r - 1, c), (r - 2, c), (r - 3, c)])
        # down
        if self.rows - r >= 4:
            self.part_a += self.check_path([(r + 1, c), (r + 2, c), (r + 3, c)])
        
    def solve(self):
        # part a
        for r in range(self.rows):
            for c in range(self.cols):
                if self.data[r][c] == "X":
                    self.find_words((r, c))
        
        # part b
        for r in range(1, self.rows - 1):
            for c in range(1, self.cols - 1):
                if self.data[r][c] == "A":
                    self.part_b += self.solve_b((r, c))
        return self.part_a, self.part_b

sol = Solution("input.txt")
part_a, part_b = sol.solve()
print(f"Part A: {part_a}")
print(f"Part B: {part_b}")