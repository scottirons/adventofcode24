from collections import defaultdict

class Solution:
    def __init__(self, source):
        self.total_a = 0
        self.total_b = 0
        with open(source, "r") as f:
            rules, patterns = f.read().split("\n\n")
            rules = rules.split("\n")
            self.patterns = patterns.split("\n")
        self.rule_dict = defaultdict(set)
        for rule in rules:
            a, b = rule.split("|")
            self.rule_dict[a].add(b)

    def valid_list(self, p_list):
        for i in range(len(p_list) - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                if p_list[j] in self.rule_dict[p_list[i]]:
                    return False
        return True
    
    def reorder(self, p_list):
        # put it backwards in list of same length as this one based on how many of the other numbers 
        # are in the set of numbers that must appear after it (idk you get what I'm saying I think lol haha)
        new_list = [None for _ in p_list]
        for i in p_list:
            count = 0
            for j in p_list:
                if j in self.rule_dict[i]:
                    count += 1
            new_list[count] = i
        return int(new_list[int((len(new_list) - 1) / 2)])

    def solve_a(self):
        for pattern in self.patterns:
            p_list = pattern.split(",")
            if self.valid_list(p_list):
                self.total_a += int(p_list[int((len(p_list) - 1) / 2)])
            else:
                self.total_b += self.reorder(p_list)
        return self.total_a, self.total_b

sol = Solution("input.txt")
a, b = sol.solve_a()
print(f"Part A: {a}")
print(f"Part B: {b}")