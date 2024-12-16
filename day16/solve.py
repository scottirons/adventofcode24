from heapq import heappush, heappop
from time import perf_counter
from math import inf

start = perf_counter()
with open('input.txt', 'r') as f:
    grid = f.read().split('\n')

n, m = len(grid), len(grid[0])

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # rdlu
best_paths = set()

check = [(0, 0, n - 2, 1, [(n - 2, 1)])] # score, dir, i, j, path
visited = {}
actual_score = inf

while True:
    score, d, i, j, path = heappop(check)
    if score > actual_score:
        break
    elif grid[i][j] == 'E' and score == actual_score:
        for p in path:
            best_paths.add(p)
    elif grid[i][j] == 'E':
        print(f"Part A: {score}")
        actual_score = score
        for p in path:
            best_paths.add(p)

    if (d, i, j) in visited and visited[(d, i, j)] < score:
        continue
    visited[(d, i, j)] = score

    # try turn left
    left = (d - 1) % 4
    li, lj = dirs[left]
    if grid[i + li][j + lj] in '.E':
        new_path = list(path)
        new_path.append((i + li, j + lj))
        heappush(check, (score + 1001, left, i + li, j + lj, new_path))

    # try turn right
    right = (d + 1) % 4
    ri, rj = dirs[right]
    if grid[i + ri][j + rj] in '.E':
        new_path = list(path)
        new_path.append((i + ri, j + rj))
        heappush(check, (score + 1001, right, i + ri, j + rj, new_path))

    # try go straight
    si, sj = dirs[d]
    if grid[i + si][j + sj] in '.E':
        new_path = list(path)
        new_path.append((i + si, j + sj))
        heappush(check, (score + 1, d, i + si, j + sj, new_path))

print(f'Part B: {len(best_paths)}')
print(f"Total Time: {perf_counter() - start}")