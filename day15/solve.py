class Solution:
    def __init__(self, source):
        with open(source, 'r') as f:
            grid, ins = f.read().split("\n\n")
        self.grid = [list(line) for line in grid.split('\n')]
        self.grid_b = []
        for line in self.grid:
            new_line = []
            for c in line:
                if c == '#':
                    new_line.append("#")
                    new_line.append("#")
                elif c == '.':
                    new_line.append(".")
                    new_line.append(".")
                elif c == '@':
                    new_line.append("@")
                    new_line.append(".")
                elif c == 'O':
                    new_line.append("[")
                    new_line.append("]")
            self.grid_b.append(new_line)
        self.ins = ins.replace('\n', '')
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == '@':
                    self.start_a = (i, j)
        for i in range(len(self.grid_b)):
            for j in range(len(self.grid_b[0])):
                if self.grid_b[i][j] == '@':
                    self.start_b = (i, j)
        self.part_a = 0
        self.part_b = 0
        self.dir_key = {
            '>': (0, 1),
            'v': (1, 0),
            '^': (-1, 0),
            '<': (0, -1)
        }

    def horizontal_box_swap(self, i, j):
        if self.grid_b[i][j] == '[':
            self.grid_b[i][j] = ']'
        else:
            self.grid_b[i][j] = '['

    def move_b(self, start_i, start_j, d):
        ii, jj = start_i, start_j
        swap = '@'
        swap_i = ii
        swap_j = jj
        move_i, move_j = self.dir_key[d]
        move_vert = bool(move_i)
        # move up or down
        # all the boxes we'll have to move up or down
        all_move = [(start_i, start_j)]
        # current set of boxes above which we are checking (set so I don't have to worry about duplicates for boxes that
        # we only hit half of
        curr_row = {(start_i, start_j)}
        while move_vert:
            next_row = set()
            for ii, jj in curr_row:
                i, j = ii + move_i, jj + move_j
                curr = self.grid_b[i][j]
                # only easy case lol
                if curr == '.' and len(all_move) == 1:
                    self.grid_b[i][j] = '@'
                    self.grid_b[start_i][start_j] = '.'
                    return i, j
                elif curr in '[]':
                    next_row.add((i, j))
                    if curr == '[':
                        next_row.add((i, j + 1))
                    else:
                        next_row.add((i, j - 1))
                elif curr == '#':
                    return start_i, start_j
            # should be when they're all dots above and I can move the mass
            if not next_row:
                for c in range(len(all_move) - 1, -1, -1):
                    i, j = all_move[c]
                    self.grid_b[i + move_i][j + move_j] = self.grid_b[i][j]
                    self.grid_b[i][j] = '.'
                return start_i + move_i, start_j + move_j
            else:
                all_move += list(next_row)
                curr_row = next_row

        # moving horizontally (almost the same)
        curr_path = []
        while not move_vert:
            ii, jj = ii + move_i, jj + move_j
            curr = self.grid_b[ii][jj]
            if curr == '.':
                self.grid_b[ii][jj] = swap
                self.grid_b[swap_i][swap_j] = '.'
                if swap in '[]':
                    self.grid_b[swap_i][swap_j] = '@'
                    self.grid_b[start_i][start_j] = '.'
                    for i, j in curr_path:
                        self.horizontal_box_swap(i, j)
                    return swap_i, swap_j
                return ii, jj
            elif curr in '[]':
                if swap == '@':
                    swap = '[]'[('[]'.index(curr) + 1) % 2] # jank lol
                    swap_i = ii
                    swap_j = jj
                else:
                    curr_path.append((ii, jj))
            elif curr == '#':
                return start_i, start_j

    def move_a(self, start_i, start_j, d):
        ii, jj = start_i, start_j
        swap = '@'
        swap_i = ii
        swap_j = jj
        move_i, move_j = self.dir_key[d]
        while True:
            ii, jj = ii + move_i, jj + move_j
            curr = self.grid[ii][jj]
            if curr == '.':
                self.grid[ii][jj] = swap
                self.grid[swap_i][swap_j] = '.'
                if swap == 'O':
                    self.grid[swap_i][swap_j] = '@'
                    self.grid[start_i][start_j] = '.'
                    return swap_i, swap_j
                return ii, jj
            elif curr == 'O':
                if swap != 'O':
                    swap = 'O'
                    swap_i = ii
                    swap_j = jj
            elif curr == '#':
                return start_i, start_j

    def solve(self):
        i, j = self.start_a
        for ins in self.ins:
            i, j = self.move_a(i, j, ins)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 'O':
                    self.part_a += 100 * i + j
        i, j = self.start_b
        for ins in self.ins:
            i, j = self.move_b(i, j, ins)
        for i in range(len(self.grid_b)):
            for j in range(len(self.grid_b[0])):
                if self.grid_b[i][j] == '[':
                    self.part_b += 100 * i + j
        return self.part_a, self.part_b


sol = Solution('input.txt')
a, b = sol.solve()
print(f"Part A: {a}")
print(f"Part B: {b}")