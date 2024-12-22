from collections import deque, defaultdict

MOD = 16777216

with open('input.txt', 'r') as f:
    nums = [int(num) for num in f.read().splitlines()]

total_a = 0
b_max = 0
best_seq = None
seq_dict = defaultdict(int)

for num in nums:
    visited = set()
    prev = num % 10
    seq = deque()
    for _ in range(2000):
        prev_num = num
        num = int(num * 64) ^ num
        num = num % MOD
        num = int(num / 32) ^ num
        num = num % MOD
        num = int(num * 2048) ^ num
        num = num % MOD

        ones = num % 10
        diff = ones - prev
        seq.append(diff)
        if len(seq) == 5:
            seq.popleft() # I don't need to use a deque, but it's fun :D :D :D :D :D :D
        if len(seq) == 4:
            tup_seq = tuple(seq)
            if tup_seq not in visited:
                seq_dict[tup_seq] += ones
                if seq_dict[tup_seq] > b_max:
                    best_seq = tup_seq
                    b_max = seq_dict[tup_seq]
                visited.add(tup_seq)
        prev = num % 10

    total_a += num

print(total_a)
print(b_max)
print(best_seq)
