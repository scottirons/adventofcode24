class Solution:
    def __init__(self, source):
        with open(source, "r") as f:
            self.lines = f.read()
            self.lines = self.lines + '0'
        self.part_a = 0
        self.part_b = 0
    
    def get_data(self):
        data = []
        add_i = 0
        for i in range(0, len(self.lines) - 1, 2):
            add_i += int(self.lines[i])
            data.append([int(self.lines[i]), int(self.lines[i + 1]), add_i - int(self.lines[i]), add_i])
            add_i += int(self.lines[i + 1])
        return data

    def solve_a(self):
        data = self.get_data()
        curr_i = 0
        max_i = int(len(self.lines) / 2) - 1
        while max_i > curr_i:
            if not data[curr_i][1]:
                curr_i += 1
                continue
            if not data[max_i][0]:
                max_i -= 1
                continue
            self.part_a += (data[curr_i][3] * max_i)
            data[curr_i][3] += 1
            data[max_i][0] -= 1
            data[curr_i][1] -= 1
        for i in range(len(data)):
            curr = data[i]
            for _ in range(curr[0]):
                self.part_a += (i * curr[2])
                curr[2] += 1
        return self.part_a
    
    def solve_b(self):
        data = self.get_data()
        curr_i = 0
        max_i = int(len(self.lines) / 2) - 1
        while max_i > 0:   
            space, to_move = data[curr_i][1], data[max_i][0]
            if not space:
                curr_i += 1
                if curr_i == max_i:
                    max_i -= 1
                    curr_i = 0
                continue
            if not to_move:
                max_i -= 1
                continue
            if to_move > space:
                curr_i += 1
                if curr_i == max_i:
                    max_i -= 1
                    curr_i = 0
                continue
            data[curr_i][1] -= data[max_i][0]
            for _ in range(data[max_i][0]):
                self.part_b += (data[curr_i][3] * max_i)
                data[curr_i][3] += 1
            data[max_i][0] = 0
            max_i -= 1
            curr_i = 0
        for i in range(len(data)):
            curr = data[i]
            for _ in range(curr[0]):
                self.part_b += (i * curr[2])
                curr[2] += 1
        return self.part_b
            

sol = Solution("input.txt")
a = sol.solve_a()
print(f"Part A: {a}")
b = sol.solve_b()
print(f"Part B: {b}")
