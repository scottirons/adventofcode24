class Directions:
    def __init__(self, start):
        self.dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        paths = {
            ">": 0,
            "v": 1,
            "<": 2,
            "^": 3
        }
        self.start = paths[start]
    
    def next(self):
        self.start = (self.start + 1) % 4
    
    def peek_next(self):
        return self.dirs[(self.start + 1) % 4]
    
    def get_curr(self):
        return self.dirs[self.start]
    
    def get_opp(self):
        return self.dirs[(self.start + 2) % 4]

class Solution:

    def __init__(self, source):
        with open(source, "r") as f:
            self.data = f.read().split("\n")
        self.part_a = 1
        self.part_b = 0
        self.visited = set()
        self.dir_vis = set()
        self.curr, self.dir = self.find_start()
        self.dir_vis.add((self.curr, self.dir.get_curr()))
        self.extend_tail()
    
    def find_start(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                if self.data[i][j] not in "#.":
                    dirs = Directions(self.data[i][j])
                    self.visited.add((i, j))
                    return (i, j), dirs
    
    def extend_tail(self):
        curr_dir = self.dir.get_curr()
        opp = self.dir.get_opp()
        a, b = self.curr[0], self.curr[1]
        while a >= 0 and a < len(self.data) and b >= 0 and b < len(self.data[0]):
            if self.data[a][b] == "#":
                break
            self.dir_vis.add(((a, b), curr_dir))
            a += opp[0]
            b += opp[1]


    def solve(self):
        while True:
            a, b = self.curr[0] + self.dir.get_curr()[0], self.curr[1] + self.dir.get_curr()[1]
            if a < 0 or a >= len(self.data) or b < 0 or b >= len(self.data[0]):
                break
            nc = self.data[a][b]
            if nc == "#":
                self.dir.next()
                self.extend_tail()
            else:
                if (a, b) not in self.visited:
                    self.part_a += 1
                self.visited.add((a, b))
                if (self.curr, self.dir.peek_next()) in self.dir_vis:
                    self.part_b += 1
                self.dir_vis.add((self.curr, self.dir.get_curr()))
                self.curr = (a, b)
        return self.part_a, self.part_b
        

sol = Solution("input.txt")
a, b = sol.solve()
print(f"Part A: {a}")
print(f"Part B: {b}")