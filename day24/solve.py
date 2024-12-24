from collections import deque
import time

OPS = {"OR": "|", "AND": "&", "XOR": "^"}

class Solution:
    def __init__(self, source):
        self.key = {}
        with open(source, 'r') as f:
            starting, processes = f.read().split('\n\n')
        for s in starting.split('\n'):
            self.key[s[:3]] = int(s[-1])
        q = deque()
        for p in processes.split('\n'):
            a, op, b, _, res = p.split(' ')
            op = OPS[op]
            q.append((a, op, b, res))
        while q:
            a, op, b, res = q.popleft()
            if a in self.key and b in self.key:
                self.key[res] = eval('{a}{op}{b}'.format(a=self.key[a], op=op, b=self.key[b]))
            else:
                q.append((a, op, b, res))

    def solve(self):
        res = ''
        curr_num = 0
        curr = 'z' + ('0' + str(curr_num) if curr_num < 10 else str(curr_num))
        while curr in self.key:
            res = str(self.key[curr]) + res
            curr_num += 1
            curr = 'z' + ('0' + str(curr_num) if curr_num < 10 else str(curr_num))
        return res, int(res, 2)

start = time.perf_counter()
sol = Solution('input.txt')
actual, a = sol.solve()
print(actual)
print(f'Part 1: {a}')
print(f'Time: {time.perf_counter() - start}')

