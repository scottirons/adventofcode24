import re
import time
from time import perf_counter

class Solution:
    def __init__(self, source):
        with open(source, 'r') as f:
            data = f.read()
        nums = [int(val) for val in re.findall(r'\d+', data)]
        self.a, self.b, self.c = nums[0], nums[1], nums[2]
        self.ins = nums[3:]
        self.pointer = 0
        self.result = []

    def process(self):
        op1, op2 = self.ins[self.pointer], self.ins[self.pointer + 1]
        jump = True
        if op1 in {0, 2, 5, 6, 7}:
            if op2 == 4:
                op2 = self.a
            elif op2 == 5:
                op2 = self.b
            elif op2 == 6:
                op2 = self.c

        if op1 == 0:
            self.a = int(self.a / (2 ** op2))
        elif op1 == 1:
            self.b = self.b ^ op2
        elif op1 == 2:
            self.b = op2 % 8
        elif op1 == 3:
            if self.a != 0:
                self.pointer = op2
                jump = False
        elif op1 == 4:
            self.b = self.b ^ self.c
        elif op1 == 5:
            self.result.append(op2 % 8)
        elif op1 == 6:
            self.b = int(self.a / (2 ** op2))
        elif op1 == 7:
            self.c = int(self.a / (2 ** op2))
        if jump:
            self.pointer += 2

    def solve_a(self):
        while self.pointer < len(self.ins):
            self.process()
        # print(f"Register A: {self.a}\nRegister B: {self.b}\nRegister C: {self.c}")
        return ','.join(str(val) for val in self.result)

    def solve_b(self):
        curr = 0
        self.a = curr
        self.b = 0
        self.c = 0
        self.pointer = 0
        self.result = []
        final_digits = 1
        # 0,3,5,4,3,0
        while True:
            self.process()
            if self.pointer >= len(self.ins) and self.result == self.ins:
                return curr
            # restart if we're already off
            if self.result == self.ins[-final_digits:] and final_digits < len(self.ins):
                final_digits += 1
                curr *= 8
                self.a = curr
                self.b = 0
                self.c = 0
                self.pointer = 0
                self.result = []
            if self.pointer >= len(self.ins):
                curr += 1
                self.a = curr
                self.b = 0
                self.c = 0
                self.pointer = 0
                self.result = []

start = time.perf_counter()
sol = Solution('input.txt')
a = sol.solve_a()
print(f"Part A: {a}")
b = sol.solve_b()
print(f"Part B: {b}")
print(f"Time: {time.perf_counter() - start}")
# 3,2,3,0,2,4,1,5,3