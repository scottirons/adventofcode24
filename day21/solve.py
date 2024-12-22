from functools import cache
from itertools import pairwise
from math import inf
import re
from time import perf_counter

KEYS = {
    '>':
        {'>': None, 'v': None, '<': 'v', '^': 'A'},
    'v':
        {'>': '>', 'v': None, '<': '<', '^': '^'},
    '<':
        {'>': 'v', 'v': None, '<': None, '^': None},
    '^':
        {'>': 'A', 'v': 'v', '<': None, '^': None},
    'A':
        {'>': None, 'v': '>', '<': '^', '^': None},
}

NUMS = {
    '0':
        {'>': 'A', 'v': None, '<': None, '^': '2'},
    '1':
        {'>': '2', 'v': None, '<': None, '^': '4'},
    '2':
        {'>': '3', 'v': '0', '<': '1', '^': '5'},
    '3':
        {'>': None, 'v': 'A', '<': '2', '^': '6'},
    '4':
        {'>': '5', 'v': '1', '<': None, '^': '7'},
    '5':
        {'>': '6', 'v': '2', '<': '4', '^': '8'},
    '6':
        {'>': None, 'v': '3', '<': '5', '^': '9'},
    '7':
        {'>': '8', 'v': '4', '<': None, '^': None},
    '8':
        {'>': '9', 'v': '5', '<': '7', '^': None},
    '9':
        {'>': None, 'v': '6', '<': '8', '^': None},
    'A':
        {'>': None, 'v': None, '<': '0', '^': '3'},
}

KEY_BEST = {
    '>': {
        'v': '<A',
        '<': '<<A',
        '^': '<^A',
        'A': '^A',
        '>': 'A'
    },
    '<': {
        'v': '>A',
        '>': '>>A',
        '^': '>^A',
        'A': '>>^A',
        '<': 'A'
    },
    'v': {
        '>': '>A',
        '<': '<A',
        '^': '^A',
        'A': '^>A',
        'v': 'A'
    },
    '^': {
        'v': 'vA',
        '<': 'v<A',
        '>': 'v>A',
        'A': '>A',
        '^': 'A'
    },
    'A': {
        'v': '<vA',
        '<': 'v<<A',
        '^': '<A',
        '>': 'vA',
        'A': 'A'
    }
}

NUM_BEST = {
    '0': {'1': '^<A', '2': '^A', '3': '^>A', '4': '^^<A', '5': '^^A', '6': '^^>A', '7': '^^^<A', '8': '^^^A', '9': '^^^>A', 'A': '>A', '0': 'A'},
    '1': {'0': '>vA', '2': '>A', '3': '>>A', '4': '^A', '5': '^>A', '6': '^>>A', '7': '^^A', '8': '^^>A', '9': '^^>>A', 'A': '>>vA', '1': 'A'},
    '2': {'1': '<A', '0': 'vA', '3': '>A', '4': '<^A', '5': '^A', '6': '^>A', '7': '<^^A', '8': '^^A', '9': '^^>A', 'A': 'v>A', '2': 'A'},
    '3': {'1': '<<A', '2': '<A', '0': '<vA', '4': '<<^A', '5': '<^A', '6': '^A', '7': '<<^^A', '8': '<^^A', '9': '^^A', 'A': 'vA', '3': 'A'},
    '4': {'1': 'vA', '2': 'v>A', '3': 'v>>A', '0': '>vvA', '5': '>A', '6': '>>A', '7': '^A', '8': '^>A', '9': '^>>A', 'A': '>>vvA', '4': 'A'},
    '5': {'1': '<vA', '2': 'vA', '3': 'v>A', '4': '<A', '0': 'vvA', '6': '>A', '7': '<^A', '8': '^A', '9': '^>A', 'A': 'vv>A', '5': 'A'},
    '6': {'1': '<<vA', '2': '<vA', '3': 'vA', '4': '<<A', '5': '<A', '0': '<vvA', '7': '<<^A', '8': '<^A', '^9': 'A', 'A': 'vvA', '6': 'A'},
    '7': {'1': 'vvA', '2': 'vv>A', '3': 'vv>>A', '4': 'vA', '5': 'v>A', '6': 'v>>A', '0': '>vvvA', '8': '>A', '9': '>>A', 'A': '>>vvvA', '7': 'A'},
    '8': {'1': '<vvA', '2': 'vvA', '3': 'vv>A', '4': '<vA', '5': 'vA', '6': 'v>A', '7': '<A', '0': 'vvvA', '9': '>A', 'A': 'vvv>A', '8': 'A'},
    '9': {'1': '<<vvA', '2': '<vvA', '3': 'vvA', '4': '<<vA', '5': '<vA', '6': 'vA', '7': '<<A', '8': '<A', '0': '<vvvA', 'A': 'vvvA', '9': 'A'},
    'A': {'1': '^<<A', '2': '<^A', '3': '^A', '4': '^^<<A', '5': '<^^A', '6': '^^A', '7': '^^^<<A', '8': '<^^^A', '9': '^^^A', '0': '<A', 'A': 'A'},
}

