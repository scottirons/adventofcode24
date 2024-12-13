from sympy import Matrix, linsolve, Integer
import re


class Solution:
    def __init__(self, source):
        with open(source, 'r') as f:
            full_data = f.read().split("\n\n")
        self.data = []
        for chunk in full_data:
            self.data.append([int(i) for i in re.findall(r"\d+", chunk)])
        self.part_a = 0
        self.part_b = 0

    def solve(self):
        for game in self.data:
            system_a = Matrix([[game[0], game[2], game[4]], [game[1], game[3], game[5]]])
            system_b = Matrix([[game[0], game[2], game[4] + 10000000000000], [game[1], game[3], game[5] + 10000000000000]])
            solution_a = linsolve(system_a)
            solution_b = linsolve(system_b)
            for i in solution_a:
                if type(i[0]) == Integer and type(i[1]) == Integer:
                    self.part_a += 3 * i[0]
                    self.part_a += i[1]
            for i in solution_b:
                if type(i[0]) == Integer and type(i[1]) == Integer:
                    self.part_b += 3 * i[0]
                    self.part_b += i[1]
        return self.part_a, self.part_b


sol = Solution("input.txt")
a, b = sol.solve()
print(f"Part A: {a}")
print(f"Part B: {b}")
