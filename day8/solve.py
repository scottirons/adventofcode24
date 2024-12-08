from collections import defaultdict

class Solution:
    def __init__(self, source):
        with open(source, 'r') as f:
            self.grid = f.read().split("\n")
        self.nodes = self.find_nodes()
        self.podes_a = set()
        self.podes_b = set()
    
    def find_nodes(self):
        nodes = defaultdict(list)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                s = self.grid[i][j]
                if s != ".":
                    nodes[s].append((i, j))
        return nodes

    def find_podes(self, a, b):
        # higher j adds the j, lower j subtracts it
        # higher i adds the i, lower i subtracts it
        diff_i, diff_j = abs(a[0] - b[0]), abs(a[1] - b[1])
        if a[0] < b[0]:
            a_i = a[0] - diff_i
            b_i = b[0] + diff_i
        else:
            a_i = a[0] + diff_i
            b_i = b[0] - diff_i
        if a[1] < b[1]:
            a_j = a[1] - diff_j
            b_j = b[1] + diff_j
        else:
            a_j = a[1] + diff_j
            b_j = b[1] - diff_j

        return (a_i, a_j), (b_i, b_j)

    def find_all_podes(self, a, b):
        podes = []
        diff_i, diff_j = abs(a[0] - b[0]), abs(a[1] - b[1])
        if a[0] > b[0]:
            diff_i *= -1
        if a[1] > b[1]:
            diff_j *= -1
        i, j = a[0], a[1]
        while i >= 0 and i < len(self.grid) and j >= 0 and j < len(self.grid[0]):
            podes.append((i, j))
            i -= diff_i
            j -= diff_j
        i, j = b[0], b[1]
        while i >= 0 and i < len(self.grid) and j >= 0 and j < len(self.grid[0]):
            podes.append((i, j))
            i += diff_i
            j += diff_j

        return podes

    def find_podes_count(self):
        for type in self.nodes:
            for i in range(len(self.nodes[type])):
                for j in range(i + 1, len(self.nodes[type])):
                    a, b = self.nodes[type][i], self.nodes[type][j]
                    a_podes = self.find_podes(a, b)
                    b_podes = self.find_all_podes(a, b)
                    for pode in a_podes:
                        if 0 <= pode[0] < len(self.grid) and 0 <= pode[1] < len(self.grid[0]):
                            self.podes_a.add(pode)
                    for pode in b_podes:
                        self.podes_b.add(pode)              

    def solve(self):
        self.find_podes_count()
        return len(self.podes_a), len(self.podes_b)

sol = Solution('input.txt')
a, b = sol.solve()
print(f"Part A: {a}")
print(f"Part B: {b}")
