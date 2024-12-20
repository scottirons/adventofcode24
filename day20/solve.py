from collections import deque, defaultdict

class Solution:
    def __init__(self, source):
        with open(source, 'r') as f:
            self.data = f.read().splitlines()
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                if self.data[i][j] == 'S':
                    self.start = (i, j)
                if self.data[i][j] == 'E':
                    self.end = (i, j)

    def is_valid(self, pos):
        return 0 <= pos[0] < len(self.data) and 0 <= pos[1] < len(self.data[0])

    def find_total(self):
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = deque()
        q.append((self.end, 0))
        visited = set()
        path = [self.end]
        steps_dict = {self.end: 1}
        while q:
            curr, steps = q.popleft()
            visited.add(curr)
            if curr == self.start:
                path.reverse()
                return steps_dict, path
            for d in dirs:
                ni, nj = curr[0] + d[0], curr[1] + d[1]
                if not self.is_valid((ni, nj)):
                    continue
                if self.data[ni][nj] in 'S.' and (ni, nj) not in visited:
                    steps_dict[(ni, nj)] = steps + 1
                    q.append(((ni, nj), steps + 1))
                    path.append((ni, nj))

    def solve_a(self):
        counts = defaultdict(int)
        steps_dict, path = self.find_total()
        total = len(steps_dict)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = deque()
        q.append((self.start, 1, False))
        visited = set()
        while q:
            curr, steps, jumped = q.popleft()
            for d in dirs:
                ni, nj = curr[0] + d[0], curr[1] + d[1]
                if not self.is_valid((ni, nj)):
                    continue
                if self.data[ni][nj] in 'E.' and (ni, nj) not in visited:
                    if jumped:
                        saved = total - (steps + steps_dict[(ni, nj)]) - 1
                        counts[saved] += 1
                    else:
                        q.append(((ni, nj), steps + 1, jumped))
                        visited.add((ni, nj))
                elif self.data[ni][nj] == '#' and not jumped:
                    q.append(((ni, nj), steps, True))
        return sum(counts[i] for i in counts if i >= 100), steps_dict, path

    def solve_both(self):
        b = 0
        a, steps_dict, path = self.solve_a()
        for i in range(len(path)):
            for j in range(i + 1, len(path)):
                diff = abs(path[i][0] - path[j][0]) + abs(path[i][1] - path[j][1])
                if diff <= 20:
                    first, second = steps_dict[path[i]], steps_dict[path[j]]
                    saved = first - second - diff
                    if saved >= 100:
                        b += 1
        return a, b


sol = Solution('input.txt')
a, b = sol.solve_both()
print(f"Part A: {a}")
print(f"Part B: {b}")
