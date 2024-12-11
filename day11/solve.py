from collections import Counter

with open("input.txt", 'r') as f:
    nums = [int(i) for i in f.read().strip('\n').split(' ')]

counts = Counter(nums)
for i in range(75):
    new_counts = Counter()
    for val in counts:
        l = len(str(val))
        half = int(l / 2)
        if val == 0:
            new_counts[1] += counts[val]
        elif l % 2 == 0:
            a = int(str(val)[0:half])
            b = int(str(val)[half:l + 1])
            new_counts[a] += counts[val]
            new_counts[b] += counts[val]
        else:
            new_counts[val * 2024] += counts[val]
    counts = new_counts

print(sum(counts[i] for i in counts))
