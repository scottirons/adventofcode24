class Solution:

    def __init__(self, source):
        with open(source, "r") as f:
            self.lines = f.read().split("\n")
        self.b_ops = self.get_ops()
        self.ops = self.b_ops[0:2] 
        self.part_a = 0
        self.part_b = 0
    
    def get_ops(self):
        def mult(a, b):
            return a * b
        def add(a, b):
            return a + b
        def concat(a, b):
            return a * (10 ** len(str(b))) + b
        return [mult, add, concat]
    
    def try_ops(self, target, curr, curr_i, nums, part_b):
        ops = self.b_ops if part_b else self.ops
        if curr_i == len(nums):
            return target == curr
        for op in ops:
            val = op(curr, nums[curr_i])
            if self.try_ops(target, val, curr_i + 1, nums, part_b):
                return True
        return False 
    
    def solve(self):
        for line in self.lines:
            target, vals = line.split(": ")
            vals = [int(val) for val in vals.split(" ")]
            target = int(target)
            all_ops_a = [op(vals[0], vals[1]) for op in self.ops]
            if any(self.try_ops(target, val, 2, vals, False) for val in all_ops_a):
                self.part_a += target

            all_ops_b = [op(vals[0], vals[1]) for op in self.b_ops]
            if any(self.try_ops(target, val, 2, vals, True) for val in all_ops_b):
                self.part_b += target

        return self.part_a, self.part_b

sol = Solution("input.txt")
a, b = sol.solve()
print(f"Part A: {a}")
print(f"Part B: {b}")
