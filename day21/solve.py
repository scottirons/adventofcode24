from functools import cache
from math import inf
import re

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


def move_dir(curr, button):
    return KEYS[curr][button]


def move_number(curr, button):
    if curr == 'A':
        return '0' if button == '<' else '3' if button == '^' else None
    elif curr == '0':
        return 'A' if button == '>' else '2' if button == '^' else None
    elif curr == '2' and button == 'v':
        return '0'
    elif curr == '3' and button == 'v':
        return 'A'
    curr_int = int(curr)
    if button == '^':
        result = curr_int + 3
        if result not in {7, 8, 9, 4, 5, 6}:
            return None
        return str(result)
    if button == '>':
        result = curr_int + 1
        if result not in {8, 5, 2, 9, 6, 3}:
            return None
        return str(result)
    if button == '<':
        result = curr_int - 1
        if result not in {7, 4, 1, 8, 5, 2}:
            return None
        return str(result)
    if button == 'v':
        result = curr_int - 3
        if result not in {4, 5, 6, 1, 2, 3}:
            return None
        return str(result)


def cascade(r1, r2, keypad):
    next_val = None
    if r1 == 'A' and r2 == 'A':
        next_val = keypad
    elif r1 == 'A':
        keypad = move_number(keypad, r2)
    else:
        r2 = move_dir(r2, r1)
    return r1, r2, keypad, next_val


class Solution:
    def __init__(self, input):
        with open(input, 'r') as f:
            self.targets = f.read().splitlines()
        self.memo = {}

    def get_paths(self, r1, r2, keypad, presses, target, seq):
        if presses > 100:
            return inf
        if (r1, r2, keypad, target) in self.memo and self.memo[(r1, r2, keypad, target)] <= presses:
            return inf
        self.memo[(r1, r2, keypad, target)] = presses
        if target == '':
            return presses
        result = inf

        # press A
        r1_next, r2_next, keypad_next, button_press = cascade(r1, r2, keypad)
        if r1_next is None or r2_next is None or keypad_next is None:
            pass
        elif button_press is None:
            result = min(self.get_paths(r1_next, r2_next, keypad_next, presses + 1, target, seq + 'A'), result)
        elif button_press != target[0]:
            pass
        elif button_press == target[0]:
            result = min(self.get_paths(r1_next, r2_next, keypad_next, presses + 1, target[1:], seq + 'A'), result)

        for button in 'v<^>':
            r1_next = move_dir(r1, button)
            if r1_next:
                result = min(self.get_paths(r1_next, r2, keypad, presses + 1, target, seq + button), result)

        return result

    def solve(self):
        total = 0

        for target in self.targets:
            self.memo = {}
            path_cost = self.get_paths('A', 'A', 'A', 0, target, '')
            print(f"Target: {target}, Path Cost: {path_cost}")
            int_part = re.match(r'(\d+)', target)
            total += int(int_part[0]) * path_cost

        return total

sol = Solution('input.txt')
a = sol.solve()
print(f"Answer: {a}")
