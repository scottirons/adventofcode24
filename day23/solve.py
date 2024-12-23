from collections import defaultdict
from time import perf_counter
import networkx as nx


class Solution:
    def __init__(self, source):
        with open(source, 'r') as f:
            self.lines = f.read().split('\n')
        self.pairs = []
        for line in self.lines:
            self.pairs.append(line.split('-'))
        self.groups = defaultdict(set)

    def solve(self):
        visited = set()
        for a, b in self.pairs:
            self.groups[a].add(b)
            self.groups[a].add(a)
            self.groups[b].add(a)
            self.groups[b].add(b)
        for a, b in self.pairs:
            for c in self.groups:
                if a in self.groups[c] and b in self.groups[c] and a != c and b != c:
                    triplet = [a, b, c]
                    triplet.sort()
                    if 't' in (triplet[0][0], triplet[1][0], triplet[2][0]):
                        visited.add(tuple(triplet))
        # networkx so I don't need to do some stinkin' algorithm thingy
        graph = nx.Graph(self.pairs)
        connected = list(nx.find_cliques(graph))
        b = ','.join(sorted(max(connected, key=len)))
        return len(visited), b

start = perf_counter()
sol = Solution('input.txt')
a, b = sol.solve()
print(f'Answer: {a}')
print(f'Answer 2: {b}')
print(f'Time: {perf_counter() - start}')