class Directions:
    def __init__(self, start):
        self.dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.start = start
        self.curr = self.start
    
    def get_start(self):
        return self.start
    
    def next(self):
        self.curr = (self.curr + 1) % 4
    
    def peek_next(self):
        return self.dirs[(self.curr + 1) % 4]
    
    def get_curr(self):
        return self.dirs[self.curr]
    
    def get_opp(self):
        return self.dirs[(self.curr + 2) % 4]

class Solution:

    def __init__(self, source):
        with open(source, "r") as f:
            self.data = f.read().split("\n")
        self.part_a = 1
        self.part_b = 0
        self.visited = set()
        self.curr, self.dir = self.find_start()
        
    def find_start(self):
        paths = {
            ">": 0,
            "v": 1,
            "<": 2,
            "^": 3
        }
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                if self.data[i][j] not in "#.":
                    dirs = Directions(paths[self.data[i][j]])
                    self.visited.add((i, j))
                    return (i, j), dirs
    
    def check_cycle(self, start, dir, new_block):
        visited = {(start, dir.get_curr())}
        curr = start
        while True:
            a, b = curr[0] + dir.get_curr()[0], curr[1] + dir.get_curr()[1]
            if a < 0 or a >= len(self.data) or b < 0 or b >= len(self.data[0]):
                break
            nc = self.data[a][b] if (a, b) != new_block else "#"
            if nc == "#":
                dir.next()
            else:
                if ((a, b), dir.get_curr()) in visited:
                    return True
                visited.add(((a, b), dir.get_curr()))
                curr = (a, b)
        return False

    def solve(self):
        while True:
            a, b = self.curr[0] + self.dir.get_curr()[0], self.curr[1] + self.dir.get_curr()[1]
            if a < 0 or a >= len(self.data) or b < 0 or b >= len(self.data[0]):
                break
            nc = self.data[a][b]
            if nc == "#":
                self.dir.next()
            else:
                if (a, b) not in self.visited:
                    self.part_a += 1
                self.visited.add((a, b))
                self.curr = (a, b)
        # now part B
        start, dir = self.find_start()
        self.visited.remove(start)
        for loc in self.visited:
            self.part_b += self.check_cycle(start, Directions(dir.get_start()), loc)
        return self.part_a, self.part_b


sol = Solution("input.txt")
a, b = sol.solve()
print(f"Part A: {a}")
print(f"Part B: {b}")