# def move_dir(curr, button):
#     return KEYS[curr][button]
#
#
# def move_number(curr, button):
#     return NUMS[curr][button]
#
# def find_best_path(start, end):
#     path = ''
#     return path
#
#
#
#
# def cascade(locations):
#     locs_list = list(locations)
#     next_val = None
#     valid = True
#     i = 0
#     while i < len(locs_list) - 1:
#         r1 = locs_list[i]
#         r2 = locs_list[i + 1]
#         # just move the next one in the sequence and break
#         if r1 in '<^v>':
#             if i == len(locs_list) - 2:
#                 r2 = move_number(r2, r1)
#             else:
#                 r2 = move_dir(r2, r1)
#             if not r2:
#                 valid = False
#             locs_list[i + 1] = r2
#             break
#         #
#         elif r1 == 'A':
#             if i == len(locs_list) - 2:
#                 next_val = r2
#                 break # don't need to but oh well
#             i += 1
#
#     return tuple(locs_list), valid, next_val


class Solution:
    def __init__(self, source):
        with open(source, 'r') as f:
            self.targets = f.read().splitlines()
        self.memo = {}

    # def get_paths(self, locs, presses, target):
    #     if (locs, target) in self.memo and self.memo[(locs, target)] <= presses:
    #         return inf
    #     self.memo[(locs, target)] = presses
    #     if target == '':
    #         return presses
    #     result = inf
    #
    #     # press A
    #     next_locs, valid, button_press = cascade(locs)
    #     if valid:
    #         if button_press is None:
    #             result = min(result, self.get_paths(next_locs, presses + 1, target))
    #         elif button_press == target[0]:
    #             result = min(result, self.get_paths(next_locs, presses + 1, target[1:]))
    #
    #     loc_list = list(locs)
    #     for button in 'v<^>':
    #         r1_next = move_dir(locs[0], button)
    #         if r1_next:
    #             loc_list[0] = r1_next
    #             result = min(self.get_paths(tuple(loc_list), presses + 1, target), result)
    #
    #     return result
    #
    # def solve(self, part_b=False):
    #     total = 0
    #
    #     for target in self.targets:
    #         self.memo = {}
    #         locations = ('A', 'A', 'A')
    #         if part_b:
    #             locations = tuple('A' for _ in range(4))
    #         path_cost = self.get_paths(locations, 0, target)
    #         print(f"Target: {target}, Path Cost: {path_cost}")
    #         int_part = re.match(r'(\d+)', target)
    #         total += int(int_part[0]) * path_cost
    #
    #     return total

    @cache
    def search(self, seq, level, nums=True):
        res = 0
        seq = "A" + seq
        for u, v in pairwise(seq):
            if nums:
                new_path = NUM_BEST[u][v]
            else:
                new_path = KEY_BEST[u][v]
            if level == 0:
                res += len(new_path)
            else:
                res += self.search(new_path, level - 1, False)
        return res

    def solve_2(self):
        result1 = 0
        result2 = 0
        for target in self.targets:
            val1 = self.search(target, 2)
            val2 = self.search(target, 25)
            # print(f'Target: {target}, Path Cost: {val1}')
            result1 += int(target[:-1]) * val1
            result2 += int(target[:-1]) * val2
        return result1, result2



start = perf_counter()
sol = Solution('input.txt')
a, b = sol.solve_2()
print(f"A: {a}")
print(f"B: {b}")
print(f"Time: {perf_counter() - start}")

